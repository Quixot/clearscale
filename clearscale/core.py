import re

UNIT_MULTIPLIERS = {
    "s": 1,
    "ms": 1e-3,
    "us": 1e-6,
    "ns": 1e-9,
}

def parse_value(s):
    match = re.fullmatch(r"(\d+(?:\.\d+)?)([a-z]+)", s.strip().lower())
    if not match:
        raise ValueError(f"Invalid unit string: {s}")
    value, unit = match.groups()
    return float(value) * UNIT_MULTIPLIERS[unit]

def how_much_bigger(a, b):
    """Return how many times `a` is bigger than `b` (e.g., '400000x')."""
    av = parse_value(a)
    bv = parse_value(b)
    if bv == 0:
        return "∞"
    return f"{av / bv:.0f}x"
