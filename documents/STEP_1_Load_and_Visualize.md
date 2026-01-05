# Step 1: Load and Visualize Satellite Images

## Objective
To load satellite images and understand them as digital signals
before applying any noise or processing.

This step establishes the **baseline image characteristics** that
determine how noise and filters behave later.

---

## Dataset
- EuroSAT RGB images
- Labels are ignored
- Images are treated as signals, not classes

---

## Process
1. Load an RGB satellite image
2. Convert the image to grayscale
3. Visualize RGB and grayscale images side by side

---

## Why Grayscale Conversion?
In Digital Image Processing, a grayscale image is modeled as a
two-dimensional intensity function:

f(x, y)

Where:
- x, y → spatial coordinates
- f(x, y) → intensity value

Most noise models and spatial filters are defined on grayscale images.

---

## Observations from Satellite Images

### Smooth Regions
- Water bodies, farmland, forests
- Filters perform well here

### Sharp Edges
- Roads, rivers, boundaries
- Susceptible to blurring during filtering

### Textured Areas
- Urban and industrial regions
- Harder to distinguish noise from texture

---

## Key Insight
Satellite images contain a mixture of smooth regions, sharp edges,
and textures. These characteristics strongly influence the performance
of noise removal filters.


