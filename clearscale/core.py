import re

UNIT_MULTIPLIERS = {
    # Time
    "ns": 1e-9,
    "us": 1e-6, "µs": 1e-6,
    "ms": 1e-3,
    "s": 1,
    "min": 60,
    "h": 3600,

    # Data size (bytes)
    "b": 1,
    "kb": 1e3,
    "mb": 1e6,
    "gb": 1e9,
    "tb": 1e12,

    # Length (meters)
    "nm": 1e-9,
    "um": 1e-6,  # alt for μm
    "μm": 1e-6,
    "mm": 1e-3,
    "cm": 1e-2,
    "m": 1,
    "km": 1e3,

    # Mass (grams)
    "mg": 1e-3,
    "g": 1,
    "kg": 1e3,
    "t": 1e6,

    # Energy (Joules)
    "j": 1,
    "kj": 1e3,
    "mj": 1e6,
    "wh": 3600,
    "kwh": 3.6e6,
}

UNIT_GROUPS = {
    "time": ["ns", "us", "µs", "ms", "s", "min", "h"],
    "data": ["b", "kb", "mb", "gb", "tb"],
    "length": ["nm", "um", "μm", "mm", "cm", "m", "km"],
    "mass": ["mg", "g", "kg", "t"],
    "energy": ["j", "kj", "mj", "wh", "kwh"],
}


def parse_value(s):
    match = re.fullmatch(r"(\d+(?:\.\d+)?)([a-z]+)", s.strip().lower())
    if not match:
        raise ValueError(f"Invalid unit string: {s}")
    value, unit = match.groups()
    return float(value) * UNIT_MULTIPLIERS[unit]

def how_much_bigger(a, b, precision=2):
    """Return how many times `a` is bigger than `b`, e.g., '400000x' or '1.25x'"""
    av = parse_value(a)
    bv = parse_value(b)
    if bv == 0:
        return "∞"
    ratio = av / bv
    if ratio == int(ratio):
        return f"{int(ratio)}x"
    return f"{round(ratio, precision)}x"

def smart_unit(seconds: float) -> str:
    """Convert seconds into the most appropriate unit."""
    thresholds = [
        (1e-9, "ns"),
        (1e-6, "µs"),
        (1e-3, "ms"),
        (1, "s"),
        (60, "min"),
        (3600, "h"),
    ]

    for threshold, unit in reversed(thresholds):
        if seconds >= threshold:
            value = seconds / threshold
            return f"{value:.2f}{unit}"
    return f"{seconds:.2e}s"

def smart_unit(value: float, unit_type: str = "auto") -> str:
    """
    Convert a base-unit value to a human-readable format.
    If unit_type is 'auto', the function tries to guess the group.
    """
    # Try to guess group if not specified
    if unit_type == "auto":
        unit_type = guess_unit_group(value)

    units = UNIT_GROUPS.get(unit_type)
    if not units:
        raise ValueError(f"Unknown or unsupported unit type: {unit_type}")

    # Sort units by multiplier
    units_sorted = sorted(units, key=lambda u: UNIT_MULTIPLIERS[u])

    for u in reversed(units_sorted):
        threshold = UNIT_MULTIPLIERS[u]
        if value >= threshold:
            return f"{value / threshold:.2f}{u}"
    # Если меньше самой маленькой единицы
    smallest = units_sorted[0]
    return f"{value / UNIT_MULTIPLIERS[smallest]:.2f}{smallest}"

def guess_unit_group(value: float) -> str:
    # Временные диапазоны
    if value < 86400:
        return "time"
    # Масса в граммах
    elif value < 1e6:
        return "mass"
    # Длина в метрах
    elif value < 1e5:
        return "length"
    # Энергия
    elif value < 1e9:
        return "energy"
    # По умолчанию — данные
    else:
        return "data"
