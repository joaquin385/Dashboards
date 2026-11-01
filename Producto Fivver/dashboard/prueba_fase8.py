"""Cierra la lectura del tablero: tres gráficos en una hoja."""

import csv
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from caso.archivos import PESOS, filas_ventas, escribir as escribir_archivos
from caso.corrida import encargo_copia, encargo_loma, instruccion_copia, instruccion_loma, marcas_loma
from caso.cuenta import FACTURACION, POR_PRODUCTO
from caso.nota_loma import escribir_copia, escribir_loma
from caso.suciedad import COLUMNAS, SUCIO, escribir as escribir_sucio, filas_sucias
from dashboard.html import escribir
from informe.nota import revisar
from pipeline.correr import Ficha, Resultado, correr
from pipeline.prueba_fase6 import _nota_inglesa


def _otro(camino: Path) -> None:
    filas = []
    for numero, origen in enumerate(filas_ventas(), start=1):
        unidades = int(origen["unidades"]) * 2
        precio = int(origen["precio"])
        filas.append(
            {
                "fecha": origen["fecha"],
                "producto": origen["producto"],
                "unidades": str(unidades),
                "precio": origen["precio"],
                "costo": origen["costo"],
                "importe": str(unidades * precio),
                "ticket": f"D{numero:04d}",
                "nota": "",
            }
        )
    with camino.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)
        escritor.writeheader()
        escritor.writerows(filas)


def _graficos(pagina: str) -> list[str]:
    return [
        linea.split('data-grafico="', 1)[1].split('"', 1)[0]
        for linea in pagina.splitlines()
        if 'data-grafico="' in linea
    ]


def _pesos(valor: int) -> str:
    return f"{valor:,}".replace(",", ".")


