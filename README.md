# SENTINEL-AI: Integrated Video Management & Analytics Platform
### Gujarat Police Innovation Challenge 2026 (SENTINEL)
*Developed for Home Department, Government of Gujarat in association with i-Hub, NFSU & DA-IICT.*

---

## 🌟 Overview

**SENTINEL-AI** is a statewide video management and edge-AI analytics platform designed to federate **~80,000 CCTV cameras** across 26 Gujarat Government departments (Police, RTO, Food & Civil Supplies, Municipal Corporations) and private commercial entities.

### Key Capabilities
* **Registry & GIS Foundation (Model 1)**: Interactive map covering 50+ onboarded cameras across Ahmedabad, Gandhinagar, Surat, Vadodara, Rajkot, Jamnagar, and border checkpoints.
* **Unified Live Viewing (Model 2/4)**: Multi-camera live grid supporting RTSP TCP ingestion with real-time AI bounding box and plate overlays.
* **Vehicle Trajectory Tracer**: Instant spatiotemporal route reconstruction and journey tracing on the GIS map for any searched vehicle registration number.
* **Law Enforcement Watchlist Matching**: Continuous cross-referencing with **eGujCop** (stolen/wanted), **VAHAN** (blacklisted/fitness expired), and **SARTHI** databases with sub-second real-time alert dispatch.
* **95%+ Bandwidth Reduction**: Edge AI computing architecture powered by **NVIDIA Jetson Orin** and **NVIDIA DeepStream SDK**.
* **1-Click Evaluation Export**: Automated generation of the official timestamped CSV/PDF report for hackathon judges.

---

## 🚀 Quick Start (Running Locally on Mac mini M4)

### 1. Launch Platform
In your terminal, navigate to this project folder and run:
```bash
cd "/Users/ashutoshrao/Desktop/Road Traffic AI Project"
bash start.sh
```

### 2. Access Command & Control Dashboard
Open your browser and navigate to:
```
http://localhost:8000
```

### 3. Conduct the Hackathon Evaluation Test Case
1. **View GIS Cameras**: Browse 50+ camera markers plotted across Gujarat cities. Click any camera to view its department and live status.
2. **Observe Video Wall**: See real-time feeds with vehicle bounding boxes and ANPR plate overlays.
3. **Trace Vehicle Journey**:
   - In the sidebar search box, enter designated plate: `GJ01DX5432` (or click one of the quick buttons).
   - Click **Trace**.
   - The map automatically draws the chronological animated route from Ahmedabad SG Highway to Gandhinagar GIFT City with timestamped waypoints!
4. **Trigger Real-Time Alerts**: Watch the live watchlist feed flash whenever a stolen or wanted vehicle is detected.
5. **Download Evaluation CSV**: Click **"📥 Download Official Evaluation CSV"** to generate the evidence log required by the screening committee.

---

## 📁 Project Structure

```
├── app.py                             # FastAPI backend & WebSocket alert broker
├── ai_engine.py                       # M4 MPS / YOLO vehicle detection & ANPR engine
├── database.py                        # SQLite storage & eGujCop watchlist database
├── download_all_models.sh             # Automatic downloader for vision models
├── generate_evaluation_report.py      # Official evaluation CSV report generator
├── start.sh                           # One-click execution script
├── requirements.txt                   # Python dependencies
├── hld_technical_proposal.md          # Complete High-Level Design (HLD) submission document
├── presentation_deck_outline.md       # 10-slide presentation deck for evaluation
├── models/                            # Downloaded model weights
│   ├── yolov8n.pt                     # YOLOv8 vehicle detection model (6.2 MB)
│   └── yolo11n.pt                     # YOLO11 next-gen detection model (5.4 MB)
├── templates/
│   └── index.html                     # ICCC Command & Control Dashboard (Leaflet GIS)
└── nvidia_deepstream_configs/         # Production NVIDIA Metropolis deployment configs
    ├── deepstream_app_config.txt      # Multi-stream DeepStream 7.x pipeline
    ├── config_infer_primary_trafficcamnet.txt
    └── config_infer_secondary_lprnet.txt
```

---

## 🏗️ Production Architecture (80,000 Statewide Cameras)

* **Edge Compute**: 8,000 roadside nodes powered by **NVIDIA Jetson Orin NX (16GB)** running DeepStream 7.0 with **NVIDIA TrafficCamNet** and **LPRNet**.
* **WAN Optimization**: Edge nodes transmit only lightweight JSON metadata and triggered alert snapshots over encrypted site-to-site IPsec VPN, reducing statewide bandwidth from **320 Gbps to < 12 Gbps**.
* **Central ICCC**: Distributed Apache Kafka event bus, PostgreSQL/PostGIS spatial registry, TimescaleDB event store, and Redis in-memory watchlist matcher.
