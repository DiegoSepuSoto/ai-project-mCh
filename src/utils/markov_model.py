from tabulate import tabulate


class MarkovState:
    name = ""
    red_state_count = 0
    pink_state_count = 0
    yellow_state_count = 0
    green_state_count = 0
    red_transition_prob = 0.0
    pink_transition_prob = 0.0
    yellow_transition_prob = 0.0
    green_transition_prob = 0.0

    def __init__(self, name):
        self.name = name
        self.red_state_count = 1
        self.pink_state_count = 1
        self.yellow_state_count = 1
        self.green_state_count = 1
        self.red_transition_prob = 0.25
        self.pink_transition_prob = 0.25
        self.yellow_transition_prob = 0.25
        self.green_transition_prob = 0.25

    def counter_up(self, state):
        if state == 'green':
            self.red_state_count += 1
        elif state == 'pink':
            self.red_state_count += 1
        elif state == 'yellow':
            self.red_state_count += 1
        else:
            self.red_state_count += 1

    def get_count_sum(self):
        return self.red_state_count + self.green_state_count + self.pink_state_count + self.yellow_state_count

    def set_probabilities(self):
        self.red_transition_prob = self.red_state_count * (1 / self.get_count_sum())
        self.pink_transition_prob = self.pink_state_count * (1 / self.get_count_sum())
        self.yellow_transition_prob = self.yellow_state_count * (1 / self.get_count_sum())
        self.green_transition_prob = self.green_state_count * (1 / self.get_count_sum())

    def to_string(self):
        return f'Final results for the {self.name} state:\n {tabulate([["Red", f"{round(self.red_transition_prob, 4) * 100}%"], ["Pink", f"{round(self.pink_transition_prob, 4) * 100}%"], ["Yellow", f"{round(self.yellow_transition_prob, 4) * 100}%"], ["Green", f"{round(self.green_transition_prob, 4) * 100}%"]], headers=["Next State", "Probability"])}'
