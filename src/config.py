
from dynaconf import Dynaconf
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[os.path.join(base_dir, 'settings.toml'), os.path.join(base_dir, '.secrets.toml')],
)