# SENTINEL: High-Level Design (HLD) & Technical Proposal
## Statewide Integrated Video Management & AI Analytics Platform
### Gujarat Police Innovation Challenge 2026 (Home Department, Government of Gujarat)

---

## 1. Executive Summary

The State of Gujarat encompasses a vast geography spanning over 196,000 sq km and connecting critical transport corridors, border districts, industrial clusters, and major urban centers (Ahmedabad, Gandhinagar, Surat, Vadodara, Rajkot, Bhavnagar, Jamnagar). Currently, **26 independent Government Departments** operate isolated CCTV networks with heterogeneous hardware, incompatible VMS vendors (Hikvision, CP Plus, Dahua, Honeywell, Milestone), varying retention schedules (7 to 15+ days), and disparate storage configurations.

**SENTINEL-AI** is a unified, vendor-agnostic, and future-ready Video Management and Analytics Platform designed to federate **~80,000 public and private CCTV cameras** across the State. Combining the mandatory **Model 1 (CCTV Registry & GIS Foundation)** with **Model 4 (Central VMS & Advanced AI Platform)** in an innovative **Edge-Cloud Hybrid Architecture**, SENTINEL-AI enables:
- Seamless multi-departmental video federation without disrupting legacy VMS infrastructure.
- Real-time Automatic Number Plate Recognition (ANPR) and vehicle classification.
- Sub-second cross-referencing against national and state law enforcement databases (**eGujCop, VAHAN, SARTHI, AFIS, NAFIS**).
- Automated real-time alert dispatch to police control rooms and field officers.
- Instant spatiotemporal vehicle route reconstruction and journey tracing.
- Over **95% statewide WAN bandwidth reduction** via localized edge intelligence.

---

## 2. System Architecture & Component Interaction

```
[ Camera Tier: ~80,000 Feeds across 26 Departments ]
  ├── Police Traffic & City Surveillance (PTZ, Fixed, ANPR)
  ├── RTO Checkposts & Driving Testing Tracks
  ├── Food & Civil Supplies Godowns & PDS Centers
  └── Private Societal / Commercial Cameras (Malls, Corridors)
               │
               ▼ (RTSP / ONVIF Profiles S, G, T / TCP)
┌──────────────────────────────────────────────────────────────────┐
│  Tier 1: Intelligent Edge Tier (Junctions, Tolls, Chowkis)       │
│  - Edge Compute: NVIDIA Jetson Orin Nano / Orin NX               │
│  - Video Ingestion: Hardware-accelerated NVDEC (H.264 / H.265)   │
│  - Primary Inference: NVIDIA TrafficCamNet (Vehicle & Pedestrian) │
│  - Multi-Object Tracking: NvDCF / BoT-SORT                       │
│  - Secondary Inference: NVIDIA LPRNet (High-Speed ANPR OCR)      │
│  - Filter: Bandwidth Saver — sends only JSON metadata & crops    │
└──────────────────────────────────────────────────────────────────┘
               │
               ▼ (Encrypted TLS 1.3 / Site-to-Site IPsec VPN)
┌──────────────────────────────────────────────────────────────────┐
│  Tier 2: Event Transport & Ingestion Message Bus                 │
│  - Distributed Apache Kafka Cluster / Redis Streams              │
│  - High throughput (>250,000 events/sec capacity)                │
└──────────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Tier 3: Central Command & AI Core (State ICCC Datacenter)       │
│  - Ingestion Engine: FastAPI / Go High-Throughput Consumers      │
│  - Watchlist Correlation Engine: In-Memory Redis + Rule Matrix   │
│  - Spatial & Asset Database: PostgreSQL + PostGIS (Model 1 GIS)  │
│  - Time-Series Database: TimescaleDB (Telemetry & Sightings)     │
│  - Search Engine: Elasticsearch (Sub-second Plate History Query)  │
│  - Hot/Warm/Cold Storage: MinIO Distributed Object Storage / S3  │
│  - Cross-Camera ReID: Deep Learning Vehicle Re-Identification    │
└──────────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Tier 4: Unified Command & Control Dashboard (ICCC Operations)   │
│  - Interactive Gujarat GIS Map (Leaflet.js / MapLibre GL)        │
│  - Configurable Video Wall & Multi-Camera Live Grid              │
│  - Automated Real-time Alert Notification Center                 │
│  - Vehicle Route Reconstruction & Spatiotemporal Breadcrumbs     │
│  - Evaluation & Audit Report Generator (CSV / PDF)               │
└──────────────────────────────────────────────────────────────────┘
```

