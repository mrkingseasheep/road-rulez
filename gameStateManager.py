class GameStateManager:
    def __init__(self, current_state):
        self.currentState = current_state

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state
