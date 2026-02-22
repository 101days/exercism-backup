color_map = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):
    val = (color_map[colors[0]] * 10 + color_map[colors[1]]) * (
        10 ** color_map[colors[2]]
    )

    if val >= 1_000_000_000 and val % 1_000_000_000 == 0:
        return f"{val // 1_000_000_000} gigaohms"
    if val >= 1_000_000 and val % 1_000_000 == 0:
        return f"{val // 1_000_000} megaohms"
    if val >= 1_000 and val % 1_000 == 0:
        return f"{val // 1_000} kiloohms"

    return f"{val} ohms"
