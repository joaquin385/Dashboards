"""Cierra la fase 1: un archivo imaginado se puede recorrer en el contrato."""

import unittest

from contrato.encargo import Encargo
from contrato.evaluar import evaluar
from contrato.hojas import HOJAS


def ventas(paquete: str, hojas: tuple[str, ...], **cambios) -> Encargo:
    """El asistente ya miró un archivo de ventas y escribió este match."""

    datos = dict(
        columnas={
            "fecha": "fecha",
            "grupo": "producto",
            "unidades": "unidades",
            "precio": "precio",
            "costo": "costo",
            "comprobante": "ticket",
        },
        importe_sale_de_unidades_por_precio=True,
        fechas_cubren_el_anio_pasado=True,
        el_calendario_cambio=True,
        moneda="pesos",
        pais="Argentina",
        pais_publica_indice=True,
        fuente_indice=None,
        mes_del_indice=None,
        corte_elegido="producto",
        hay_personas=False,
        grano="una venta",
        grano_coincide=True,
        decision=None,
        paquete=paquete,
        hojas_pedidas=hojas,
        filas=800,
    )
    datos.update(cambios)
    return Encargo(**datos)


HOJAS_DE_VENTAS = (
    "monitoreo",
    "anio_pasado",
    "piezas",
    "lo_que_queda",
    "calendario",
    "el_que_se_aparta",
)


class Contrato(unittest.TestCase):
    def test_cada_hoja_tiene_cuenta_grafico_limite_y_prohibicion(self):
        for hoja in HOJAS:
            self.assertTrue(hoja.cuenta)
            self.assertTrue(hoja.grafico.base_escrita)
            self.assertEqual(hoja.grafico.eje, "arranca en cero")
            self.assertTrue(hoja.limite_obligatorio)
            self.assertTrue(hoja.oraciones_prohibidas)
            self.assertTrue(any(hueco.lo_llena == "asistente" for hueco in hoja.huecos))

    def test_premium_de_ventas_completa_seis_y_deja_los_pesos_afuera(self):
        recorrido = evaluar(ventas("premium", HOJAS_DE_VENTAS))
        self.assertIsNone(recorrido.detenido)
        self.assertEqual(
            [hoja.id for hoja in recorrido.se_completan],
            list(HOJAS_DE_VENTAS),
        )
        self.assertEqual(recorrido.se_anuncian_vacias, ())
        self.assertIn("no alcanza a firmar", recorrido.nota.primera_oracion)
        self.assertEqual(recorrido.nota.profundidad, "piramide_con_otra_historia")

    def test_pesos_con_unidades_se_anuncia_vacia(self):
        hojas = (
            "monitoreo",
            "anio_pasado",
            "lo_que_queda",
            "calendario",
            "el_que_se_aparta",
            "pesos_de_un_mes",
        )
        recorrido = evaluar(ventas("premium", hojas))
        self.assertEqual(
            [hoja.id for hoja in recorrido.se_completan],
            ["monitoreo", "anio_pasado", "lo_que_queda", "calendario", "el_que_se_aparta"],
        )
        self.assertEqual(len(recorrido.se_anuncian_vacias), 1)
        vacia = recorrido.se_anuncian_vacias[0]
        self.assertEqual(vacia.hoja.id, "pesos_de_un_mes")
        self.assertIn("unidades", vacia.motivo)

    def test_pesos_sin_unidades_se_completa_si_la_fuente_esta_escrita(self):
        columnas = {"fecha": "fecha", "importe": "facturacion", "grupo": "local"}
        recorrido = evaluar(
            ventas(
                "premium",
                ("monitoreo", "pesos_de_un_mes"),
                columnas=columnas,
                importe_sale_de_unidades_por_precio=False,
                fuente_indice="INDEC, IPC",
                mes_del_indice="febrero 2026",
            )
        )
        self.assertEqual(
            [hoja.id for hoja in recorrido.se_completan],
            ["monitoreo", "pesos_de_un_mes"],
        )

    def test_basic_no_entrega_piezas(self):
        recorrido = evaluar(ventas("basic", ("monitoreo", "piezas")))
        self.assertEqual([hoja.id for hoja in recorrido.se_completan], ["monitoreo"])
        self.assertEqual(recorrido.fuera_del_paquete, ("piezas",))
        self.assertEqual(recorrido.nota.profundidad, "frase")

    def test_standard_no_elige_la_tercera_hoja(self):
        recorrido = evaluar(
            ventas("standard", ("monitoreo", "anio_pasado", "piezas", "lo_que_queda"))
        )
        self.assertIn("admite 2", recorrido.detenido)

    def test_sin_corte_la_hoja_del_grupo_queda_vacia(self):
        recorrido = evaluar(
            ventas("premium", ("monitoreo", "el_que_se_aparta"), corte_elegido=None)
        )
        self.assertEqual([hoja.id for hoja in recorrido.se_completan], ["monitoreo"])
        self.assertIn("antes de mirar", recorrido.se_anuncian_vacias[0].motivo)

    def test_personas_detienen_el_encargo(self):
        recorrido = evaluar(ventas("premium", HOJAS_DE_VENTAS, hay_personas=True))
        self.assertIn("personas", recorrido.detenido)
        self.assertEqual(recorrido.se_completan, ())
        self.assertIsNone(recorrido.nota)

    def test_embudo_es_otro_encargo(self):
        recorrido = evaluar(ventas("premium", ("monitoreo", "embudo")))
        self.assertEqual(recorrido.otro_encargo[0][0], "embudo")
        self.assertEqual([hoja.id for hoja in recorrido.se_completan], ["monitoreo"])

    def test_decision_nombrada_entra_en_la_primera_oracion(self):
        recorrido = evaluar(
            ventas(
                "standard",
                ("monitoreo", "piezas"),
                decision="No reponer solo por el neto del mes.",
            )
        )
        self.assertIn("No reponer solo por el neto del mes.", recorrido.nota.primera_oracion)
        self.assertIn(
            "Una decisión que el comprador no nombró.",
            recorrido.nota.oraciones_prohibidas,
        )

    def test_papel_inventado_no_entra_al_match(self):
        recorrido = evaluar(
            ventas("basic", ("monitoreo",), columnas={"cliente": "nombre", "importe": "total", "fecha": "fecha"})
        )
        self.assertIn("cliente", recorrido.detenido)


if __name__ == "__main__":
    recorrido = evaluar(ventas("premium", HOJAS_DE_VENTAS))
    print(recorrido.texto())
    print()
    unittest.main()
