# Aero-Ground-Control-Station-Simulation
A Python &amp; Socket-based Miniature Ground Control Station (GCS) that visualizes real-time UAV/Satellite telemetry data over TCP/IP network.

# 🛰️ Aero Ground Control Station (GCS) & Telemetry Simulator

This project is a miniature **Ground Control Station (GCS)** system designed for UAVs and satellites. It establishes a local network architecture using Python's `socket` programming to capture and visualize real-time aeronautical data (temperature, stability status) over a TCP/IP connection.

## 🛠️ System Architecture
- **UAV/Satellite Simulator (`iha_simulasyon.py`):** Acts as the client, generating and serializing simulated sensor data (temperature and motion status) and transmitting it via port 50005.
- **Ground Control Station (`yer_control.py`):** Acts as the server, hosting a modern GUI using `customtkinter` and rendering real-time graphs with `matplotlib`.

## 📸 Screenshots
*(Buraya az önce bana attığın o harika çalışan arayüz ekran görüntüsünü yükle!)*

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   py -m pip install customtkinter matplotlib
   ```
3. First, start the Ground Control Station (Server):
   ```bash
   py yer_control.py
   ```
4. Then, run the UAV Simulator (Client):
   ```bash
   py iha_simulasyon.py
   ```

## 🧠 What I Learned
- Network Architecture (Socket Programming, TCP/IP, Ports, Client-Server model).
- Multi-threading in Python to handle concurrent GUI rendering and network data stream.
- Object-Oriented Programming (OOP) for GUI design.
