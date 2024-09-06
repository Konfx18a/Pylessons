import multiprocessing as mp
import time

class WarehouseManager:

    def __init__(self):
        self.data = mp.Manager().dict()


    def process_request(self, data, p, op, vol):
        if op == 'receipt':
            data[p] = vol
        if op == 'shipment':
            if data.get(p):
                data[p] = data[p] - vol if data[p] - vol > 0 else 0
            else:
                print ('Товар на складе отсутствует')


    def run(self, request):
        proceses = []
        for i in request:
            p = mp.Process(target=self.process_request, args=(self.data, *i))
            proceses.append(p)
        for i in proceses:
            i.start()
            i.join()





manager = WarehouseManager()

requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

manager.run(requests)
print(manager.data)

