import abc


class ChainWorker(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    async def send(self):
        pass

    @abc.abstractmethod
    async def submit(self):
        pass