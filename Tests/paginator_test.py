"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/06/2025
Commentarios:
    Tests de la clase paginator.
"""
from Model.DAO.paginator import Paginator


def test_configuracion():
    """ Primer test para saber que se ha configurado correctamente. """
    pag = Paginator("VISTA_TIPOS_FILTRO", 5)
    pag.initialize_paginator()

    print(pag)

def test_configuracion_last_page():
    """ Primer test para saber que se ha configurado la última página. """
    pag = Paginator("VISTA_TIPOS_FILTRO", 5)
    pag.initialize_paginator(False)

    print(pag)


if __name__ == "__main__":
    print("ORUEBA DE LA CLASE PAGINATOR.")
    print("-----------------------------")
    print(" Primera página")
    print(" ----------------------------")
    test_configuracion()
    print(" Última página")
    print(" ----------------------------")
    test_configuracion_last_page()