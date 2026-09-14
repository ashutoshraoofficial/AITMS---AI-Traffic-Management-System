# SENTINEL-AI: Comprehensive Technical Documentation
**Gujarat Police Innovation Challenge 2026 (SENTINEL)**

## 1. Executive Summary
SENTINEL-AI is an enterprise-grade Video Management System (VMS) and AI Analytics platform engineered explicitly for the Gujarat Police. It manages an unprecedented scale of 80,000 CCTV cameras by decentralizing AI inference to the edge, drastically reducing bandwidth overhead, and enabling sub-second watchlist correlations.

## 2. Why SENTINEL-AI Stands Out (Our USPs)
1. **Edge-AI Bandwidth Eradication**: Instead of transmitting 320 Gbps of raw video, our nodes transmit JSON metadata (under 12 Gbps statewide), saving 96% of network costs and ensuring uptime even in remote areas like Kutch.
2. **Zero-Latency Database Correlation**: Real-time asynchronous WebSocket pipelines match plates against eGujCop/VAHAN databases in under 400ms.
3. **Hardware Agnosticism & Acceleration**: Built to leverage Apple Silicon (MPS) for rapid prototyping and NVIDIA Jetson (TensorRT) for production, proving immediate adaptability.
4. **Interactive Spatiotemporal Tracing**: A unified GIS interface (Leaflet/OSM) that visually reconstructs a suspect vehicle's precise route, timestamps, and velocity across the state.
5. **Multi-Department Multi-Tenancy**: Granular Role-Based Access Control (RBAC) allowing RTOs, Traffic Police, and Civil Supplies to utilize the same infrastructure securely.

## 3. High-Level Architecture (HLD)
- **Tier 1 (Edge Node)**: NVIDIA Jetson Orin running DeepStream pipelines. Executes YOLOv11 vehicle detection and LPRNet plate recognition locally.
- **Tier 2 (Telemetry Bus)**: Apache Kafka cluster digesting 80,000 JSON metadata streams per second.
- **Tier 3 (State Database)**: PostgreSQL/TimescaleDB for time-series camera sightings, Elasticsearch for sub-second plate lookups.
- **Tier 4 (Command Dashboard)**: FastAPI backend with React/HTML5 WebSockets, featuring a live customizable video wall and automated alerts.

## 4. Artificial Intelligence Pipeline
- **Vehicle Detection**: Fine-tuned YOLOv11 model detecting Cars, Trucks, Two-Wheelers, and Buses.
- **ANPR (Number Plate)**: Optimized optical character recognition handling single-line, double-line, and high-security registration plates (HSRP).
- **Multi-Object Tracking**: BoT-SORT algorithm maintaining vehicle identities across blind spots and sequential highway toll plazas.

## 5. Security & Compliance
- **Zero-Trust (ZTNA)**: Mutual TLS authentication for edge-to-core telemetry.
- **Audit Logging**: Immutable cryptographic logging of all video exports and plate searches for Indian judicial evidentiary standards.
