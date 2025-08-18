"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Commentarios:
    Tests de la clase UrnaTableModel.
"""
from Model.TableModel.urna_table_model import UrnaTableModel


def test_desglose_dimensiones(dimension: str):
    model = UrnaTableModel(None)
    model.brakdown_dimensions(dimension)

if __name__ == "__main__":
    print("PRUEBA DE LA CLASE ACUARIOTABLEMODEL.")
    print("-----------------------------")
    print(" Primera página")
    print(" ----------------------------")
    test_desglose_dimensiones("100x60x50 (cm)")