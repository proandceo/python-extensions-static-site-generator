import sys
import importlib
from pathlib import Path


def load_module(self, directory, name):
    sys.path.insert(directory, 0)
    importlib.import_module(name)
    sys.path.pop(0)
