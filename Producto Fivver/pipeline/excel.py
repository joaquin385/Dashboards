"""Lee la hoja que el asistente nombró. No elige la primera del libro."""

import zipfile
from pathlib import Path
from xml.etree import ElementTree

_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
_PKG = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def leer(archivo: Path, solapa: str) -> tuple[list[str], list[dict[str, str]]]:
    with zipfile.ZipFile(archivo) as libro:
        nombres = _solapas(libro)
        if solapa not in nombres:
            lista = ", ".join(nombres)
            raise ValueError(f"La hoja {solapa} no está en el libro. Hay: {lista}.")
        compartidas = _compartidas(libro)
        raiz = ElementTree.fromstring(libro.read(nombres[solapa]))
    filas = [_fila(nodo, compartidas) for nodo in raiz.iter(f"{_MAIN}row")]
    if not filas or not any(filas[0]):
        raise ValueError(f"La hoja {solapa} no tiene encabezado.")
    encabezado = filas[0]
    datos = []
    for cruda in filas[1:]:
        fila = {
            encabezado[indice]: cruda[indice] if indice < len(cruda) else ""
            for indice in range(len(encabezado))
            if encabezado[indice]
        }
        if any(fila.values()):
            datos.append(fila)
    return encabezado, datos


def escribir(archivo: Path, solapas: dict[str, tuple[list[str], list[dict[str, str]]]]) -> None:
    """Arma un libro chico, con el orden en que vienen las solapas."""

    partes: dict[str, str] = {
        "[Content_Types].xml": _tipos(len(solapas)),
        "_rels/.rels": _rels_raiz(),
        "xl/workbook.xml": _libro(list(solapas)),
        "xl/_rels/workbook.xml.rels": _rels_libro(len(solapas)),
    }
    for numero, (columnas, filas) in enumerate(solapas.values(), start=1):
        partes[f"xl/worksheets/sheet{numero}.xml"] = _hoja(columnas, filas)
    archivo.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archivo, "w", compression=zipfile.ZIP_DEFLATED) as libro:
        for nombre, texto in partes.items():
            libro.writestr(nombre, texto.encode("utf-8"))


def _solapas(libro: zipfile.ZipFile) -> dict[str, str]:
    raiz = ElementTree.fromstring(libro.read("xl/workbook.xml"))
    rels = ElementTree.fromstring(libro.read("xl/_rels/workbook.xml.rels"))
    destinos = {
        nodo.attrib["Id"]: _unir("xl", nodo.attrib["Target"])
        for nodo in rels
        if nodo.tag == f"{_PKG}Relationship"
    }
    salida = {}
    for hoja in raiz.iter(f"{_MAIN}sheet"):
        salida[hoja.attrib["name"]] = destinos[hoja.attrib[f"{_REL}id"]]
    return salida


def _unir(base: str, destino: str) -> str:
    if destino.startswith("/"):
        return destino.lstrip("/")
    partes = base.split("/")
    for tramo in destino.split("/"):
        if tramo == "..":
            partes.pop()
        elif tramo and tramo != ".":
            partes.append(tramo)
    return "/".join(partes)


def _compartidas(libro: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in libro.namelist():
        return []
    raiz = ElementTree.fromstring(libro.read("xl/sharedStrings.xml"))
    return ["".join(nodo.itertext()) for nodo in raiz.findall(f"{_MAIN}si")]


def _fila(nodo: ElementTree.Element, compartidas: list[str]) -> list[str]:
    celdas: dict[int, str] = {}
    for celda in nodo.findall(f"{_MAIN}c"):
        celdas[_indice(celda.attrib.get("r", "A1"))] = _texto(celda, compartidas)
    if not celdas:
        return []
    ancho = max(celdas) + 1
    return [celdas.get(indice, "") for indice in range(ancho)]


def _indice(referencia: str) -> int:
    letras = []
    for caracter in referencia:
        if caracter.isalpha():
            letras.append(caracter)
        else:
            break
    numero = 0
    for caracter in letras:
        numero = numero * 26 + ord(caracter.upper()) - 64
    return numero - 1


def _texto(celda: ElementTree.Element, compartidas: list[str]) -> str:
    tipo = celda.attrib.get("t")
    if tipo == "inlineStr":
        return "".join(celda.itertext())
    valor = celda.find(f"{_MAIN}v")
    if valor is None or valor.text is None:
        return ""
    if tipo == "s":
        return compartidas[int(valor.text)]
    return valor.text


def _tipos(cantidad: int) -> str:
    hojas = "".join(
        "<Override PartName=\"/xl/worksheets/sheet"
        f"{numero}.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\"/>"
        for numero in range(1, cantidad + 1)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        f"{hojas}</Types>"
    )


def _rels_raiz() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        "</Relationships>"
    )


def _libro(nombres: list[str]) -> str:
    hojas = "".join(
        f'<sheet name="{_xml(nombre)}" sheetId="{numero}" r:id="rId{numero}"/>'
        for numero, nombre in enumerate(nombres, start=1)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f"<sheets>{hojas}</sheets></workbook>"
    )


def _rels_libro(cantidad: int) -> str:
    rels = "".join(
        f'<Relationship Id="rId{numero}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{numero}.xml"/>'
        for numero in range(1, cantidad + 1)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        f"{rels}</Relationships>"
    )


def _hoja(columnas: list[str], filas: list[dict[str, str]]) -> str:
    filas_xml = [_celdas(1, columnas)]
    for numero, fila in enumerate(filas, start=2):
        filas_xml.append(_celdas(numero, [fila.get(columna, "") for columna in columnas]))
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f"<sheetData>{''.join(filas_xml)}</sheetData></worksheet>"
    )


def _celdas(numero: int, valores: list[str]) -> str:
    celdas = []
    for indice, valor in enumerate(valores):
        letra = _letra(indice)
        celdas.append(
            f'<c r="{letra}{numero}" t="inlineStr"><is><t>{_xml(valor)}</t></is></c>'
        )
    return f'<row r="{numero}">{"".join(celdas)}</row>'


def _letra(indice: int) -> str:
    indice += 1
    letras = ""
    while indice:
        indice, resto = divmod(indice - 1, 26)
        letras = chr(65 + resto) + letras
    return letras


def _xml(texto: str) -> str:
    return (
        texto.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
