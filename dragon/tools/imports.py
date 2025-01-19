import glob
import importlib
from typing import List, Optional


def escape_module(module: str) -> str:
    """
    Converts a module path into a dotted module name by replacing directory
    separators with dots and removing the ".py" file extension if present.
    """

    return module.replace("\\", ".").replace("/", ".").replace(".py", "")


def export_models(path: Optional[str] = "domain/**/*/model.py") -> List[str]:
    """
    Imports all models by searching recursively for `model.py` files in the
    specified directory structure and escaping their module paths. Returns the
    list of models.
    """

    models = ["aerich.models"]
    for m in glob.iglob(path, recursive=True):
        models.append(escape_module(m))

    return models


def import_webviews(path: Optional[str] = "web/*/**/webviews.py") -> None:
    """
    Imports all webviews modules dynamically, by default from the "web" directory.

    :raises ModuleNotFoundError: If a module cannot be found during the import.
    """

    for m in glob.iglob(path, recursive=True):
        importlib.import_module(escape_module(m))
