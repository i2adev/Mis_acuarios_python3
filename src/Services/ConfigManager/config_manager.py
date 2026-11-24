"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/11/2026
Descripción:
    Gestiona la configuración de la aplicación mediante
    archivos JSON.
"""

import copy
import json
import sys
import os

from pathlib import Path

from Config.config_defaults import DEFAULT_CONFIG


class ConfigManager:
    """
    Gestiona la configuración general de Mis Acuarios.

    Los cambios se mantienen en memoria hasta ejecutar save().
    """

    def __init__(self, config_dir=None):
        """
        Inicializa el gestor de configuración.

        Args:
            config_dir (str | Path, optional):
                Directorio donde se encuentra config.json.
        """

        # Directorio de configuración
        if config_dir is None:
            if getattr(sys, "frozen", False):
                base_path = Path(sys.executable).resolve().parent
            else:
                base_path = Path(__file__).resolve().parents[2]

            self.config_dir = base_path / "Config"

        else:
            self.config_dir = Path(config_dir)

        # Archivo JSON
        self.config_file = self.config_dir / "config.json"

        # Configuración predeterminada
        self._defaults = copy.deepcopy(DEFAULT_CONFIG)

        # Configuración original cargada del archivo
        self._original = {}

        # Configuración de trabajo
        self._config = {}

        # Cargar configuración
        self.load()

    # ---------------------------------------------------------
    # CARGA DE CONFIGURACIÓN
    # ---------------------------------------------------------

    def load(self) -> bool:
        """
        Carga la configuración desde el archivo JSON.

        Si el archivo no existe, utiliza los valores
        predeterminados en memoria.

        Returns:
            bool: True si la carga se realiza correctamente.
        """

        if not self.config_file.exists():
            # Cargar valores predeterminados
            self._config = copy.deepcopy(self._defaults)

            # Crear archivo de configuración inicial
            self.save()

            # Establecer configuración original
            self._original = copy.deepcopy(self._config)

            return True

        try:
            with self.config_file.open(
                    "r",
                    encoding="utf-8"
            ) as file:

                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError(
                    "LA RAÍZ DEL ARCHIVO JSON DEBE SER UN OBJETO"
                )

            # Incorporar valores predeterminados ausentes
            config = self._merge_defaults(
                self._defaults,
                data
            )

            # Validar configuración
            self.validate(config)

            self._config = config
            self._original = copy.deepcopy(config)

            return True

        except (OSError, json.JSONDecodeError, ValueError, TypeError) as error:

            print(
                f"ERROR AL CARGAR LA CONFIGURACIÓN: {error}"
            )

            # Utilizar configuración predeterminada
            self._config = copy.deepcopy(self._defaults)
            self._original = copy.deepcopy(self._config)

            return False

    # ---------------------------------------------------------
    # FUSIÓN DE VALORES PREDETERMINADOS
    # ---------------------------------------------------------

    @staticmethod
    def _merge_defaults(defaults, data):
        """
        Completa los valores ausentes utilizando los valores
        predeterminados.

        Los valores existentes en el archivo tienen prioridad.
        """

        result = copy.deepcopy(defaults)

        for key, value in data.items():

            if (
                    key in result
                    and isinstance(result[key], dict)
                    and isinstance(value, dict)
            ):

                result[key] = ConfigManager._merge_defaults(
                    result[key],
                    value
                )

            elif key in result:

                result[key] = copy.deepcopy(value)

        return result

    # ---------------------------------------------------------
    # VALIDACIÓN
    # ---------------------------------------------------------

    def validate(self, config=None):
        """
        Comprueba la estructura y los tipos de los valores.

        Raises:
            ValueError: Si existe algún valor incompatible.
        """

        if config is None:
            config = self._config

        self._validate_structure(
            self._defaults,
            config
        )

        return True

    @staticmethod
    def _validate_structure(defaults, config, path=""):
        """
        Valida recursivamente los valores de configuración.
        """

        for key, default_value in defaults.items():

            current_path = f"{path}.{key}" if path else key

            if key not in config:
                raise ValueError(
                    f"FALTA LA CONFIGURACIÓN: {current_path}"
                )

            value = config[key]

            if isinstance(default_value, dict):

                if not isinstance(value, dict):
                    raise ValueError(
                        f"{current_path} DEBE SER UN DICCIONARIO."
                    )

                ConfigManager._validate_structure(
                    default_value,
                    value,
                    current_path
                )

            elif default_value is not None:

                # bool debe comprobarse antes que int
                if isinstance(default_value, bool):
                    valid = isinstance(value, bool)

                elif isinstance(default_value, int):
                    valid = (
                            isinstance(value, int)
                            and not isinstance(value, bool)
                    )

                else:
                    valid = isinstance(value, type(default_value))

                if not valid:
                    raise ValueError(
                        f"TIPO INCORRECTO EN {current_path}. "
                        f"SE ESPERABA {type(default_value).__name__}."
                    )

            elif value is not None and (
                    not isinstance(value, int)
                    or isinstance(value, bool)
            ):
                raise ValueError(
                    f"{current_path} DEBE SER ENTERO O 'None'."
                )

    # ---------------------------------------------------------
    # CONSULTA DE CONFIGURACIÓN
    # ---------------------------------------------------------

    def get_value(self, section, key, default=None):
        """
        Obtiene un valor de una sección.

        Args:
            section (str): Nombre de la sección.
            key (str): Nombre del parámetro.
            default: Valor alternativo si no existe.

        Returns:
            El valor solicitado.
        """

        return self._config.get(
            section, {}
        ).get(key, default)

    def get_section(self, section):
        """
        Obtiene una sección completa de configuración.
        """

        return copy.deepcopy(
            self._config.get(section, {})
        )

    def get_all(self):
        """
        Devuelve una copia completa de la configuración.
        """

        return copy.deepcopy(self._config)

    # ---------------------------------------------------------
    # MODIFICACIÓN DE CONFIGURACIÓN
    # ---------------------------------------------------------
    def set_value(self, section, key, value):
        """
        Modifica un parámetro en memoria.

        No escribe en el archivo JSON.
        """

        if section not in self._defaults:
            raise KeyError(
                f"SECCIÓN DESCONOCIDA: {section}"
            )

        if key not in self._defaults[section]:
            raise KeyError(
                f"PARÁMETRO DESCONOCIDO: {section}.{key}"
            )

        # Crear una copia temporal
        new_config = copy.deepcopy(self._config)

        new_config[section][key] = value

        # Validar antes de aplicar el cambio
        self.validate(new_config)

        self._config = new_config

    def set_section(self, section, values):
        """
        Sustituye los valores de una sección en memoria.
        """

        if section not in self._defaults:
            raise KeyError(
                f"SECCIÓN DESCONOCIDA: {section}"
            )

        if not isinstance(values, dict):
            raise TypeError(
                "LA SECCIÓN DEBE SER UN DICCIONARIO."
            )

        new_config = copy.deepcopy(self._config)
        new_config[section] = copy.deepcopy(values)

        self.validate(new_config)

        self._config = new_config

    # ---------------------------------------------------------
    # DETECCIÓN DE CAMBIOS
    # ---------------------------------------------------------

    def has_changes(self):
        """
        Comprueba si existen cambios pendientes de guardar.
        """

        return self._config != self._original

    # ---------------------------------------------------------
    # GUARDADO
    # ---------------------------------------------------------

    def save(self):
        """
        Guarda la configuración en el archivo JSON.

        Utiliza un archivo temporal para evitar que un error
        durante la escritura destruya el archivo anterior.

        Returns:
            bool: True si se guarda correctamente.
        """

        try:

            self.validate()

            # Crear directorio si no existe
            self.config_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            # Archivo temporal
            temp_file = self.config_file.with_suffix(
                ".tmp"
            )

            with temp_file.open(
                    "w",
                    encoding="utf-8"
            ) as file:

                json.dump(
                    self._config,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

                file.write("\n")

                file.flush()

                os.fsync(file.fileno())

            # Sustituir archivo original
            temp_file.replace(self.config_file)

            # Actualizar configuración original
            self._original = copy.deepcopy(
                self._config
            )

            return True

        except (OSError, ValueError, TypeError) as error:

            print(
                f"ERROR AL GUARDAR LA CONFIGURACIÓN: {error}"
            )

            return False

    # ---------------------------------------------------------
    # RECARGAR CONFIGURACIÓN
    # ---------------------------------------------------------

    def reload(self):
        """
        Descarta los cambios pendientes y vuelve a cargar
        la configuración almacenada en el archivo.
        """

        return self.load()

    # ---------------------------------------------------------
    # RESTAURAR VALORES PREDETERMINADOS
    # ---------------------------------------------------------
    def reset(self):
        """
        Restablece la configuración a los valores predeterminados.

        Los cambios permanecen en memoria hasta que se guarden.
        """

        self._config = copy.deepcopy(self._defaults)
