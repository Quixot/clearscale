# clearscale

**`clearscale`** is a lightweight Python library that helps you understand and visually compare differences between values (like time, bytes, etc.) in a human-readable way.

## Simple example

```python
from clearscale import how_much_bigger

how_much_bigger("40ms", "100ns")  # → "400 000x"
