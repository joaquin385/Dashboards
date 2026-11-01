"""Cierra la fase 4: la nota de Loma se lee en la pirámide y cada peso tiene su hoja."""

import unittest
from dataclasses import replace

from caso.archivos import PESOS
from caso.corrida import encargo_copia, encargo_loma, instruccion_copia, instruccion_loma, marcas_loma
from caso.nota_loma import escribir_copia, escribir_loma
from caso.suciedad import SUCIO, escribir, filas_sucias
from informe.nota import Cierre, revisar
from pipeline.correr import correr


class NotaDeLoma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        escribir()
        cls.encargo = encargo_loma(len(filas_sucias()))
        cls.resultado = correr(cls.encargo, SUCIO, instruccion_loma(), marcas_loma())
        cls.nota = revisar(escribir_loma(cls.resultado), cls.resultado, cls.encargo)
        cls.encargo_copia = encargo_copia(77)
        cls.copia = correr(cls.encargo_copia, PESOS, instruccion_copia())
        cls.nota_copia = revisar(escribir_copia(cls.copia), cls.copia, cls.encargo_copia)

    def test_la_piramide_y_los_dos_cierres(self):
        self.assertEqual(
            self.nota.orden,
            ("destinatario", "primera oración", "evidencia", "límite", "otra historia", "cierres"),
        )
        texto = self.nota.texto
        self.assertLess(texto.index("Destinatario"), texto.index("Primera oración"))
        self.assertLess(texto.index("Primera oración"), texto.index("Evidencia"))
        self.assertLess(texto.index("Evidencia"), texto.index("Límite"))
        self.assertLess(texto.index("Límite"), texto.index("Otra historia"))
        self.assertLess(texto.index("Otra historia"), texto.index("Cierres"))
        self.assertLess(texto.index("Descriptivo."), texto.index("Causal."))
        self.assertNotIn("Decisión.", texto)

    def test_cada_peso_sale_de_su_hoja(self):
        texto = self.nota.texto
        self.assertIn("878.000 abajo", texto)
        self.assertIn("78.000 arriba", texto)
        self.assertIn("572.000", texto)
        self.assertIn("1.450.000", texto)
        self.assertIn("494.000", texto)
        self.assertIn("58.000 arriba", texto)
        self.assertIn("936.000 abajo", texto)
        self.assertIn("en el mismo número", texto)
        self.assertIn("312.000", texto)
        self.assertIn("650.000", texto)
        self.assertIn("Maroma", texto)
        self.assertIn("1.000.000 abajo", texto)
        self.assertIn("122.000 arriba", texto)
        self.assertIn("Cordel", texto)
        self.assertIn("Monitoreo.", texto)
        self.assertIn("El que se aparta.", texto)
        self.assertIn("no separa la causa", texto.casefold())
        self.assertIn("no alcanza para firmar", texto)

    def test_una_decision_que_nadie_nombro_no_entra(self):
        nota = escribir_loma(self.resultado)
        de_mas = replace(
            nota,
            cierres=nota.cierres + (Cierre("decision", "Hay que dejar Maroma."),),
        )
        with self.assertRaises(ValueError):
            revisar(de_mas, self.resultado, self.encargo)

    def test_un_numero_de_una_hoja_vacia_no_entra(self):
        nota = escribir_copia(self.copia)
        evidencia = nota.evidencia + (("lo_que_queda", "Queda {lo_que_queda|queda}."),)
        with self.assertRaises(ValueError):
            revisar(replace(nota, evidencia=evidencia), self.copia, self.encargo_copia)

    def test_la_copia_nombra_el_costo_que_falta(self):
        texto = self.nota_copia.texto
        self.assertIn("falta el costo que aparece con la venta", texto)
        self.assertIn("decir lo que queda después de ese costo", texto)
        self.assertIn("260.000", texto)
        self.assertIn("725.000", texto)
        self.assertIn("78.000 arriba", texto)
        self.assertIn("Lo que queda no se completa", texto)
        self.assertNotIn("Decisión.", texto)


if __name__ == "__main__":
    unittest.main()
