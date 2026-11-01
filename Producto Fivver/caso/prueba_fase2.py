"""Cierra la fase 2: la cuenta escrita y el archivo dan el mismo número."""

import csv
import unittest
from datetime import date
from pathlib import Path

from caso.archivos import PESOS, VENTAS, dias_de_apertura, filas_pesos, filas_ventas
from caso.cuenta import (
    COSTO_DEL_MES,
    DIAS_DE_APERTURA,
    FACTURACION,
    FACTURACION_EN_PESOS_DE_SEPTIEMBRE_2025,
    FUENTE_INDICE,
    GRANO,
    HOJAS_DE_LA_COPIA,
    HOJAS_DE_LOMA,
    INDICE,
    MARCA_DE_CALENDARIO,
    MES_DEL_INDICE,
    NETO_CONTRA_AGOSTO,
    NETO_CONTRA_EL_ANIO_PASADO,
    NETO_QUEDA,
    PIEZA_CANTIDAD,
    PIEZA_MEZCLA,
    PIEZA_PRECIO,
    POR_PRODUCTO,
    QUEDA,
    QUEDA_POR_PRODUCTO,
)
from contrato.encargo import Encargo
from contrato.evaluar import evaluar
from contrato.hojas import HOJAS_POR_ID


def _leer(camino: Path) -> list[dict[str, str]]:
    with camino.open(encoding="utf-8", newline="") as archivo:
        return list(csv.DictReader(archivo))


def _facturacion(filas: list[dict[str, str]], anio: int, mes: int) -> int:
    total = 0
    for fila in filas:
        fecha = date.fromisoformat(fila["fecha"])
        if fecha.year == anio and fecha.month == mes:
            total += int(fila["unidades"]) * int(fila["precio"])
    return total


class CuentaDeLoma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filas = _leer(VENTAS)
        cls.pesos = _leer(PESOS)

    def test_el_archivo_es_el_que_arma_la_cuenta(self):
        self.assertEqual(self.filas, filas_ventas())
        self.assertEqual(self.pesos, filas_pesos())

    def test_los_dias_de_apertura_son_los_de_la_cuenta(self):
        for (anio, mes), cantidad in DIAS_DE_APERTURA.items():
            self.assertEqual(len(dias_de_apertura(anio, mes)), cantidad)

    def test_la_facturacion_de_cada_mes(self):
        for (anio, mes), total in FACTURACION.items():
            self.assertEqual(_facturacion(self.filas, anio, mes), total)

    def test_septiembre_de_2026_no_tiene_maroma(self):
        maroma = [
            fila
            for fila in self.filas
            if fila["producto"] == "Maroma" and fila["fecha"].startswith("2026-09")
        ]
        self.assertEqual(maroma, [])

    def test_el_neto_las_piezas_y_el_producto_cierran(self):
        neto = FACTURACION[(2026, 9)] - FACTURACION[(2026, 8)]
        self.assertEqual(neto, NETO_CONTRA_AGOSTO)
        self.assertEqual(PIEZA_CANTIDAD + PIEZA_MEZCLA + PIEZA_PRECIO, neto)
        self.assertEqual(sum(POR_PRODUCTO.values()), neto)

    def test_lo_que_queda_cierra(self):
        for mes, facturacion in FACTURACION.items():
            self.assertEqual(facturacion - COSTO_DEL_MES[mes], QUEDA[mes])
        neto = QUEDA[(2026, 9)] - QUEDA[(2026, 8)]
        self.assertEqual(neto, NETO_QUEDA)
        self.assertEqual(sum(QUEDA_POR_PRODUCTO.values()), neto)

    def test_el_anio_pasado_y_el_calendario(self):
        self.assertEqual(
            FACTURACION[(2026, 9)] - FACTURACION[(2025, 9)],
            NETO_CONTRA_EL_ANIO_PASADO,
        )
        self.assertEqual(FACTURACION[(2026, 8)] // DIAS_DE_APERTURA[(2026, 8)], MARCA_DE_CALENDARIO)

    def test_la_copia_tiene_el_mismo_importe_y_los_pesos_del_mes_elegido(self):
        for (anio, mes), total in FACTURACION.items():
            suma = 0
            for fila in self.pesos:
                fecha = date.fromisoformat(fila["fecha"])
                if fecha.year == anio and fecha.month == mes:
                    suma += int(fila["importe"])
            self.assertEqual(suma, total)
        for mes, corriente in FACTURACION.items():
            constante = corriente * INDICE[(2025, 9)] // INDICE[mes]
            self.assertEqual(constante, FACTURACION_EN_PESOS_DE_SEPTIEMBRE_2025[mes])

    def test_el_contrato_completa_las_seis_hojas_de_loma(self):
        recorrido = evaluar(_encargo_loma(len(self.filas)))
        self.assertIsNone(recorrido.detenido)
        self.assertEqual([hoja.id for hoja in recorrido.se_completan], list(HOJAS_DE_LOMA))
        self.assertEqual(recorrido.se_anuncian_vacias, ())

    def test_pesos_queda_vacia_porque_hay_unidades(self):
        motivo = HOJAS_POR_ID["pesos_de_un_mes"].motivo_si_no_enciende(_encargo_loma(205))
        self.assertIn("unidades", motivo)

    def test_la_copia_completa_pesos_y_anuncia_lo_que_no_tiene(self):
        recorrido = evaluar(_encargo_copia(len(self.pesos)))
        self.assertEqual([hoja.id for hoja in recorrido.se_completan], list(HOJAS_DE_LA_COPIA))
        self.assertEqual(recorrido.se_anuncian_vacias, ())
        vacias = {
            hoja_id: HOJAS_POR_ID[hoja_id].motivo_si_no_enciende(_encargo_copia(77))
            for hoja_id in ("piezas", "lo_que_queda", "el_que_se_aparta")
        }
        self.assertIn("unidades", vacias["piezas"])
        self.assertIn("costo", vacias["lo_que_queda"])
        self.assertIn("grupo", vacias["el_que_se_aparta"])


def _encargo_loma(filas: int) -> Encargo:
    return Encargo(
        columnas={
            "fecha": "fecha",
            "grupo": "producto",
            "unidades": "unidades",
            "precio": "precio",
            "costo": "costo",
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
        grano=GRANO,
        grano_coincide=True,
        decision=None,
        paquete="premium",
        hojas_pedidas=HOJAS_DE_LOMA,
        filas=filas,
    )


def _encargo_copia(filas: int) -> Encargo:
    return Encargo(
        columnas={"fecha": "fecha", "importe": "importe"},
        fechas_cubren_el_anio_pasado=True,
        el_calendario_cambio=True,
        moneda="pesos",
        pais="Argentina",
        pais_publica_indice=True,
        fuente_indice=FUENTE_INDICE,
        mes_del_indice=MES_DEL_INDICE,
        corte_elegido=None,
        hay_personas=False,
        grano="un día de apertura",
        grano_coincide=True,
        decision=None,
        paquete="premium",
        hojas_pedidas=HOJAS_DE_LA_COPIA,
        filas=filas,
    )


if __name__ == "__main__":
    unittest.main()
