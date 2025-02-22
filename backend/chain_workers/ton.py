from backend.chain_workers.base import ChainWorker


class TonWorker(ChainWorker):
    def __init__(self):
        super().__init__()

    async def send(self):
        pass

    async def submit(self):
        pass