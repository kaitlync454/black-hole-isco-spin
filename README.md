# Kerr Black Hole ISCO Calculator

## Overview

This project calculates the innermost stable circular orbit (ISCO) for a test particle orbiting a rotating Kerr black hole. It investigates how the black hole's dimensionless spin and mass relate to the ISCO radius.

The project combines an analytical calculation implemented in Python, automated tests, and numerical comparisons of prograde and retrograde orbits.

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

Positive spin represents prograde orbits in the adopted convention, while negative spin represents retrograde orbits.

The gravitational radius is

\[
r_g = \frac{GM}{c^2}.
\]

The physical ISCO radius can be written as

\[
r_{\mathrm{ISCO}} = \rho_{\mathrm{ISCO}}r_g,
\]

where \(\rho_{\mathrm{ISCO}}\) is the dimensionless ISCO radius calculated from the Kerr spin parameter.

For equatorial circular orbits, the dimensionless ISCO radius is calculated using the analytical Kerr ISCO expression:

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

At zero spin, the prograde and retrograde branches meet at the Schwarzschild value of \(6r_g\). The implementation handles this limit directly.

## Project Features

- Calculates the dimensionless ISCO radius for a Kerr black hole.
- Converts black hole mass from solar masses to gravitational radius in meters.
- Converts the ISCO radius into kilometers.
- Checks the allowed spin range and validates black hole mass inputs.
- Plots ISCO radius as a function of dimensionless spin.
- Compares physical ISCO radii for black holes with different masses.
- Compares prograde, nonrotating, and retrograde cases.
- Includes automated tests for limiting cases, an intermediate spin, and invalid inputs.

## Repository Structure

```text
Black-hole-ISCO-spin/
├── ISCO.py
├── test_isco.py
├── plot_isco.py
├── mass_comparison.py
├── orbit_comparison.py
├── requirements.txt
├── README.md
└── isco_vs_spin.png
```

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the plotting dependencies with:

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
python test_isco.py
```

Generate the ISCO-versus-spin plot:

```bash
python plot_isco.py
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

For the implemented Kerr ISCO calculation, representative dimensionless radii are:

| Dimensionless spin | ISCO radius (\(r_g\)) | Orbit |
|---:|---:|---|
| -1.000 | 9.0000 | Extremal retrograde limit |
| -0.900 | 8.7174 | Retrograde |
| -0.500 | 7.5546 | Retrograde |
| 0.000 | 6.0000 | Nonrotating |
| +0.500 | 4.2330 | Prograde |
| +0.900 | 2.3209 | Prograde |
| +0.998 | 1.2370 | Near-extremal prograde |
| +1.000 | 1.0000 | Extremal prograde limit |

The results show that the ISCO radius decreases for prograde orbits as the spin increases in the adopted convention, and increases for retrograde orbits as the magnitude of negative spin increases.

At fixed spin, the dimensionless ISCO radius remains constant as black hole mass changes. The physical ISCO radius scales linearly with mass because the gravitational radius is proportional to mass.

## Validation

The automated test script checks:

- The Schwarzschild limit at zero spin.
- The extremal prograde and retrograde limits.
- An intermediate-spin reference value.
- Rejection of spin values outside the allowed range.
- Rejection of nonpositive black hole masses.

The tests currently pass for the implemented calculations.

## Assumptions and Limitations

- The model describes an idealized Kerr black hole.
- The ISCO expression applies to equatorial circular test-particle orbits.
- The calculation does not model an accretion disk's hydrodynamics, magnetic fields, radiation, or plasma processes.
- The extremal spin cases are mathematical limits; astrophysical black holes may not attain these exact limits.
- The project evaluates an analytical expression numerically; it does not independently derive the Kerr metric or solve the full geodesic equations.

## Future Work

Potential extensions include:

- Comparing results against independently published reference values.
- Adding numerical precision and edge-case tests.
- Improving plot annotations and scientific presentation.
- Exploring how mass and spin affect physical length scales.
- Investigating the relationship between ISCO location and accretion-disk properties.

## References

1. Bardeen, J. M., Press, W. H., & Teukolsky, S. A. (1972). *Rotating Black Holes: Locally Nonrotating Frames, Energy Extraction, and Scalar Synchrotron Radiation*. The Astrophysical Journal, 178, 347–369. https://doi.org/10.1086/151796

2. Shapiro, S. L., & Teukolsky, S. A. (1983). *Black Holes, White Dwarfs, and Neutron Stars: The Physics of Compact Objects*. Wiley.

---

*This project is an educational computational astrophysics project developed to explore the dependence of Kerr black hole ISCO radii on spin and mass.*