---

## 3. The 80,000 Camera Bandwidth Problem & Edge-AI Solution

### The Conventional Bottleneck
Streaming 80,000 raw 1080p video feeds centrally at 4 Mbps per stream requires:
$$\text{Total Bandwidth} = 80,000 \times 4\text{ Mbps} = 320,000\text{ Mbps} = 320\text{ Gbps}$$
Transmitting 320 Gbps across statewide public WAN infrastructure is cost-prohibitive, fragile, and prone to single-point network failure.

### The SENTINEL-AI Edge Architecture
1. **Edge Intelligence**: Each roadside junction or toll plaza hosts an **NVIDIA Jetson Orin NX** node managing 8–16 camera channels.
2. **Local Inference**: Jetson nodes execute hardware-accelerated video decoding (NVDEC), vehicle detection (TrafficCamNet), tracking (NvDCF), and plate recognition (LPRNet) on-site.
3. **Metadata-Only Transmission**: Under normal conditions, only compact JSON telemetry is transmitted upstream:
   ```json
   {
     "camera_id": "GJ-AHM-SG-042",
     "timestamp": "2026-09-15T14:23:18.421Z",
     "plate_number": "GJ01DX5432",
     "vehicle_class": "Car",
     "confidence": 0.962,
     "lat": 23.0722,
     "lon": 72.5164
   }
   ```
   *Average payload per detection: < 500 bytes.*
4. **Triggered Snapshot Upload**: High-resolution cropped vehicle and plate imagery is only transmitted when a potential watchlist hit, incident, or manual operator request occurs.
5. **Bandwidth Savings**: Reduces required statewide WAN bandwidth from **320 Gbps to under 12 Gbps (>96% savings)**, ensuring flawless operational stability even in remote border corridors (Kutch, Banaskantha, Dahod).

---

## 4. AI & Video Analytics Engine

### 4.1 Primary Vehicle & Person Detection: NVIDIA TrafficCamNet
- **Architecture**: Deep convolutional neural network (ResNet18 backbone) pre-trained on surveillance camera angles.
- **Classes**: `Car`, `Two-Wheeler`, `Person`, `Road Sign`.
- **Optimization**: TensorRT INT8 quantization delivering >120 FPS per stream on edge accelerators.

### 4.2 License Plate Recognition: NVIDIA LPRNet & Deep OCR
- **Architecture**: Connectionist Temporal Classification (CTC) sequence recognition network.
- **Indian Number Plate Adaptation**: Accommodates single-row and double-row Indian vehicle plates, state codes (GJ, MH, DL, etc.), high-security registration plates (HSRP), and non-standard font variations.

### 4.3 Multi-Object Tracking & Cross-Camera Re-Identification (ReID)
- **Tracking Algorithm**: BoT-SORT with Kalman Filtering and appearance feature extraction.
- **Spatiotemporal ReID**: Maintains consistent track IDs across momentary blind spots and matches vehicle visual embeddings across successive highway toll plazas.

---

## 5. Law Enforcement Database Integration

SENTINEL-AI incorporates a high-performance **Database Correlation Engine** that continuously cross-references live ANPR reads with:

