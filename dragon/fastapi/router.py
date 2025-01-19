import glob
import importlib
from typing import Optional, List

from fastapi import APIRouter

from dragon.tools.imports import escape_module


class GlobalRouter:
    def __init__(self, prefix: str, path: Optional[str] = 'web/*/**/webviews.py'):
        self.path = path
        self.router = APIRouter(prefix=prefix)

    def export_routers(self) -> List[APIRouter]:
        """
        Import all FastAPI routers dynamically, by default from "web" directory.

        :raises ModuleNotFoundError: If a module cannot be found during the import.
        """

        routers = []

        for m in glob.iglob(self.path, recursive=True):
            module = importlib.import_module(escape_module(m))

            if hasattr(module, 'router'):
                routers.append(module.router)

        return routers

    def __call__(self, *args, **kwargs) -> APIRouter:
        for r in self.export_routers():
            self.router.include_router(r)

        return self.router
