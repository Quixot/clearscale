# clearscale

**clearscale** — это лёгкая библиотека для Python, которая помогает понять и визуально оценить разницу между величинами (время, байты и т.д.) в человекочитаемом виде.

## Пример

```python
from clearscale import how_much_bigger

how_much_bigger("40ms", "100ns")  # → "400 000x"
