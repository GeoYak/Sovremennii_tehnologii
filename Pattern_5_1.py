class Mediator:
    def register_runway(self, runway):
        """Регистрируем полосу у посредника"""

        pass

    def register_terminal(self, terminal):
        """Регистрируем терминал у посредника"""

        pass

    def runway_ready(self, runway):
        """Полоса готова к использованию"""

        pass

    def terminal_ready(self, terminal):
        """Полоса готова к использованию"""

        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self.runways = []
        self.terminals = []

    def register_runway(self, runway):

        """Регистрируем полосу у посредника"""

        self.runways.append(runway)

    def register_terminal(self, terminal):

        """Регистрируем терминал у посредника"""

        self.terminals.append(terminal)

    def runway_ready(self, runway):

        """Полоса готова к использованию"""

        for t in self.terminals:
            if not t.busy:
                t.assign_runway(runway)
                break

    def terminal_ready(self, terminal):

        """Полоса готова к использованию"""

        for r in self.runways:
            if not r.busy:
                r.assign_terminal(terminal)
                break


class Runway:
    def __init__(self):
        self.busy = False
        self.assigned_terminal = None

    def assign_terminal(self, terminal):
        """Полосе присваивается терминал"""

        self.busy = True
        self.assigned_terminal = terminal
        print(f'Полоса {id(self)} назначена терминалу {id(terminal)}.')
        terminal.busy = True
        terminal.assigned_runway = self

    def release(self):
        """Полоса освобождается"""

        self.busy = False
        print(f'Полоса {id(self)} освобождена.')


class Terminal:
    def __init__(self):
        self.busy = False
        self.assigned_runway = None

    def assign_runway(self, runway):
        """Терминалу присваивается полоса"""

        self.busy = True
        self.assigned_runway = runway
        print(f'Терминал {id(self)} назначен полосе {id(runway)}.')
        runway.busy = True
        runway.assigned_terminal = self

    def release(self):
        """Терминал освобождается"""

        self.busy = False
        print(f'Терминал {id(self)} освобожден.')


mediator = ConcreteMediator()
runways = [Runway() for _ in range(3)]
terminals = [Terminal() for _ in range(5)]
for r in runways:
    mediator.register_runway(r)
for t in terminals:
    mediator.register_terminal(t)

mediator.terminal_ready(terminals[0])
terminals[0].release()
runways[0].release()
mediator.terminal_ready(terminals[1])
terminals[1].release()
mediator.terminal_ready(terminals[2])
