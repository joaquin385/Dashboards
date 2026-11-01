"""Cierra la fase 6: Loma sigue exacto, y un Excel en dólares da la cuenta de al lado.

Muelle, en centavos de dólar. La cuenta está hecha antes de correr.

Agosto de 2026, Cuerda: 1 unidad a 4,00 el 3 de agosto y 2 unidades a 5,00
el 4. Son 14,00 dólares, 1.400 centavos, con dos precios en el mes. El precio
de la base es 1.400 / 3 = 466,666…, que redondea a 467 centavos.

Septiembre de 2026: 2 unidades a 6,00 el 1 de septiembre. Son 12,00 dólares,
1.200 centavos.

El neto es 200 centavos abajo. La cantidad, redondeada, se lleva 467 abajo.
La mezcla, por ese redondeo, se lleva 1 arriba. El precio se lleva 266 arriba.
467 abajo, más 1, más 266, es 200 abajo.

El calendario es lunes a sábado, domingo cerrado, y el 17 de agosto feriado.
Agosto tiene 25 días de apertura y septiembre 26. 1.400 / 25 es 56, exacto.
La marca es un día, 56 centavos. De esos 25, dos tienen filas: quedan 23 sin
venta. En septiembre, 25.

Las fechas del archivo están como las exporta Excel en Estados Unidos:
08/03/2026 es el 3 de agosto, no el 8 de marzo. La primera solapa del libro,
portada, trae 999.999,00 y no entra en la cuenta.
"""

import csv
import tempfile
import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path

from caso.corrida import encargo_loma, instruccion_loma, marcas_loma
from caso.suciedad import SUCIO, escribir, filas_sucias
from contrato.encargo import Encargo
from informe.nota import Cierre, Nota, revisar
from pipeline.correr import correr
from pipeline.excel import escribir as escribir_excel
from pipeline.instruccion import Calendario, Instruccion, Marca, Periodo, ReglaMedicion

_CAMINO = ("cantidad", "mezcla", "precio")
_COLUMNAS = ["date", "product", "units", "price", "amount"]
_REDONDEO = "La cuenta está redondeada a la unidad."


def _encargo_muelle(solapa: str) -> Encargo:
    return Encargo(
        columnas={
            "fecha": "date",
            "grupo": "product",
            "unidades": "units",
            "precio": "price",
            "importe": "amount",
        },
        fechas_cubren_el_anio_pasado=False,
        el_calendario_cambio=True,
        moneda="dólares",
        pais="Estados Unidos",
        pais_publica_indice=False,
        fuente_indice=None,
        mes_del_indice=None,
        corte_elegido=None,
        hay_personas=False,
        grano="un producto en un día",
        grano_coincide=True,
        decision=None,
        paquete="premium",
        hojas_pedidas=("monitoreo", "piezas", "calendario"),
        filas=3,
        separador_decimal=".",
        separador_miles=",",
        formato_fecha="%m/%d/%Y",
        decimales=2,
        idioma="es",
        unidad_del_papel={"importe": "centavo de dólar", "precio": "centavo de dólar"},
        hoja_del_archivo=solapa,
    )


def _instruccion_muelle() -> Instruccion:
    return Instruccion(
        periodo=Periodo.mes(2026, 9),
        periodo_anterior=Periodo.mes(2026, 8),
        anio_pasado=Periodo.mes(2025, 9),
        camino=_CAMINO,
        que_dia="17 de agosto de 2026, feriado, sin fila en este archivo",
        costo_es_por_unidad=False,
        calendario=Calendario(
            abre=(0, 1, 2, 3, 4, 5),
            feriados=(date(2026, 8, 17),),
            texto=(
                "Día de apertura es lunes a sábado. El domingo cierra. "
                "El feriado del 17 de agosto de 2026 sacó un lunes."
            ),
        ),
    )


def _filas_muelle() -> list[dict[str, str]]:
    return [
        {"date": "08/03/2026", "product": "Cuerda", "units": "1", "price": "4.00", "amount": "4.00"},
        {"date": "08/04/2026", "product": "Cuerda", "units": "2", "price": "5.00", "amount": "10.00"},
        {"date": "09/01/2026", "product": "Cuerda", "units": "2", "price": "6.00", "amount": "12.00"},
    ]


def _encargo_basico(**cambios) -> Encargo:
    datos = dict(
        columnas={"fecha": "fecha", "importe": "importe"},
        fechas_cubren_el_anio_pasado=False,
        el_calendario_cambio=False,
        moneda="pesos",
        pais="Argentina",
        pais_publica_indice=False,
        fuente_indice=None,
        mes_del_indice=None,
        corte_elegido=None,
        hay_personas=False,
        grano="una fila",
        grano_coincide=True,
        decision=None,
        paquete="basic",
        hojas_pedidas=("monitoreo",),
        filas=4,
    )
    datos.update(cambios)
    return Encargo(**datos)


