COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]

COLORS_TOLERANCE = {
    'brown': 1,
    'red': 2,
    'green': 0.5,
    'blue': 0.25,
    'violet': 0.1,
    'grey': 0.05,
    'gold': 5,
    'silver': 10
}

def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'
    
    *digits, multiplier, tolerance = colors
    base_val = int("".join(str(COLORS.index(c)) for c in digits))
    value = base_val * (10 ** COLORS.index(multiplier))
    value, unit = format_unit(value)
    value = int(value) if value == int(value) else value
    return f'{value} {unit} ±{COLORS_TOLERANCE[tolerance]}%'
        
def format_unit(value):
    units = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    for unit in units:
        if value < 1000:
            return value, unit
        value /= 1000
    return value, units[-1] 