import sqlite3
import traceback

def insert(self, ent: "UrnaEntity") -> "Result":
    """
    Inserta un nuevo registro en la tabla URNAS y devuelve el ID generado.
    :param ent: UrnaEntity
    """
    sql = """
        INSERT INTO URNAS 
            (ID_MARCA, MODELO, ANCHURA, PROFUNDIDAD, ALTURA, 
             GROSOR_CRISTAL, VOLUMEN_TANQUE, ID_MATERIAL, DESCRIPCION)
        VALUES 
            (:idm, :modelo, :anch, :prof, :alt, 
             :grosor, :vol, :mat, :obs);
    """

    params = {
        "idm":    ent.id_marca,  # FK -> MARCAS_COMERCIALES (si aplica)
        "modelo": ent.modelo,
        "anch":   ent.anchura,
        "prof":   ent.profundidad,
        "alt":    ent.altura,
        "grosor": ent.grosor_cristal,
        "vol":    ent.volumen_tanque,
        "mat":    ent.id_material,  # FK -> MATERIALES_URNA
        "obs":    ent.descripcion
    }

    try:
        # Usa el context manager del connection: COMMIT/ROLLBACK automático
        with self.db.conn as con:
            cur = con.execute(sql, params)
            last_id = cur.lastrowid
            return Result.success(last_id)

    except sqlite3.IntegrityError as e:
        # Violación de FK/UNIQUE/NOT NULL, etc.
        return Result.failure(f"[INTEGRITY ERROR] {e}")
    except sqlite3.OperationalError as e:
        # Tabla/columna inexistente, bloqueo, sintaxis, etc.
        traceback.print_exc()
        return Result.failure(f"[OPERATIONAL ERROR] {e}")
    except sqlite3.ProgrammingError as e:
        return Result.failure(f"[PROGRAMMING ERROR] {e}")
    except sqlite3.DatabaseError as e:
        return Result.failure(f"[DATABASE ERROR] {e}")
    except sqlite3.Error as e:
        return Result.failure(f"[SQLITE ERROR] {e}")
# Importante: no cierres aquí la conexión; deja que la gestione el ciclo de vida
# de la app.
