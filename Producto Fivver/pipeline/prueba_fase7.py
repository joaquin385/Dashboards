"""Cierra la fase 7: un archivo que no es Loma, con el match escrito a mano.

Tres archivos. El primero trae las columnas de Loma con otros nombres, en pesos,
y la misma suciedad. Cae en las mismas hojas y en los mismos números. El antes
y el después de la limpieza no quedan en cero.

El segundo no trae el costo. Completa el resto y deja “lo que queda” vacía,
con la frase de que el margen no está. Una marca de esa hoja se anota y no
toca las filas. La marca de la hoja encendida sí mueve la suma.

El tercero trae nombre, teléfono, mail y un identificador. No produce HTML.

La mirada, sobre amount y total, pregunta. No elige total, aunque septiembre
pasa de 1.000 a 1 y amount se queda en 100.
"""

import csv
import tempfile
import unittest
from pathlib import Path

from caso.archivos import filas_ventas
from caso.corrida import instruccion_loma
from caso.cuenta import (
    FACTURACION,
    GRANO,
    HOJAS_DE_LOMA,
    MARCA_DE_CALENDARIO,
    NETO_CONTRA_AGOSTO,
    NETO_CONTRA_EL_ANIO_PASADO,
    NETO_QUEDA,
    PIEZA_CANTIDAD,
    PIEZA_MEZCLA,
    PIEZA_PRECIO,
    POR_PRODUCTO,
    QUEDA,
)
from caso.suciedad import TICKET_QUE_NO_SE_SUMA, filas_sucias
from contrato.encargo import Encargo
from dashboard.html import escribir
from informe.nota import NotaLista
from pipeline.correr import correr
from pipeline.instruccion import Marca
from pipeline.mirada import FRASE_DE_PERSONAS, mirar

_RENOMBRE = {
    "fecha": "day",
    "producto": "item",
    "unidades": "qty",
    "precio": "unit_price",
    "costo": "unit_cost",
    "importe": "amount",
    "ticket": "receipt",
    "nota": "comment",
}

_MATCH = {
    "fecha": "day",
    "grupo": "item",
    "unidades": "qty",
    "precio": "unit_price",
    "costo": "unit_cost",
    "comprobante": "receipt",
}


def _csv(camino: Path, filas: list[dict[str, str]]) -> None:
    with camino.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0]))
        escritor.writeheader()
        escritor.writerows(filas)


def _encargo(columnas: dict[str, str], filas: int, **cambios) -> Encargo:
    datos = dict(
        columnas=columnas,
        fechas_cubren_el_anio_pasado=True,
        el_calendario_cambio=True,
        moneda="pesos",
        pais="Argentina",
        pais_publica_indice=True,
        fuente_indice=None,
        mes_del_indice=None,
        corte_elegido="producto",
        hay_personas=False,
        grano=GRANO,
        grano_coincide=True,
        decision=None,
        paquete="premium",
        hojas_pedidas=HOJAS_DE_LOMA,
        filas=filas,
        importe_sale_de_unidades_por_precio=True,
    )
    datos.update(cambios)
    return Encargo(**datos)


def _mismos_pesos(caso: unittest.TestCase, resultado) -> None:
    monitoreo = resultado.ficha("monitoreo")
    caso.assertEqual(monitoreo.huecos["total"], FACTURACION[(2026, 9)])
    caso.assertEqual(monitoreo.huecos["total_base"], FACTURACION[(2026, 8)])
    caso.assertEqual(monitoreo.huecos["diferencia"], NETO_CONTRA_AGOSTO)
    caso.assertEqual(monitoreo.huecos["lo_que_mas_pesa"], {"grupo": "Cordel", "importe": 312_000})

    anio = resultado.ficha("anio_pasado")
    caso.assertEqual(anio.huecos["diferencia"], NETO_CONTRA_EL_ANIO_PASADO)

    piezas = resultado.ficha("piezas")
    caso.assertEqual(
        piezas.huecos["tramo_de_cada_pieza"],
        {"cantidad": PIEZA_CANTIDAD, "mezcla": PIEZA_MEZCLA, "precio": PIEZA_PRECIO},
    )

    calendario = resultado.ficha("calendario")
    caso.assertEqual(calendario.huecos["importe_en_dias_de_calendario"], MARCA_DE_CALENDARIO)

    aparta = resultado.ficha("el_que_se_aparta")
    caso.assertEqual(aparta.huecos["importe_del_grupo"], {"grupo": "Maroma", "importe": POR_PRODUCTO["Maroma"]})
    caso.assertEqual(resultado.total_pelado, sum(FACTURACION.values()))


