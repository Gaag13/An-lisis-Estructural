# Análisis de un Pórtico Plano de Concreto con Cimentación en Pilas

Este proyecto modela y analiza un pórtico plano de concreto soportado por pilas en un suelo de dos estratos (blando y rígido). Se emplea un modelo estático para estudiar el comportamiento del conjunto estructura + cimentación + suelo, considerando los siguientes parámetros:

## Características de la Estructura:
- **Material**: Concreto (*E = 2 \times 10^7* kN/m²)
- **Geometría**:
  - *a = 2.05* m
  - *b = 1.8* m
  - *c = 4* m
  - *d = 2.7* m
  - *H = 5* m
- **Cargas**:
  - Carga distribuida: *q = 60* kN/m
  - Carga puntual: *P = 70* kN

## Condiciones de Cimentación:
- Pilas circulares con diámetro de 80 cm.
- Se desprecia la fricción entre el fuste de las pilas y el suelo blando.
- Se modela la rigidez lateral del suelo con *k<sub>Lateral</sub> = 5000* kN/m².
- Se considera el efecto de la fuerza axial desacoplada.
- Se emplea apoyo simple en la punta de las pilas.

## Dependencias necesarias:
Para la ejecución del análisis, se requieren las siguientes librerías en Python:

```python
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
```

Asegúrate de tenerlas instaladas antes de ejecutar el código.
