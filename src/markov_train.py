import csv

from utils import markov_model
from utils import vpd

HUMIDITY_INDEX = 1
TEMPERATURE_INDEX = 0

RED_STATE = markov_model.MarkovState("red")
PINK_STATE = markov_model.MarkovState("pink")
YELLOW_STATE = markov_model.MarkovState("yellow")
GREEN_STATE = markov_model.MarkovState("green")


def markov_training():
    with open('../data/data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            state_obj = vpd.get_vpd_state(float(row[HUMIDITY_INDEX]), float(row[TEMPERATURE_INDEX]))
            get_next_state(state_obj).counter_up(state_obj)
            get_next_state(state_obj).set_probabilities()

        print(f'{line_count} sets of humidity and temperature were used for the markov chain training')


def get_next_state(next_state_name):
    if next_state_name == "green":
        return GREEN_STATE
    elif next_state_name == "pink":
        return PINK_STATE
    elif next_state_name == "yellow":
        return YELLOW_STATE
    else:
        return RED_STATE


def print_states_info():
    print(RED_STATE.to_string())
    print("\n=======================================\n")
    print(PINK_STATE.to_string())
    print("\n=======================================\n")
    print(YELLOW_STATE.to_string())
    print("\n=======================================\n")
    print(GREEN_STATE.to_string())
