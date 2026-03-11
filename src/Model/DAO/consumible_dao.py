"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      04/03/2026
Comentarios:
    DAO para la entidad FormatoCunsumibleEntity.
"""

import sqlite3
import traceback

from Model.DAO.base_dao import BaseDAO
from Model.Entities.consumible_entity import ConsumibleEntity
from Model.database import DBManager
from Services.Result.result import Result


class ConsumibleDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
CunsumibleEntity.
    """

    def __init__(self) -> None:
        """Constructor de clase."""

        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """ Obtiene el listado completo ordenado por categoría. """

        sql = (
            """
            SELECT C.ID_CONSUMIBLE AS ID,
                   ROW_NUMBER() OVER(ORDER BY M.MARCA, C.PRODUCTO, 
                                     C.CONTENIDO, C.DESCRIPCION) AS NUM,
                   M.MARCA AS MARCA,
                   C.PRODUCTO AS PRODUCTO,
                   T.CATEGORIA_CONSUMIBLE AS CATEGORIA,
                   F.FORMATO AS FORMATO,
                   C.CONTENIDO AS CONTENIDO,
                   U.UNIDAD AS UNIDAD,
                   C.DESCRIPCION AS DESCRIPCION
            FROM   CONSUMIBLES AS C
            LEFT JOIN MARCAS_COMERCIALES AS M
                ON    C.ID_MARCA = M.ID_MARCA
            LEFT JOIN CATEGORIAS_CONSUMIBLE AS T
                ON    C.ID_CATEGORIA = T.ID_CATEGORIA
            LEFT JOIN FORMATOS_CONSUMIBLE AS F
                ON    C.ID_FORMATO_CONSUMIBLE = F.ID_FORMATO_CONSUMIBLE
            LEFT JOIN UNIDADES_CONTENIDO AS U
                ON    C.ID_UNIDAD_CONTENIDO = U.ID_UNIDAD_CONTENIDO
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    ConsumibleEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_marca=f["MARCA"],
                        producto=f["PRODUCTO"],
                        id_categoria=f["CATEGORIA"],
                        id_formato=f["FORMATO"],
                        contenido=f["CONTENIDO"],
                        id_unidad=f["UNIDAD"],
                        descripcion=f["DESCRIPCION"],
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def get_num_by_id(self, id_: int) -> Result:
        """
        Obtiene el valor NÚM. de la vista VISTA_FORMATOS_CONSUMIBLE dado
        un ID.
        """
        sql = (
            """
            SELECT NUM
            FROM   VISTA_CONSUMIBLE
            WHERE  ID_CONSUMIBLE = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                if row is not None:
                    return Result.success(row["NUM"])
                return Result.failure(
                    f"NO SE ENCONTRÓ NINGÚN RESULTADO CON EL ID '{id_}'.")

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        """

        sql = (
            """
            SELECT C.ID_CONSUMIBLE AS ID,
                   M.MARCA || ' ' || C.PRODUCTO || ' (' 
                   || C.CONTENIDO || ' ' || U.UNIDAD || ')' AS VALUE
            FROM   CONSUMIBLES AS C
            LEFT JOIN MARCAS_COMERCIALES AS M
                ON    C.ID_MARCA = M.ID_MARCA
            LEFT JOIN UNIDADES_CONTENIDO AS U
                ON    C.ID_UNIDAD_CONTENIDO = U.ID_UNIDAD_CONTENIDO
            ORDER BY  VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    ConsumibleEntity(
                        id=f["ID"],
                        descripcion=f["VALUE"],
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def insert(self, ent: ConsumibleEntity) -> Result:
        """Inserta un nuevo registro y devuelve el ID generado."""

        sql = (
            """
            INSERT INTO CONSUMIBLES (ID_MARCA, PRODUCTO, ID_CATEGORIA, 
                                    ID_FORMATO_CONSUMIBLE, CONTENIDO, 
                                    ID_UNIDAD_CONTENIDO, DESCRIPCION)
            VALUES (:marca, :producto, :categoria, :formato, :contenido, 
                    :unidad, :descripcion);
            """
        )
        params = {"marca": ent.id_marca,
                  "producto": ent.producto,
                  "categoria": ent.id_categoria,
                  "formato": ent.id_formato,
                  "contenido": ent.contenido,
                  "unidad": ent.id_unidad,
                  "descripcion": ent.descripcion}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(cur.lastrowid)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def update(self, ent: ConsumibleEntity) -> Result:
        """Actualiza un registro. Devuelve el ID de la entidad modificada."""

        sql = (
            """
            UPDATE  CONSUMIBLES
            SET     ID_MARCA = :marca,
                    PRODUCTO = :producto,
                    ID_CATEGORIA = :categoria,
                    ID_FORMATO_CONSUMIBLE = :formato,
                    CONTENIDO = :contenido,
                    ID_UNIDAD_CONTENIDO = :unidad,
                    DESCRIPCION = :descripcion
             WHERE  ID_CONSUMIBLE = :id;
            """
        )
        params = {"id": ent.id,
                  "marca": ent.id_marca,
                  "producto": ent.producto,
                  "categoria": ent.id_categoria,
                  "formato": ent.id_formato,
                  "contenido": ent.contenido,
                  "unidad": ent.id_unidad,
                  "descripcion": ent.descripcion}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(ent.id)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM CONSUMIBLES
            WHERE       ID_CONSUMIBLE = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(id_)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")