def _instruccion(**cambios) -> Instruccion:
    datos = dict(
        periodo=Periodo.mes(2026, 9),
        periodo_anterior=Periodo.mes(2026, 8),
        anio_pasado=Periodo.mes(2025, 9),
        camino=_CAMINO,
        que_dia="",
        costo_es_por_unidad=False,
    )
    datos.update(cambios)
    return Instruccion(**datos)


def _csv(camino: Path, columnas: list[str], filas: list[dict[str, str]]) -> None:
    with camino.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(filas)


class ExcelEnDolares(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporal = tempfile.TemporaryDirectory()
        cls.libro = Path(cls.temporal.name) / "muelle.xlsx"
        escribir_excel(
            cls.libro,
            {
                "portada": (_COLUMNAS, [
                    {
                        "date": "08/03/2026",
                        "product": "Otro",
                        "units": "1",
                        "price": "1.00",
                        "amount": "999999.00",
                    }
                ]),
                "ventas": (_COLUMNAS, _filas_muelle()),
            },
        )
        cls.instruccion = _instruccion_muelle()
        cls.encargo = _encargo_muelle("ventas")
        cls.resultado = correr(
            cls.encargo,
            cls.libro,
            cls.instruccion,
            (Marca("esperar", detalle="El archivo ya viene en números."),),
        )

    @classmethod
    def tearDownClass(cls):
        cls.temporal.cleanup()

    def test_la_cuenta_en_centavos_y_el_redondeo(self):
        self.assertEqual(self.resultado.unidad, "centavo de dólar")
        self.assertEqual(self.resultado.total_pelado, 2_600)
        self.assertEqual(self.resultado.limpieza[0].antes, 2_600)
        self.assertEqual(self.resultado.limpieza[0].despues, 2_600)
        monitoreo = self.resultado.ficha("monitoreo")
        self.assertEqual(monitoreo.huecos["total_base"], 1_400)
        self.assertEqual(monitoreo.huecos["total"], 1_200)
        self.assertEqual(monitoreo.huecos["diferencia"], -200)
        piezas = self.resultado.ficha("piezas")
        self.assertEqual(piezas.huecos["neto"], -200)
        self.assertEqual(
            piezas.huecos["tramo_de_cada_pieza"],
            {"cantidad": -467, "mezcla": 1, "precio": 266},
        )
        self.assertEqual(piezas.huecos["redondeado"], _REDONDEO)
        self.assertEqual(
            piezas.huecos["definicion_precio"],
            "El precio de la base es el importe del grupo dividido sus unidades.",
        )

    def test_el_calendario_lo_declara_el_asistente(self):
        calendario = self.resultado.ficha("calendario")
        self.assertEqual(calendario.huecos["dias_de_apertura_base"], 25)
        self.assertEqual(calendario.huecos["dias_de_apertura"], 26)
        self.assertEqual(calendario.huecos["dias_sin_filas_base"], 23)
        self.assertEqual(calendario.huecos["dias_sin_filas"], 25)
        self.assertEqual(calendario.huecos["importe_en_dias_de_calendario"], 56)
        self.assertNotIn("redondeado", calendario.huecos)

    def test_la_hoja_nombrada_no_es_la_primera(self):
        portada = correr(
            _encargo_muelle("portada"),
            self.libro,
            self.instruccion,
        )
        self.assertEqual(portada.total_pelado, 99_999_900)
        self.assertNotEqual(portada.total_pelado, self.resultado.total_pelado)


class PeriodoYMedicion(unittest.TestCase):
    def test_la_semana_y_el_trimestre_no_suponen_el_mes(self):
        with tempfile.TemporaryDirectory() as carpeta:
            archivo = Path(carpeta) / "semanas.csv"
            _csv(
                archivo,
                ["fecha", "importe"],
                [
                    {"fecha": "2026-09-07", "importe": "10"},
                    {"fecha": "2026-09-08", "importe": "10"},
                    {"fecha": "2026-09-09", "importe": "10"},
                    {"fecha": "2026-09-14", "importe": "100"},
                    {"fecha": "2026-02-01", "importe": "5"},
                    {"fecha": "2026-04-01", "importe": "9"},
                ],
            )
            semana = correr(
                _encargo_basico(),
                archivo,
                _instruccion(
                    periodo=Periodo.entre("semana", date(2026, 9, 7), date(2026, 9, 13)),
                    periodo_anterior=Periodo.entre("semana", date(2026, 8, 31), date(2026, 9, 6)),
                    anio_pasado=Periodo.entre("semana", date(2025, 9, 8), date(2025, 9, 14)),
                ),
            )
            self.assertEqual(semana.ficha("monitoreo").huecos["total"], 30)
            trimestre = correr(
                _encargo_basico(),
                archivo,
                _instruccion(
                    periodo=Periodo.trimestre(2026, 1),
                    periodo_anterior=Periodo.trimestre(2025, 4),
                    anio_pasado=Periodo.trimestre(2025, 1),
                ),
            )
            self.assertEqual(trimestre.ficha("monitoreo").huecos["total"], 5)

    def test_las_tres_bases_comparten_el_grano(self):
        with self.assertRaises(ValueError):
            correr(
                _encargo_basico(),
                Path("no-hace-falta.csv"),
                _instruccion(
                    periodo_anterior=Periodo.entre("semana", date(2026, 8, 1), date(2026, 8, 7)),
                ),
            )

    def test_la_regla_resta_la_devolucion_y_deja_el_impuesto_afuera(self):
        with tempfile.TemporaryDirectory() as carpeta:
            archivo = Path(carpeta) / "caja.csv"
            _csv(
                archivo,
                ["fecha", "importe", "devolucion", "impuesto"],
                [
                    {"fecha": "2026-08-01", "importe": "80", "devolucion": "0", "impuesto": "0"},
                    {"fecha": "2026-09-01", "importe": "100", "devolucion": "40", "impuesto": "21"},
                ],
            )
            encargo = _encargo_basico(
                columnas={
                    "fecha": "fecha",
                    "importe": "importe",
                    "devolucion": "devolucion",
                    "impuesto": "impuesto",
                },
                filas=2,
            )
            salto = "En julio cambió la regla y agosto no se reescribió."
            neta = correr(
                encargo,
                archivo,
                _instruccion(
                    medicion=ReglaMedicion("neta", impuesto_afuera=True, salto=salto),
                ),
            )
            self.assertEqual(neta.ficha("monitoreo").huecos["total"], 60)
            self.assertEqual(neta.ficha("monitoreo").huecos["total_base"], 80)
            self.assertIn("venta neta", neta.ficha("monitoreo").huecos["regla_de_medicion"])
            self.assertIn("el impuesto queda afuera del precio", neta.ficha("monitoreo").huecos["regla_de_medicion"])
            self.assertEqual(neta.ficha("monitoreo").huecos["salto_de_regla"], salto)
            bruta = correr(
                encargo,
                archivo,
                _instruccion(medicion=ReglaMedicion("bruta", impuesto_afuera=True)),
            )
            self.assertEqual(bruta.ficha("monitoreo").huecos["total"], 100)
            with self.assertRaises(ValueError):
                correr(encargo, archivo, _instruccion())


class NotaEnIngles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        escribir()
        cls.encargo = replace(encargo_loma(len(filas_sucias())), idioma="en")
        cls.resultado = correr(cls.encargo, SUCIO, instruccion_loma(), marcas_loma())

    def test_la_piramide_en_ingles_pasa_y_la_que_decide_no(self):
        nota = revisar(_nota_inglesa(), self.resultado, self.encargo)
        self.assertIn("does not suffice to sign", nota.texto)
        self.assertIn("does not separate", nota.texto.casefold())
        self.assertLess(nota.texto.index("First sentence"), nota.texto.index("Evidence"))
        de_mas = replace(_nota_inglesa(), limite="We should drop it.")
        with self.assertRaises(ValueError):
            revisar(de_mas, self.resultado, self.encargo)
        sin_firma = replace(
            _nota_inglesa(),
            primera_oracion="September is {monitoreo|diferencia|resta} from August.",
            limite="The two bases are read together.",
        )
        with self.assertRaises(ValueError):
            revisar(sin_firma, self.resultado, self.encargo)
        sin_separar = replace(
            _nota_inglesa(),
            cierres=(
                Cierre("descriptivo", "September billed {monitoreo|total}."),
                Cierre("causal", "The table stays with the comparison."),
            ),
        )
        with self.assertRaises(ValueError):
            revisar(sin_separar, self.resultado, self.encargo)


def _nota_inglesa() -> Nota:
    return Nota(
        destinatario="Whoever could sign at Loma is not named. The note stays with the comparison.",
        primera_oracion=(
            "September 2026 is {monitoreo|diferencia|resta} from August "
            "and {anio_pasado|diferencia|resta} from September 2025. "
            "This file does not suffice to sign a purchase."
        ),
        evidencia=(
            ("monitoreo", "September billed {monitoreo|total} against {monitoreo|total_base}."),
            ("anio_pasado", "September 2025 billed {anio_pasado|total_base}."),
            ("piezas", "The path is {piezas|camino}. The net is {piezas|neto|resta}."),
            ("lo_que_queda", "September leaves {lo_que_queda|queda}."),
            ("calendario", "The mark is {calendario|importe_en_dias_de_calendario}."),
            (
                "el_que_se_aparta",
                "{el_que_se_aparta|importe_del_grupo|grupo} carries "
                "{el_que_se_aparta|importe_del_grupo|importe|resta}.",
            ),
        ),
        limite="The two bases are read together. A piece is not a cause.",
        otra_historia="The mix also fits these figures. The first sentence stays with the two bases.",
        cierres=(
            Cierre("descriptivo", "September billed {monitoreo|total} against {monitoreo|total_base}."),
            Cierre("causal", "The table does not separate the cause. It describes the month."),
        ),
    )


if __name__ == "__main__":
    unittest.main()
