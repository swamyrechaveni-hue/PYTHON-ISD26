scales = ["C", "F", "K"]


def convert(temperature_scale: str = "C", temperature_input: str = "0"):
    if temperature_scale not in scales:
        return 0.0, 32.0, 273.15

    if temperature_scale == "C":
        c = float(temperature_input)
        f = (c * 9/5) + 32
        k = c + 273.15

    elif temperature_scale == "F":
        f = float(temperature_input)
        c = (f - 32) * 5/9
        k = (f + 459.67) * 5/9

    elif temperature_scale == "K":
        k = float(temperature_input)
        c = k - 273.15
        f = (k - 273.15) * 9/5 + 32

    return c, f, k