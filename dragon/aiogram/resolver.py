from typing import Any, Callable

from aiogram import Router


class Resolver:
    def __init__(self, router: Router) -> None:
        self.router = router

    def message(self, *filters: Callable[[Any], bool]) -> Callable[[Callable], Callable]:
        def decorator(func):
            self.router.message.register(func, *filters)
            return func

        return decorator

    def callback(self, *filters: Callable[[Any], bool]) -> Callable[[Callable], Callable]:
        def decorator(func):
            self.router.callback_query.register(func, *filters)
            return func

        return decorator
