def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "grey": 8, "white": 9
    }
    tolerances = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25,
        "green": 0.5, "brown": 1, "red": 2,
        "gold": 5, "silver": 10
    }

    digit_colors = colors[:-2]
    multiplier_color = colors[-2]
    tolerance_color = colors[-1]

    digits_str = "".join(str(color_values[color]) for color in digit_colors)
    base_ohms = int(digits_str) * (10 ** color_values[multiplier_color])

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit_idx = 0
    final_ohms = base_ohms

    while final_ohms >= 1000 and unit_idx < len(units) - 1:
        final_ohms /= 1000
        unit_idx += 1

    if isinstance(final_ohms, float) and final_ohms.is_integer():
        final_ohms = int(final_ohms)

    tolerance_val = tolerances[tolerance_color]
    return f"{final_ohms} {units[unit_idx]} ±{tolerance_val}%"