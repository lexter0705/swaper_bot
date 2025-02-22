import abc

from backend.chain_workers.base import ChainWorker


class DexWorker(abc.ABC):
    def __init__(self, chain_worker: ChainWorker):
        self.__chain_worker = chain_worker

    @abc.abstractmethod
    async def swap(self):
        pass

    @property
    def chain_worker(self):
        return self.__chain_worker


