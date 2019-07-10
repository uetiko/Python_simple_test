from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration


class CoreIoC(DeclarativeContainer):
    config = Configuration('config')