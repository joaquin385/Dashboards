"""Cierra la fase 5: el HTML de Loma y el del archivo siguiente."""

import csv
import unittest
from pathlib import Path

from caso.archivos import filas_ventas
from caso.corrida import encargo_loma, instruccion_loma, marcas_loma
from caso.nota_loma import escribir_loma
from caso.suciedad import COLUMNAS, SUCIO, filas_sucias
from dashboard.html import escribir, grafico, guardar
from informe.nota import revisar
from pipeline.correr import correr

CARPETA = Path(__file__).resolve().parent.parent / "caso"
OTRO = CARPETA / "loma-otro.csv"
HTML = CARPETA / "loma.html"
HTML_OTRO = CARPETA / "loma-otro.html"


def _otro() -> None:
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
    with OTRO.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)
        escritor.writeheader()
        escritor.writerows(filas)


def _graficos(pagina: str) -> list[str]:
    return [
        linea.split('data-grafico="', 1)[1].split('"', 1)[0]
        for linea in pagina.splitlines()
        if 'data-grafico="' in linea
    ]


class DashboardDeLoma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _otro()
        cls.instruccion = instruccion_loma()
        cls.encargo = encargo_loma(len(filas_sucias()))
        cls.resultado = correr(
            cls.encargo,
            SUCIO,
            cls.instruccion,
            marcas_loma(),
        )
        cls.nota = revisar(escribir_loma(cls.resultado), cls.resultado, cls.encargo)
        cls.pagina = escribir(cls.resultado, cls.nota, cls.instruccion, "Loma", cls.encargo)
        guardar(HTML, cls.pagina)
        cls.otro = correr(encargo_loma(205), OTRO, cls.instruccion, marcas_loma())
        cls.nota_otro = revisar(escribir_loma(cls.otro), cls.otro, encargo_loma(205))
        cls.pagina_otro = escribir(cls.otro, cls.nota_otro, cls.instruccion, "Loma", encargo_loma(205))
        guardar(HTML_OTRO, cls.pagina_otro)

    def test_tres_graficos_en_una_hoja(self):
        self.assertEqual(_graficos(self.pagina), ["evolucion", "piezas", "atributo"])
        self.assertIn("572.000", self.pagina)
        self.assertIn("1.450.000", self.pagina)
        self.assertIn("El eje arranca en cero.", self.pagina)
        self.assertNotIn("http", self.pagina)
        self.assertIn('data-diferencia="-878000"', self.pagina)

    def test_el_otro_archivo_mueve_los_numeros_y_deja_la_estructura(self):
        self.assertEqual(_graficos(self.pagina), _graficos(self.pagina_otro))
        self.assertIn('data-diferencia="-1756000"', self.pagina_otro)
        self.assertNotIn('data-diferencia="-878000"', self.pagina_otro)
        self.assertIn("2.900.000", self.pagina_otro)
        self.assertIn("1.144.000", self.pagina_otro)
        with OTRO.open(encoding="utf-8", newline="") as archivo:
            self.assertEqual(list(csv.DictReader(archivo).fieldnames), COLUMNAS)

    def test_un_eje_recortado_dice_que_quedo_debajo(self):
        dibujo = grafico([("Agosto", 100)], debajo_del_corte="lo que está bajo el corte")
        self.assertIn("Debajo del corte quedó lo que está bajo el corte.", dibujo)
        self.assertIn('data-eje="cero"', dibujo)


if __name__ == "__main__":
    unittest.main()
