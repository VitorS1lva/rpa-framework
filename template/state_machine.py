from template.components.initialize_environment.initialize_environment import InitializeEnvironment

class StateMachine:
    def __init__(self):
        self.state = InitializeEnvironment(self)  # Estado inicial
        self.global_variables = {}  # Variáveis globais compartilhadas
        self.queue_items = []  # Lista de itens da fila

    def run(self):
        # while not isinstance(self.state, finalstate):
        #     self.state.execute()

        # Executa o estado final
        self.state.execute()


    def transition_to(self, new_state):
        self.state = new_state