class OtrosNombres(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filas = [{_RENOMBRE[clave]: valor for clave, valor in fila.items()} for fila in filas_sucias()]
        cls.temporal = tempfile.TemporaryDirectory()
        cls.archivo = Path(cls.temporal.name) / "otros-nombres.csv"
        _csv(cls.archivo, cls.filas)
        cls.encargo = _encargo(_MATCH, len(cls.filas))
        cls.resultado = correr(
            cls.encargo,
            cls.archivo,
            instruccion_loma(),
            (
                Marca(
                    "numero_con_punto_de_miles",
                    columnas=("unit_price", "unit_cost", "amount"),
                    detalle="El importe de una fila de Cordel está escrito con punto de miles.",
                ),
                Marca(
                    "comprobante_repetido",
                    detalle="La Maroma del 1 de agosto está dos veces, con el mismo ticket.",
                ),
                Marca(
                    "no_sumar",
                    tickets=(TICKET_QUE_NO_SE_SUMA,),
                    detalle="El total de Cordel de agosto ya está en las filas del mes.",
                ),
                Marca(
                    "esperar",
                    detalle="La fila en blanco no suma. La nota es mayúscula y comentario al margen.",
                ),
            ),
        )

    @classmethod
    def tearDownClass(cls):
        cls.temporal.cleanup()

    def test_la_mirada_no_escribe_el_match(self):
        mirada = mirar(list(self.filas[0]), self.filas)
        self.assertEqual(mirada.preguntas, ())
        self.assertEqual(mirada.personas, ())
        self.assertTrue(mirada.se_puede_correr)

    def test_cae_en_las_mismas_hojas_y_los_mismos_numeros(self):
        self.assertIsNone(self.resultado.detenido)
        self.assertEqual(
            tuple(ficha.hoja_id for ficha in self.resultado.fichas),
            HOJAS_DE_LOMA,
        )
        self.assertTrue(all(ficha.estado == "completa" for ficha in self.resultado.fichas))
        _mismos_pesos(self, self.resultado)
        queda = self.resultado.ficha("lo_que_queda")
        self.assertEqual(queda.huecos["queda"], QUEDA[(2026, 9)])
        self.assertEqual(queda.huecos["queda_base"], QUEDA[(2026, 8)])
        self.assertEqual(queda.huecos["queda"] - queda.huecos["queda_base"], NETO_QUEDA)

    def test_el_antes_y_el_despues_no_quedan_en_cero(self):
        anotaciones = self.resultado.limpieza
        self.assertEqual(anotaciones[0].antes, 2_744_000)
        self.assertEqual(anotaciones[0].despues, 2_756_000)
        self.assertEqual(anotaciones[1].despues, 2_716_000)
        self.assertEqual(anotaciones[2].despues, 2_516_000)
        self.assertEqual(anotaciones[3].antes, anotaciones[3].despues)
        for nota in anotaciones:
            self.assertNotEqual(nota.antes, 0)
            self.assertNotEqual(nota.despues, 0)


class SinCosto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        filas = []
        marcado = False
        for numero, origen in enumerate(filas_ventas(), start=1):
            precio = origen["precio"]
            ticket = f"T{numero:04d}"
            nota = ""
            if not marcado and origen["producto"] == "Cordel" and origen["fecha"].startswith("2026-09"):
                precio = "2.000"
                ticket = "T-MARGEN"
                nota = "REVISAR"
                marcado = True
            filas.append(
                {
                    "day": origen["fecha"],
                    "item": origen["producto"],
                    "qty": origen["unidades"],
                    "unit_price": precio,
                    "receipt": ticket,
                    "comment": nota,
                }
            )
        cls.temporal = tempfile.TemporaryDirectory()
        cls.archivo = Path(cls.temporal.name) / "sin-costo.csv"
        _csv(cls.archivo, filas)
        columnas = {papel: nombre for papel, nombre in _MATCH.items() if papel != "costo"}
        cls.resultado = correr(
            _encargo(columnas, len(filas)),
            cls.archivo,
            instruccion_loma(),
            (
                Marca(
                    "numero_con_punto_de_miles",
                    columnas=("unit_price",),
                    hoja="monitoreo",
                    detalle="Un precio de Cordel está escrito con punto de miles.",
                ),
                Marca(
                    "no_sumar",
                    tickets=("T-MARGEN",),
                    hoja="lo_que_queda",
                    detalle="Esa fila cambiaría lo que queda, y esa hoja no se encendió.",
                ),
                Marca(
                    "esperar",
                    detalle="La nota REVISAR no cambia la suma.",
                ),
            ),
        )

    @classmethod
    def tearDownClass(cls):
        cls.temporal.cleanup()

    def test_el_resto_se_completa_y_el_margen_no_esta(self):
        self.assertIsNone(self.resultado.detenido)
        completas = [ficha.hoja_id for ficha in self.resultado.fichas if ficha.estado == "completa"]
        self.assertEqual(
            completas,
            ["monitoreo", "anio_pasado", "piezas", "calendario", "el_que_se_aparta"],
        )
        _mismos_pesos(self, self.resultado)
        vacia = self.resultado.ficha("lo_que_queda")
        self.assertEqual(vacia.estado, "vacia")
        self.assertIn("El margen no está", vacia.motivo)
        self.assertEqual(vacia.huecos, {})

    def test_la_hoja_apagada_se_anota_sin_tocar(self):
        encendida, apagada, espera = self.resultado.limpieza
        self.assertEqual(encendida.accion, "numero_con_punto_de_miles")
        self.assertNotEqual(encendida.antes, 0)
        self.assertNotEqual(encendida.despues, 0)
        self.assertNotEqual(encendida.antes, encendida.despues)
        self.assertEqual(apagada.accion, "no_sumar")
        self.assertEqual(apagada.antes, apagada.despues)
        self.assertEqual(espera.antes, espera.despues)
        self.assertEqual(self.resultado.ficha("monitoreo").huecos["total"], FACTURACION[(2026, 9)])


class ConPersonas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filas = [
            {
                "day": "2026-09-01",
                "item": "Cuerda",
                "amount": "100",
                "nombre": "Ana Pérez",
                "telefono": "11-5555-0101",
                "mail": "ana@correo.com",
                "id_cliente": "C-19",
            },
            {
                "day": "2026-08-01",
                "item": "Cuerda",
                "amount": "80",
                "nombre": "Luis Gómez",
                "telefono": "11-5555-0102",
                "mail": "luis@correo.com",
                "id_cliente": "C-20",
            },
        ]
        cls.temporal = tempfile.TemporaryDirectory()
        cls.archivo = Path(cls.temporal.name) / "personas.csv"
        _csv(cls.archivo, cls.filas)
        cls.encargo = _encargo(
            {"fecha": "day", "grupo": "item", "importe": "amount"},
            len(cls.filas),
            importe_sale_de_unidades_por_precio=False,
            hojas_pedidas=("monitoreo",),
            corte_elegido=None,
            el_calendario_cambio=False,
            fechas_cubren_el_anio_pasado=False,
        )

    @classmethod
    def tearDownClass(cls):
        cls.temporal.cleanup()

    def test_la_mirada_pide_otro_corte(self):
        mirada = mirar(list(self.filas[0]), self.filas)
        self.assertEqual(mirada.personas, ("nombre", "telefono", "mail", "id_cliente"))
        self.assertEqual(mirada.preguntas, (FRASE_DE_PERSONAS,))
        self.assertFalse(mirada.se_puede_correr)

    def test_no_produce_html(self):
        resultado = correr(self.encargo, self.archivo, instruccion_loma())
        self.assertEqual(resultado.fichas, ())
        self.assertEqual(resultado.limpieza, ())
        self.assertEqual(resultado.detenido, FRASE_DE_PERSONAS)
        with self.assertRaises(ValueError) as fallo:
            escribir(resultado, NotaLista((), ""), instruccion_loma(), "Personas")
        self.assertEqual(str(fallo.exception), FRASE_DE_PERSONAS)

    def test_el_flag_no_abre_el_archivo(self):
        encargo = _encargo(
            {"fecha": "day", "importe": "amount"},
            1,
            hay_personas=True,
            hojas_pedidas=("monitoreo",),
        )
        resultado = correr(encargo, Path("archivo-que-no-existe.csv"), instruccion_loma())
        self.assertEqual(resultado.fichas, ())
        self.assertEqual(resultado.detenido, FRASE_DE_PERSONAS)


class PapelAmbiguo(unittest.TestCase):
    def test_pregunta_y_no_elige_la_columna_llamativa(self):
        nombres = ["day", "amount", "total"]
        filas = [
            {"day": "2026-08-01", "amount": "100", "total": "1000"},
            {"day": "2026-09-01", "amount": "100", "total": "1"},
        ]
        mirada = mirar(nombres, filas)
        self.assertEqual(
            mirada.preguntas,
            (
                "Hay más de una columna que puede ser el importe: amount, total. "
                "El asistente pregunta cuál es. "
                "No se elige la que deja el período más llamativo.",
            ),
        )
        self.assertNotIn("1000", mirada.preguntas[0])
        self.assertEqual(mirada.personas, ())
        self.assertTrue(mirada.se_puede_correr)


if __name__ == "__main__":
    unittest.main()
