# Daikibo-machine-health-dashboard (Simulation)

This is a simple Python-based simulation of a machine health monitoring dashboard for Daikibo Corporation, created as part of the Forage virtual experience.

## 💡 Project Overview

This simulation displays the real-time health status of machines in four factories. Each factory has three machines, and each machine is randomly assigned a status of:

- ✅ Healthy
- ⚠️ Warning
- ❌ Critical

The system prints a formatted summary of all machines across all factories to the console.

## 🛠️ Technologies Used

- Python 3
- `random` module for simulating dynamic health states

## 📋 How It Works

- A dictionary stores factory names and machine names.
- A function `show_status()` loops through each machine and assigns a random health status.
- Results are printed in a clean, readable format on the console.

## 🧪 Example Output

