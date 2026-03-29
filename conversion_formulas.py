def inches_to_mm_conversion(user_input: float):
    return round(user_input * 25.4, 2)


def fahr_to_cels_conversion(user_input: float):
    return round((user_input - 32) / 1.8, 2)


def pound_to_kilo_converson(user_input: float):
    return round(user_input / 2.20462262, 2)


def mph_to_kmh_conversion(user_input: float):
    return round(user_input * 1.609344, 2)


def knots_mph_conversion(user_input: float):
    return round(user_input * 1.15078, 2)