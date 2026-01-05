# Step 2: Noise Models in Satellite Images

## Objective
To create controlled degradation in satellite images
by adding synthetic noise.

This allows systematic evaluation of filtering techniques.

---

## Why Add Synthetic Noise?
- Real noise is unpredictable
- Synthetic noise allows repeatable experiments
- Known noise models enable objective evaluation

---

## Noise Models Implemented

### 1. Gaussian Noise
Models sensor noise and atmospheric disturbances.

Mathematical model:

g(x, y) = f(x, y) + η(x, y)

Where:
- η(x, y) follows a Gaussian distribution
- Mean = 0
- Variance = σ²

#### Parameters Used
- σ = 10 (low noise)
- σ = 20 (higher noise)

---

### Observations (Gaussian Noise)
- Appears as fine grain across the image
- Affects all pixels
- Edges remain visible but degraded as σ increases

---

### 2. Salt-and-Pepper Noise
Models transmission errors and impulse noise.

Characteristics:
- Random pixels set to 0 (black) or 255 (white)
- Sparse but extreme intensity changes

#### Parameter Used
- Noise probability p = 0.02

---

### Observations (Salt-and-Pepper Noise)
- Isolated black and white pixels
- Local pixel destruction
- Strongly affects averaging filters

---

## Key Insight
Different noise models affect images in fundamentally different ways.
Understanding the noise type is essential for selecting an appropriate
filtering strategy.

---

## EXM Notes
*Gaussian noise introduces small intensity variations across all pixels,
while salt-and-pepper noise introduces extreme values at random locations,
making them behave differently under spatial filtering.*
