import time


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class Currency(Observable):
    def __init__(self, name, exchange_rate):
        super().__init__()
        self.name = name
        self.exchange_rate = exchange_rate

    def set_exchange_rate(self, new_rate):
        self.exchange_rate = new_rate
        self.notify_observers()


class Observer:
    def update(self, observable):
        pass


class Graph(Observer):
    def __init__(self, currency):
        self.currency = currency

    def update(self, observable):
        print(f"Graph for {self.currency.name}: {self.currency.exchange_rate}")


if __name__ == '__main__':
    usd = Currency('USD', 1)
    eur = Currency('EUR', 0.85)

    graph_usd = Graph(usd)
    graph_eur = Graph(eur)

    usd.add_observer(graph_usd)
    eur.add_observer(graph_eur)

    while True:
        usd.set_exchange_rate(1.2)
        time.sleep(1)
        usd.set_exchange_rate(1.4)
        time.sleep(1)
        eur.set_exchange_rate(1)
        time.sleep(1)
        eur.set_exchange_rate(0.8)
        time.sleep(1)
