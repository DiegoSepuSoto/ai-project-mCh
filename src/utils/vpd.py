import math

RED_STATE = "red"
PINK_STATE = "pink"
YELLOW_STATE = "yellow"
GREEN_STATE = "green"

LATENT_HEAT_OF_VAPORIZATION = 2.5e6
GAS_CONSTANT_FOR_WATER_VAPOR = 461


def get_svp(temperature):
    return math.exp(
        (LATENT_HEAT_OF_VAPORIZATION / GAS_CONSTANT_FOR_WATER_VAPOR) * ((1 / 273) - 1 / (273 + temperature))) * 6.11


def get_vpd(humidity, temperature):
    return ((100 - humidity) / 100) * (get_svp(temperature))


def get_vpd_state(humidity, temperature):
    vpd = get_vpd(humidity, temperature)
    if vpd <= 4.5:
        return PINK_STATE
    elif 4.5 < vpd <= 7.4 or 10.6 <= vpd <= 12.4:
        return YELLOW_STATE
    elif 7.4 < vpd <= 10.5:
        return GREEN_STATE
    else:
        return RED_STATE
