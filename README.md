# Kerr Black Hole ISCO Calculator

## Overview

This project calculates the innermost stable circular orbit (ISCO) radius for a test particle orbiting a rotating Kerr black hole. It examines how the black hole's dimensionless spin determines the ISCO radius and how black hole mass affects the corresponding physical length scale.

The project uses an analytical Kerr ISCO expression implemented in Python, automated validation tests, and numerical comparisons of black hole spin and mass. NumPy is used for numerical calculations and Matplotlib for visualization.

## Scientific Background

The innermost stable circular orbit is the smallest radius at which a test particle can maintain a stable circular orbit under the assumptions of the model.

For a rotating Kerr black hole, the ISCO depends on the dimensionless spin parameter:

\[
a_* = \frac{cJ}{GM^2}
\]

where:

- \(a_*\) is the dimensionless spin parameter, with \(-1 \leq a_* \leq 1\).
- \(J\) is the black hole's angular momentum.
- \(G\) is the gravitational constant.
- \(M\) is the black hole's mass.
- \(c\) is the speed of light.

In the sign convention used here, positive spin corresponds to prograde equatorial orbits, while negative spin corresponds to retrograde equatorial orbits.

The gravitational radius is

\[
r_g = \frac{GM}{c^2}.
\]

The physical ISCO radius is

\[
r_{\mathrm{ISCO}} = \rho_{\mathrm{ISCO}}r_g,
\]

where \(\rho_{\mathrm{ISCO}}\) is the dimensionless ISCO radius.

For equatorial circular test-particle orbits, the dimensionless radius is calculated using the analytical Kerr ISCO expression:

\[
Z_1 = 1 + (1-a_*^2)^{1/3}
\left[(1+|a_*|)^{1/3}+(1-|a_*|)^{1/3}\right]
\]

\[
Z_2 = \sqrt{3a_*^2+Z_1^2}
\]

\[
\rho_{\mathrm{ISCO}} =
3+Z_2-\operatorname{sgn}(a_*)
\sqrt{(3-Z_1)(3+Z_1+2Z_2)}.
\]

At zero spin, the prograde and retrograde cases coincide at the Schwarzschild value of \(6r_g\). The implementation handles this limit.

## Project Features

- Calculates dimensionless ISCO radii for Kerr black holes.
- Calculates the gravitational radius from black hole mass in solar-mass units.
- Converts dimensionless radii into physical length scales.
- Validates spin and mass inputs.
- Visualizes the ISCO radius as a function of dimensionless spin.
- Compares physical radii for black holes of different masses.
- Compares prograde, nonrotating, and retrograde cases.
- Tests analytical benchmark values, physical trends, and mass scaling.

## Repository Structure

```text
Black-hole-ISCO-spin/
├── ISCO.py
├── test_ISCO.py
├── plot_ISCO.py
├── mass_comparison.py
├── orbit_comparison.py
├── requirements.txt
├── README.md
├── .gitignore
└── isco_vs_spin.png
```

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run the main calculator:

```bash
python ISCO.py
```

Run the automated tests:

```bash
python test_ISCO.py
```

Generate the ISCO-versus-spin plot:

```bash
python plot_ISCO.py
```

Compare black holes of different masses:

```bash
python mass_comparison.py
```

Compare prograde and retrograde orbits:

```bash
python orbit_comparison.py
```

## Results

Representative dimensionless ISCO radii calculated by the model are shown below.

| Dimensionless spin \(a_*\) | ISCO radius (\(r_g\)) | Orbit |
|---:|---:|---|
| -1.000 | 9.0000 | Extremal retrograde limit |
| -0.900 | 8.7174 | Retrograde |
| -0.500 | 7.5546 | Retrograde |
| 0.000 | 6.0000 | Nonrotating |
| +0.500 | 4.2330 | Prograde |
| +0.900 | 2.3209 | Prograde |
| +0.998 | 1.2370 | Near-extremal prograde |
| +1.000 | 1.0000 | Extremal prograde limit |

The results show that the ISCO moves inward as prograde spin increases and outward as the magnitude of retrograde spin increases.

At a fixed dimensionless spin, the dimensionless ISCO radius does not depend on black hole mass. The physical radius scales linearly with mass because \(r_g = GM/c^2\).

The plot `isco_vs_spin.png` visualizes the relationship between dimensionless spin and ISCO radius, including the Schwarzschild reference value.

## Validation

The automated tests check:

- The Schwarzschild limit at zero spin.
- The extremal prograde and retrograde limits.
- Reference values at several intermediate spin parameters.
- The expected decrease in ISCO radius as spin increases across the tested range.
- Rejection of spin values outside the allowed range.
- Rejection of nonpositive black hole masses.
- Linear scaling of gravitational radius with mass.
- Positivity of the gravitational radius for valid masses.

The tests passed for the implemented calculations. These checks help verify the implementation against known limits and expected physical behavior; they do not independently prove the underlying analytical model.

## Assumptions and Limitations

- The model assumes an idealized Kerr black hole described by general relativity.
- The ISCO expression applies to equatorial circular test-particle orbits.
- The calculation does not simulate an accretion disk or model its hydrodynamics, magnetic fields, radiation, or plasma processes.
- Exact extremal spin values are included as mathematical limits. Their inclusion does not imply that astrophysical black holes attain those limits.
- The project evaluates an established analytical expression numerically; it does not independently derive the Kerr metric or solve the full geodesic equations.
- Numerical results depend on the accuracy of the implementation and the precision of the calculations.

## Future Work

Potential extensions include:

- Comparing results with additional independently implemented reference calculations.
- Testing additional edge cases and numerical precision.
- Examining how spin and mass affect physical ISCO length scales.
- Exploring the relationship between ISCO location and accretion-disk properties.
- Extending the analysis with more detailed physical models.

## References

1. Bardeen, J. M., Press, W. H., & Teukolsky, S. A. (1972). "Rotating Black Holes: Locally Nonrotating Frames, Energy Extraction, and Scalar Synchrotron Radiation." *The Astrophysical Journal*, 178, 347–369. https://doi.org/10.1086/151796

2. Shapiro, S. L., & Teukolsky, S. A. (1983). *Black Holes, White Dwarfs, and Neutron Stars: The Physics of Compact Objects*. Wiley.

---

*This is an educational computational astrophysics project exploring the dependence of Kerr black hole ISCO radii on spin and mass.*