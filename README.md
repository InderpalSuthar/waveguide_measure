# Waveguide Length Measurement Tool for KLayout

An interactive extension for **KLayout** that calculates the exact total path length of selected waveguide traces directly from the layout viewer.

---

## Overview

When working with converted geometry, imported GDS files, or manual drawings in KLayout, PCell metadata is often lost, making it difficult to determine exact waveguide path lengths. 

This tool adds an interactive action under the **Tools** menu (complete with a custom menu icon) that allows you to select arbitrary waveguide shapes or boxes and instantly calculates their total path length in micrometers ($\mu\text{m}$) by evaluating area and trace width.

---

## Features

* **Instant Selection Measurement:** Select single or multiple waveguide segments/polygons on screen and get immediate feedback.
* **Automatic Layout DBU Scaling:** Works seamlessly across layout databases with different Database Units (DBU).
* **Clear GUI Pop-up:** Displays results in a native KLayout message box.
* **Custom Toolbar/Menu Icon:** Fits natively into KLayout's user interface.

---

## Installation

### Method 1: KLayout Package Manager (Recommended)
1. Open KLayout.
2. Go to **Tools > Manage Packages**.
3. Select **Install New Packages**.
4. Search for `waveguide_measure` and click **Install**.
5. Restart KLayout.

### Method 2: Manual Installation
1. Download or clone this repository.
2. Copy the `waveguide_measure` folder into your local KLayout `salt` directory:
   * **Windows:** `%USERPROFILE%\KLayout\salt\`
   * **Linux/macOS:** `~/.klayout/salt/`
3. Restart KLayout.

---

## Usage

1. Open your layout in KLayout.
2. Select one or more waveguide shapes/polygons on screen.
3. Click on **Tools > Measure Waveguide Length** in the menu bar.
4. A pop-up dialog will display the total combined path length in $\mu\text{m}$.

---

## License

This project is licensed under the MIT License - see the `grain.xml` file for details.