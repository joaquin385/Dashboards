"""Cierra la fase 3: el pipeline y la cuenta de Loma dan el mismo número."""

import unittest

from caso.archivos import PESOS
from caso.corrida import encargo_copia, encargo_loma, instruccion_copia, instruccion_loma, marcas_loma
from caso.cuenta import (
    FACTURACION,
    FACTURACION_EN_PESOS_DE_SEPTIEMBRE_2025,
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
from caso.suciedad import SUCIO, escribir, filas_sucias
from pipeline.correr import correr
from pipeline.limpieza import total_leido


class PipelineDeLoma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        escribir()
        cls.resultado = correr(encargo_loma(len(filas_sucias())), SUCIO, instruccion_loma(), marcas_loma())
        cls.copia = correr(encargo_copia(77), PESOS, instruccion_copia())

    def test_la_limpieza_anota_el_antes_y_el_despues(self):
        self.assertIsNone(self.resultado.detenido)
        anotaciones = self.resultado.limpieza
        self.assertEqual([nota.accion for nota in anotaciones], [
            "numero_con_punto_de_miles",
            "comprobante_repetido",
            "no_sumar",
            "esperar",
        ])
        self.assertEqual(anotaciones[0].antes, 2_744_000)
        self.assertEqual(anotaciones[0].despues, 2_756_000)
        self.assertEqual(anotaciones[1].despues, 2_716_000)
        self.assertEqual(anotaciones[2].despues, 2_516_000)
        self.assertEqual(anotaciones[3].antes, anotaciones[3].despues)
        self.assertEqual(self.resultado.total_pelado, sum(FACTURACION.values()))
        self.assertEqual(total_leido(filas_sucias()), 2_744_000)

    def test_el_monitoreo_es_la_resta_y_no_el_total_pelado(self):
        ficha = self.resultado.ficha("monitoreo")
        self.assertEqual(ficha.huecos["total"], FACTURACION[(2026, 9)])
        self.assertEqual(ficha.huecos["total_base"], FACTURACION[(2026, 8)])
        self.assertEqual(ficha.huecos["diferencia"], NETO_CONTRA_AGOSTO)
        self.assertNotEqual(ficha.huecos["diferencia"], self.resultado.total_pelado)
        self.assertEqual(ficha.huecos["lo_que_mas_pesa"], {"grupo": "Cordel", "importe": 312_000})
        self.assertIsNone(ficha.huecos["limite"])
        self.assertIn("el período anterior", ficha.base)

    def test_las_hojas_encendidas_coinciden_con_la_cuenta(self):
        anio = self.resultado.ficha("anio_pasado")
        self.assertEqual(anio.huecos["diferencia"], NETO_CONTRA_EL_ANIO_PASADO)

        piezas = self.resultado.ficha("piezas")
        self.assertEqual(piezas.huecos["neto"], NETO_CONTRA_AGOSTO)
        self.assertEqual(
            piezas.huecos["tramo_de_cada_pieza"],
            {"cantidad": PIEZA_CANTIDAD, "mezcla": PIEZA_MEZCLA, "precio": PIEZA_PRECIO},
        )
        self.assertEqual(piezas.huecos["camino"], "cantidad, mezcla, precio")

        queda = self.resultado.ficha("lo_que_queda")
        self.assertEqual(queda.huecos["queda"], QUEDA[(2026, 9)])
        self.assertEqual(queda.huecos["queda_base"], QUEDA[(2026, 8)])
        self.assertEqual(queda.huecos["queda"] - queda.huecos["queda_base"], NETO_QUEDA)

        calendario = self.resultado.ficha("calendario")
        self.assertEqual(calendario.huecos["importe_en_dias_de_calendario"], MARCA_DE_CALENDARIO)
        self.assertEqual(calendario.huecos["importe_en_dias_comparables"], FACTURACION[(2026, 8)])
        self.assertIn("17 de agosto", calendario.huecos["que_dia"])
        self.assertNotIn("redondeado", calendario.huecos)
        self.assertEqual(calendario.huecos["dias_sin_filas"], 0)
        self.assertEqual(calendario.huecos["dias_sin_filas_base"], 0)
        self.assertNotIn("redondeado", piezas.huecos)

        aparta = self.resultado.ficha("el_que_se_aparta")
        self.assertEqual(aparta.huecos["corte"], "producto")
        self.assertEqual(
            aparta.huecos["importe_del_grupo"],
            {"grupo": "Maroma", "importe": POR_PRODUCTO["Maroma"]},
        )
        self.assertEqual(aparta.huecos["importe_del_resto"], POR_PRODUCTO["Cordel"] + POR_PRODUCTO["Soga"])

    def test_cada_ficha_guarda_la_pregunta_los_pasos_y_la_comprobacion(self):
        for ficha in self.resultado.fichas:
            self.assertEqual(ficha.estado, "completa")
            self.assertTrue(ficha.pregunta)
            self.assertTrue(ficha.pasos)
            self.assertTrue(ficha.comprobacion)
            self.assertTrue(ficha.grafico)
        self.assertEqual(self.resultado.grano, "un producto en un día de apertura")
        self.assertIn("No hay personas", self.resultado.personas)
        self.assertEqual(self.resultado.filas, 205)

    def test_la_hoja_sin_costo_se_anuncia_vacia(self):
        self.assertIsNone(self.copia.detenido)
        vacia = self.copia.ficha("lo_que_queda")
        self.assertEqual(vacia.estado, "vacia")
        self.assertIn("costo", vacia.motivo)
        self.assertEqual(vacia.huecos, {})
        pesos = self.copia.ficha("pesos_de_un_mes")
        self.assertEqual(pesos.huecos["constantes"]["2026-09"], FACTURACION_EN_PESOS_DE_SEPTIEMBRE_2025[(2026, 9)])
        self.assertEqual(pesos.huecos["constantes"]["2026-08"], FACTURACION_EN_PESOS_DE_SEPTIEMBRE_2025[(2026, 8)])
        self.assertEqual(pesos.huecos["mes"], "septiembre 2025")
        self.assertNotIn("redondeado", pesos.huecos)


if __name__ == "__main__":
    unittest.main()