class PantallaDeLoma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        escribir_sucio()
        cls.temporal = tempfile.TemporaryDirectory()
        cls.otro_archivo = Path(cls.temporal.name) / "loma-otro.csv"
        _otro(cls.otro_archivo)
        cls.instruccion = instruccion_loma()
        cls.encargo = encargo_loma(len(filas_sucias()))
        cls.resultado = correr(cls.encargo, SUCIO, cls.instruccion, marcas_loma())
        cls.nota = revisar(escribir_loma(cls.resultado), cls.resultado, cls.encargo)
        cls.pagina = escribir(cls.resultado, cls.nota, cls.instruccion, "Loma", cls.encargo)
        cls.otro = correr(encargo_loma(205), cls.otro_archivo, cls.instruccion, marcas_loma())
        cls.nota_otro = revisar(escribir_loma(cls.otro), cls.otro, encargo_loma(205))
        cls.pagina_otro = escribir(cls.otro, cls.nota_otro, cls.instruccion, "Loma", encargo_loma(205))

    @classmethod
    def tearDownClass(cls):
        cls.temporal.cleanup()

    def test_tres_graficos_de_izquierda_a_derecha(self):
        self.assertEqual(_graficos(self.pagina), ["evolucion", "piezas", "atributo"])
        self.assertIn("Evolución", self.pagina)
        self.assertIn("Piezas", self.pagina)
        self.assertIn("Ventas por atributo", self.pagina)
        self.assertIn("572.000", self.pagina)
        self.assertIn("1.450.000", self.pagina)
        self.assertIn("494.000", self.pagina)
        self.assertIn("58.000", self.pagina)
        self.assertIn("−936.000", self.pagina)
        self.assertIn("312.000", self.pagina)
        self.assertIn("260.000", self.pagina)
        self.assertIn("Cordel", self.pagina)
        self.assertIn("Soga", self.pagina)
        self.assertIn("Maroma", self.pagina)
        self.assertIn('data-diferencia="-878000"', self.pagina)

    def test_el_hallazgo_va_en_tarjetas_antes_de_los_graficos(self):
        cabeza = self.pagina.split('data-grafico="evolucion"', 1)[0]
        self.assertIn('class="costado"', cabeza)
        tarjetas = cabeza.split('class="hallazgos"', 1)[1]
        self.assertIn("572.000", tarjetas)
        self.assertIn("878.000 abajo", tarjetas)
        self.assertIn("78.000 arriba", tarjetas)
        self.assertIn("1.450.000", tarjetas)
        self.assertIn("494.000", tarjetas)
        self.assertIn(">Tablero<", self.pagina)
        otro = self.pagina_otro.split('class="hallazgos"', 1)[1].split('data-grafico="evolucion"', 1)[0]
        self.assertNotIn("878.000 abajo", otro)
        self.assertIn(_pesos(self.otro.ficha("monitoreo").huecos["total"]), otro)

    def test_los_pesos_de_las_fichas_no_se_mueven(self):
        self.assertEqual(
            self.resultado.ficha("calendario").huecos["facturacion_por_dia"]["2026-08"],
            58_000,
        )
        self.assertEqual(
            self.resultado.ficha("calendario").huecos["facturacion_por_dia"]["2026-09"],
            22_000,
        )
        self.assertEqual(
            self.resultado.ficha("el_que_se_aparta").huecos["nivel_de_cada_grupo"]["Cordel"],
            312_000,
        )
        self.assertEqual(
            self.resultado.ficha("el_que_se_aparta").huecos["resta_de_cada_grupo"]["Maroma"],
            POR_PRODUCTO["Maroma"],
        )
        self.assertEqual(self.resultado.ficha("monitoreo").huecos["diferencia"], -878_000)
        self.assertEqual(self.resultado.ficha("lo_que_queda").huecos["queda"], 312_000)

    def test_el_titulo_y_los_filtros_van_antes_de_los_graficos(self):
        self.assertIn("<h1>Loma</h1>", self.pagina)
        cabeza = self.pagina.split('data-grafico="evolucion"', 1)[0]
        self.assertIn('data-filtro="fecha"', cabeza)
        self.assertIn('data-filtro="producto"', cabeza)
        self.assertIn(">Fecha<", cabeza)
        self.assertIn(">Producto<", cabeza)
        self.assertIn(">Todos<", cabeza)
        self.assertIn('class="disparador"', cabeza)
        self.assertIn('class="flecha"', cabeza)
        fecha = cabeza.split('data-filtro="fecha"', 1)[1].split('data-filtro="producto"', 1)[0]
        self.assertIn('data-anio="2025"', fecha)
        self.assertIn('data-anio="2026"', fecha)
        self.assertIn(">septiembre<", fecha)
        self.assertIn(">agosto<", fecha)
        self.assertIn('data-anio="2026" data-mes="9" data-dia="17"', fecha)
        self.assertNotIn('data-anio="2026" data-mes="8" data-dia="17"', fecha)
        self.assertIn(">Cordel<", cabeza)
        self.assertIn(">Soga<", cabeza)
        self.assertIn(">Maroma<", cabeza)
        self.assertNotIn('data-filtro="local"', self.pagina)
        self.assertNotIn('data-filtro=', self.pagina.split('data-grafico="evolucion"', 1)[1])

    def test_la_historia_nombra_lo_que_la_cuenta_muestra(self):
        self.assertIn(">Reproducir<", self.pagina)
        self.assertIn('id="historia"', self.pagina)
        self.assertIn("878.000 abajo", self.pagina)
        self.assertIn("78.000 arriba", self.pagina)
        self.assertIn("58.000 arriba", self.pagina)
        self.assertIn("936.000 abajo", self.pagina)
        self.assertIn("Cordel queda en 312.000", self.pagina)
        self.assertIn("Maroma queda en 0", self.pagina)
        self.assertNotIn("878.000 abajo", self.pagina_otro)

    def test_el_glosario_dice_como_se_construye(self):
        self.assertIn(">Glosario<", self.pagina)
        self.assertIn(">Volver<", self.pagina)
        glosario = self.pagina.split('class="glosario"', 1)[1]
        self.assertIn("unidades por precio", glosario)
        self.assertIn("cantidad, mezcla, precio", glosario)
        self.assertIn("estira las unidades", glosario)
        self.assertIn("No es la resta contra", glosario)
        self.assertIn("lunes a sábado", glosario)

    def test_el_informe_cuenta_los_hallazgos_en_parrafos(self):
        self.assertIn(">Informe<", self.pagina)
        informe = self.pagina.split('class="informe"', 1)[1].split("</section>", 1)[0]
        self.assertIn("878.000 abajo", informe)
        self.assertIn("78.000 arriba", informe)
        self.assertIn("936.000 abajo", informe)
        self.assertIn("Maroma", informe)
        self.assertIn("1.000.000 abajo", informe)
        self.assertIn("No es la causa", informe)
        self.assertIn("no alcanza para firmar", informe)
        self.assertIn("312.000", informe)
        self.assertNotIn("878.000 abajo", self.pagina_otro.split('class="informe"', 1)[1].split("</section>", 1)[0])

    def test_el_otro_archivo_mueve_los_numeros_y_deja_la_estructura(self):
        self.assertEqual(_graficos(self.pagina), _graficos(self.pagina_otro))
        self.assertIn('data-diferencia="-1756000"', self.pagina_otro)
        self.assertNotIn('data-diferencia="-878000"', self.pagina_otro)
        self.assertIn("2.900.000", self.pagina_otro)
        self.assertIn("1.144.000", self.pagina_otro)
        self.assertEqual(self.pagina_otro.count('data-filtro="producto"'), 1)


