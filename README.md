# Pyramage - Python Random Image Creator

This is a python package that will help you create a random image with perlin noise algorithm.

## Installation
```bash
  pip install pyramage
```

## Generating A Random Image

```python
from randimg import Randimg

Randimg.generate_perlin_image(100, 4, 'terrain')
                              # size, # perlin scan depth, # colormap (cmap)
```

## Dependencies
~ matplotlib
~ numpy