| Database | Authority | Target Entities | Alert Trigger Condition |
| :--- | :--- | :--- | :--- |
| **eGujCop** | Gujarat Police (CCTNS) | Stolen Vehicles, Wanted History-Sheeters, FIR Suspects | Immediate Red Alert (Audio-Visual + SMS/WhatsApp Dispatch) |
| **VAHAN** | MoRTH / Gujarat Transport | Blacklisted Plates, Expired Fitness, Unregistered | Amber Alert (Traffic Violation Queue / E-Challan) |
| **SARTHI** | MoRTH | Suspended Driving Licenses, Repeat Violators | Automated Verification Workflow |
| **AFIS / NAFIS** | NCRB / SCRB Gandhinagar | Wanted Criminals, Repeat Offenders | High-Priority Tactical Alert to Local PCR Vans |

### Alert SLA & Dispatch Workflow
- **Detection to Alert Latency**: **< 400 milliseconds**.
- **Alert Dispatch**: Real-time push to the ICCC Video Wall, local Police Control Room (PCR), and mobile push notification to nearest patrolling police units via geotagged proximity dispatch.

---

## 6. Vehicle Journey Tracing & Route Reconstruction

The problem statement requires immediate tracing of a designated vehicle registration number across the CCTV grid:

1. **Query Execution**: Operator inputs plate registration (e.g. `GJ01DX5432`) or partial plate wildcard (`GJ01*`).
2. **Spatiotemporal Breadcrumb Query**: Elasticsearch and TimescaleDB retrieve all historical sightings sorted chronologically.
3. **GIS Route Visualization**:
   - Leaflet/MapLibre engine plots markers at each camera location.
   - A directional polyline animates the traversed journey over time.
   - Speed estimation is automatically calculated based on camera-to-camera distance and delta time ($\Delta d / \Delta t$).
4. **Visual Evidence Dossier**: Each sighting point displays:
   - High-res vehicle image crop and license plate snippet.
   - Exact UTC timestamp and camera identifier.
   - Camera geographical coordinates and department ownership.
5. **One-Click Audit Report**: Generates official court-admissible PDF/CSV evidence reports with cryptographic hash checksums.

---

## 7. Infrastructure Sizing for 80,000 Statewide Cameras

### 7.1 Edge Tier Sizing
- **Total Cameras**: 80,000.
- **Edge Deployment Model**: 1 Edge Node per 10 cameras at local chowkis/junctions.
- **Edge Units**: 8,000 units of **NVIDIA Jetson Orin NX (16GB)**.
- **Local Power Draw**: ~15W per edge appliance.

### 7.2 Central Datacenter Sizing (Gandhinagar SCRB / GSDC)
- **Central GPU Cluster**: 32 Enterprise GPU Servers (each equipped with 4× NVIDIA L40S or A100 GPUs) for centralized ReID, VLM queries, and fallback streams.
- **Message Bus Cluster**: 12-node Apache Kafka cluster configured for triple replication.
- **Database Cluster**: 6-node PostgreSQL + PostGIS cluster with TimescaleDB sharding.
- **Storage Architecture (Tiered Retention)**:
  - **Hot Storage (0–7 days)**: NVMe SSD array for high-speed alert clips, plate crops, and recent telemetry (~120 TB).
  - **Warm Storage (8–30 days)**: High-density Ceph object storage for incident archives (~800 TB).
  - **Cold Storage (31–365 days)**: Tiered S3 tape/object storage for court-evidence archives.

---

## 8. Cybersecurity, Resilience & Governance

1. **Zero-Trust Network Access (ZTNA)**: Mutual TLS (mTLS) authentication between all edge nodes and central command.
2. **Video Stream Encryption**: AES-256 encryption in transit (SRTP / RTSP over TLS) and at rest.
3. **Role-Based Access Control (RBAC)**: Department-wise multi-tenancy:
   - *Police Admins*: Full operational access, alert dispatch, route tracing.
   - *RTO Officers*: Vehicle fitness, overloading, registration violations.
   - *PDS / Civil Supplies*: Facility-only camera monitoring.
4. **Audit Logs & Chain of Custody**: Every video view, plate query, and export action is immutably logged with digital signatures for evidentiary integrity in Indian judicial proceedings.
5. **Disaster Recovery (DR)**: Active-Passive hot standby datacenter replication between Gandhinagar and secondary Gujarat state datacenter with RPO < 5 seconds and RTO < 15 minutes.
