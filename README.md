# ⚖️ BMI Calculator (Python GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

A lightweight, user-friendly desktop application built with Python and **Tkinter**. This app allows users to quickly calculate their Body Mass Index (BMI) by inputting their weight and height, and immediately see their health category based on standard metrics.

---

## ✨ Features

- **Clean & Simple UI**: A minimal, centered GUI window.
- **Instant Calculation**: Get your exact BMI score with a single click.
- **Smart Categorization**: Automatically classifies your result (e.g., Normal weight, Obese).
- **Input Validation**: Prevents app crashes by catching invalid inputs (text or negative numbers) and showing a helpful error dialog.


## 📊 BMI Categories

The application uses the standard classification system:

| BMI Range ($kg/m^2$) | Category Classification | Health Indicator |
| :--- | :--- | :---: |
| **$< 18.5$** | Under weight | 🔵 |
| **$18.5 - 24.9$** | Normal weight | 🟢 |
| **$25.0 - 29.9$** | Over weight | 🟡 |
| **$30.0 - 34.9$** | Obese | 🟠 |
| **$\ge 35.0$** | Extremely obese | 🔴 |


## 💻 Code Structure

- `calculate_bmi()`: Core logic to fetch inputs, validate them, compute the math ($BMI = weight / height^2$), and update the UI.
- `show_category()`: Determines the BMI string category.
- `main()`: Handles the Tkinter window setup, widgets (Labels, Entries, Buttons), and window centering geometry.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

