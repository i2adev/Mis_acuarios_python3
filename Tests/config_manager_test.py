"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/11/2026
Descripción:
    Pruebas unitarias de ConfigManager.
"""

import json
import pytest

from Services.ConfigManager.config_manager import ConfigManager


class TestConfigManager:
    """Pruebas unitarias para ConfigManager."""

    def test_load_default_config(self, tmp_path):
        """Comprueba que se carga la configuración por defecto."""

        config_manager = ConfigManager(config_dir=tmp_path)

        assert config_manager.get_value("unidades", "dimension") == "cm"
        assert config_manager.get_value("unidades", "volumen") == "L"
        assert config_manager.get_value("unidades", "temperatura") == "°C"

    def test_get_value(self, tmp_path):
        """Comprueba la lectura de un valor."""

        config_manager = ConfigManager(config_dir=tmp_path)

        assert config_manager.get_value("unidades", "dimension") == "cm"

    def test_get_value_default(self, tmp_path):
        """Comprueba el valor devuelto cuando la clave no existe."""

        config_manager = ConfigManager(config_dir=tmp_path)

        assert config_manager.get_value(
            "seccion_inexistente",
            "clave_inexistente",
            "valor_defecto"
        ) == "valor_defecto"

    def test_get_section(self, tmp_path):
        """Comprueba la lectura de una sección completa."""

        config_manager = ConfigManager(config_dir=tmp_path)

        unidades = config_manager.get_section("unidades")

        assert isinstance(unidades, dict)
        assert unidades["dimension"] == "cm"
        assert unidades["volumen"] == "L"

    def test_get_all(self, tmp_path):
        """Comprueba que se obtiene la configuración completa."""

        config_manager = ConfigManager(config_dir=tmp_path)

        config = config_manager.get_all()

        assert isinstance(config, dict)
        assert "unidades" in config
        assert "general" in config

    def test_set_value(self, tmp_path):
        """Comprueba la modificación de un valor."""

        config_manager = ConfigManager(config_dir=tmp_path)

        config_manager.set_value("unidades", "dimension", "mm")

        assert config_manager.get_value("unidades", "dimension") == "mm"

    def test_set_section(self, tmp_path):
        """Comprueba la modificación de una sección."""

        config_manager = ConfigManager(config_dir=tmp_path)

        unidades = config_manager.get_section("unidades")
        unidades["dimension"] = "mm"
        unidades["volumen"] = "ml"

        config_manager.set_section("unidades", unidades)

        assert config_manager.get_value("unidades", "dimension") == "mm"
        assert config_manager.get_value("unidades", "volumen") == "ml"

    def test_has_changes(self, tmp_path):
        """Comprueba la detección de modificaciones."""

        config_manager = ConfigManager(config_dir=tmp_path)

        assert not config_manager.has_changes()

        config_manager.set_value("unidades", "dimension", "mm")

        assert config_manager.has_changes()

    def test_save(self, tmp_path):
        """Comprueba que la configuración se guarda correctamente."""

        config_manager = ConfigManager(config_dir=tmp_path)

        config_manager.set_value("unidades", "dimension", "mm")

        assert config_manager.save()

        config_file = tmp_path / "config.json"

        assert config_file.exists()

        with open(config_file, "r", encoding="utf-8") as file:
            config = json.load(file)

        assert config["unidades"]["dimension"] == "mm"
        assert not config_manager.has_changes()

    def test_reload(self, tmp_path):
        """Comprueba que se recuperan los valores guardados."""

        config_manager = ConfigManager(config_dir=tmp_path)

        config_manager.set_value("unidades", "dimension", "mm")
        config_manager.save()

        config_manager.set_value("unidades", "dimension", "m")

        assert config_manager.reload()

        assert config_manager.get_value("unidades", "dimension") == "mm"
        assert not config_manager.has_changes()

    def test_reset(self, tmp_path):
        """Comprueba que se restablecen los valores por defecto."""

        config_manager = ConfigManager(config_dir=tmp_path)

        # Guardamos una configuración diferente a la predeterminada.
        config_manager.set_value("unidades", "dimension", "mm")
        config_manager.set_value("unidades", "iluminacion", "lux")
        config_manager.save()

        # Modificamos nuevamente la configuración.
        config_manager.set_value("unidades", "dimension", "m")
        config_manager.set_value("unidades", "iluminacion", "cd")

        # Restablecemos los valores por defecto.
        config_manager.reset()

        assert config_manager.get_value("unidades", "dimension") == "cm"
        assert config_manager.get_value("unidades", "iluminacion") == "lm"

        # Los valores por defecto difieren de los últimos valores guardados.
        assert config_manager.has_changes()

    def test_invalid_section(self, tmp_path):
        """Comprueba que no se permite modificar una sección inexistente."""

        config_manager = ConfigManager(config_dir=tmp_path)

        with pytest.raises(KeyError):
            config_manager.set_value(
                "seccion_inexistente",
                "clave",
                "valor"
            )

    def test_invalid_key(self, tmp_path):
        """Comprueba que no se permite modificar una clave inexistente."""

        config_manager = ConfigManager(config_dir=tmp_path)

        with pytest.raises(KeyError):
            config_manager.set_value(
                "unidades",
                "unidad_inexistente",
                "valor"
            )
