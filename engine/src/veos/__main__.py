import sys

from .cli import main
from .core import apply_home_env

apply_home_env()  # temp files and caches inside VEOS_HOME (never AppData / the system temp)
sys.exit(main())
