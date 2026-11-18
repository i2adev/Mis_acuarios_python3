"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  11/11/2026
Comentarios:
    DAO de la configuración.
"""
from Main.Model.DAO.base_dao import BaseDAO
from ModuloMaestro.Model.Entities.base_entity import BaseEntity
from Services.Result.result import Result


class ConfiguracionDAO(BaseDAO):
    def __init__(self):
        pass

    def delete(self, id: int) -> Result:
        pass

    def update(self, ent: BaseEntity) -> Result:
        pass

    def get_list_combo(self) -> Result:
        pass

    def insert(self, ent: BaseEntity) -> Result:
        pass

    def get_list(self) -> Result:
        pass