class CopiaYDecision(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        escribir_archivos()
        escribir_sucio()
        cls.instruccion = instruccion_copia()
        cls.encargo = replace(encargo_copia(77), abre="pesos_de_un_mes")
        cls.resultado = correr(cls.encargo, PESOS, cls.instruccion)
        cls.nota_escrita = escribir_copia(cls.resultado)
        cls.nota = revisar(cls.nota_escrita, cls.resultado, cls.encargo)
        cls.pagina = escribir(
            cls.resultado,
            cls.nota,
            cls.instruccion,
            "Loma",
            cls.encargo,
            cls.nota_escrita.huecos_vacios,
        )

    def test_la_copia_deja_los_tres_lugares_y_no_inventa_piezas(self):
        self.assertEqual(_graficos(self.pagina), ["evolucion", "piezas", "atributo"])
        monitoreo = self.resultado.ficha("monitoreo")
        anio = self.resultado.ficha("anio_pasado")
        self.assertIn(_pesos(monitoreo.huecos["total"]), self.pagina)
        self.assertIn(_pesos(monitoreo.huecos["total_base"]), self.pagina)
        self.assertIn(_pesos(anio.huecos["total_base"]), self.pagina)
        piezas = self.pagina.split('data-grafico="piezas"', 1)[1].split('data-grafico="atributo"', 1)[0]
        self.assertNotIn("<svg", piezas)
        self.assertIn('data-filtro="fecha"', self.pagina)
        self.assertNotIn('data-filtro="producto"', self.pagina)
        glosario = self.pagina.split('class="glosario"', 1)[1].split("</section>", 1)[0]
        self.assertIn("el de la columna del archivo", glosario)
        self.assertNotIn("estira las unidades", glosario)
        self.assertNotIn("No es la resta contra", glosario)
        self.assertEqual(self.resultado.ficha("pesos_de_un_mes").huecos["constantes"]["2026-09"], 260_000)

    def test_una_decision_no_cambia_los_tres_graficos(self):
        escribir_sucio()
        encargo = replace(
            encargo_loma(len(filas_sucias())),
            abre="lo_que_queda",
            decision="Mirar lo que queda antes de reponer.",
        )
        resultado = correr(encargo, SUCIO, instruccion_loma(), marcas_loma())
        nota = revisar(escribir_loma(resultado), resultado, encargo_loma(len(filas_sucias())))
        pagina = escribir(resultado, nota, instruccion_loma(), "Loma", encargo)
        self.assertEqual(_graficos(pagina), ["evolucion", "piezas", "atributo"])
        self.assertEqual(
            resultado.ficha("lo_que_queda").huecos["queda"] - resultado.ficha("lo_que_queda").huecos["queda_base"],
            -338_000,
        )


class IdiomaYPersona(unittest.TestCase):
    def test_en_ingles_los_numeros_siguen_y_la_nota_pasa(self):
        escribir_sucio()
        encargo = replace(encargo_loma(len(filas_sucias())), idioma="en")
        resultado = correr(encargo, SUCIO, instruccion_loma(), marcas_loma())
        nota = revisar(_nota_inglesa(), resultado, encargo)
        pagina = escribir(resultado, nota, instruccion_loma(), "Loma", encargo)
        self.assertIn("Trend", pagina)
        self.assertIn("Sales by attribute", pagina)
        self.assertIn("September 2026", pagina)
        self.assertIn("312.000", pagina)
        self.assertIn('data-diferencia="-878000"', pagina)
        self.assertEqual(resultado.ficha("monitoreo").huecos["total"], FACTURACION[(2026, 9)])

    def test_un_recorte_de_una_persona_no_muestra_la_hoja(self):
        ficha = Ficha(
            hoja_id="el_que_se_aparta",
            estado="completa",
            motivo=None,
            pregunta="Qué grupo se aparta.",
            base="el corte",
            grafico="barras",
            huecos={
                "corte": "cliente",
                "importe_del_grupo": {"grupo": "ana@correo.com", "importe": 1},
                "importe_del_resto": 0,
                "neto": 1,
                "nivel_de_cada_grupo": {"ana@correo.com": 1},
                "resta_de_cada_grupo": {"ana@correo.com": 1},
            },
            pasos=(),
            comprobacion="1 + 0 = 1",
        )
        resultado = Resultado(
            archivo="personas.csv",
            grano="una persona",
            personas="El archivo trae personas. La corrida se detiene.",
            filas=1,
            total_pelado=1,
            limpieza=(),
            fichas=(ficha,),
            unidad="pesos",
        )
        pagina = escribir(resultado, revisar_vacia(), instruccion_loma(), "Personas", None)
        self.assertNotIn("ana@correo.com", pagina)
        self.assertNotIn('data-filtro="producto"', pagina)


def revisar_vacia():
    from informe.nota import NotaLista

    return NotaLista(("primera oración",), "Primera oración\nSin hoja.\n")


if __name__ == "__main__":
    unittest.main()
