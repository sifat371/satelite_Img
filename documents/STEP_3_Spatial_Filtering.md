# Step 3: Spatial Filtering in Satellite Images

## Objective
To study how different spatial filters remove noise from satellite images and
to understand their impact on edges, textures, and smooth regions.
focuses on **restoration attempts**, not enhancement.

---

## Filters Applied

### 1. Mean Filter
- Computes the average of neighboring pixels.
- Effective for reducing low-level Gaussian noise.
- Blurs edges and fine details.

**Observation:**
- Noise is reduced.
- Roads and boundaries become less sharp.
- Performs poorly on salt-and-pepper noise.

---

### 2. Median Filter
- Replaces each pixel with the median value of its neighborhood.
- Non-linear filter.

**Observation:**
- Very effective for salt-and-pepper noise.
- Preserves edges better than mean filtering.
- Minimal blurring of structural details.

---

### 3. Gaussian Filter
- Uses a weighted average based on a Gaussian distribution.
- Controlled smoothing via kernel size and sigma.

**Observation:**
- Effective for Gaussian noise.
- Provides smoother results than mean filtering.
- Edge blurring depends on kernel size and sigma.

---

## Effect of Filter Size
- Smaller kernels (3×3): preserve details but remove less noise.
- Larger kernels (5×5): remove more noise but blur edges.

---

## Key Takeaway
Different filters exist because **no single filter works optimally for all noise types**.
Filter selection must be based on the noise model and image characteristics.
