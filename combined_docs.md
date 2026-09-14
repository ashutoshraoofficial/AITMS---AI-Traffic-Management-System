# SENTINEL-AI: Solution Presentation Deck
## Statewide Integrated Video Management & AI Analytics Platform
### Gujarat Police Innovation Challenge 2026 | Home Department, Government of Gujarat

---

## SLIDE 1: Title Slide
* **Title**: SENTINEL-AI: Statewide Integrated Video Management & Real-Time AI Platform
* **Subtitle**: Scalable, Edge-Powered CCTV Federation & Automated Watchlist Intelligence for Gujarat Police
* **Initiative**: Gujarat Police Innovation Challenge 2026 (SENTINEL)
* **Partners**: In Association with i-Hub Gujarat, NFSU Gandhinagar & DA-IICT
* **Team**: [Your Team / Organization Name]

---

## SLIDE 2: Problem Understanding & The 80k Camera Challenge
* **The Fragmented Reality**:
  - 26 independent Gujarat Government departments operating siloed CCTV systems.
  - ~80,000 heterogeneous cameras spread across 1,000+ km from Kutch to Valsad.
  - Multi-vendor sprawl: Hikvision, CP Plus, Dahua, Honeywell, Milestone.
  - Disparate retention periods (7 to 15+ days) and isolated storage silos.
* **The Police Imperative**:
  - Law enforcement needs rapid cross-jurisdiction vehicle tracking.
  - Immediate identification of stolen vehicles, suspects, and wanted offenders.
  - Seamless database correlation with **eGujCop, VAHAN, SARTHI, AFIS/NAFIS**.
* **The Bandwidth Bottleneck**: Streaming 80,000 raw 1080p feeds centrally requires **320+ Gbps**, which is impossible over public WAN infrastructure.

---

## SLIDE 3: Proposed Architecture: Hybrid Model 5
* **Strategic Selection**: Proposing a **Hybrid Architecture** combining:
  - **Model 1 (Mandatory Foundation)**: Centralized CCTV Registry & PostGIS Mapping Layer.
  - **Model 4 (AI & VMS Platform)**: Real-time ANPR, vehicle tracking, and automated alerts.
  - **Edge-Cloud Intelligent Tiering**: Overcoming the bandwidth barrier.
* **Core Technological Pillars**:
  1. **Edge Tier**: NVIDIA Jetson Orin nodes at roadside chowkis and toll plazas.
  2. **Transport Tier**: Distributed Apache Kafka Event Bus (JSON metadata only).
  3. **Central Command Tier**: FastAPI, PostGIS, TimescaleDB, and Redis Matcher.
  4. **Operations Tier**: ICCC Command Center with interactive Leaflet GIS and video wall.

---

## SLIDE 4: Edge-to-Cloud Bandwidth Optimization
* **Conventional Centralized Streaming**:
  - 80,000 cameras × 4 Mbps = **320 Gbps** statewide bandwidth demand.
  - High risk of network congestion, dropped frames, and astronomical telecom costs.
* **SENTINEL-AI Edge Paradigm**:
  - Edge AI nodes (NVIDIA Jetson) execute local video decoding, detection, and OCR on-site.
  - Only lightweight JSON metadata (< 500 bytes) transmitted across the WAN.
  - High-res images only uploaded upon a verified watchlist hit or manual inquiry.
* **Results**:
  - **>96% Statewide Bandwidth Savings** (reducing WAN traffic from 320 Gbps to < 12 Gbps).
  - Sub-second local response time (< 400 ms) regardless of external network latency.

---

## SLIDE 5: AI & Video Analytics Architecture
* **Primary Detector — NVIDIA TrafficCamNet**:
  - ResNet18 backbone pre-trained for pole and overhead surveillance perspectives.
  - Accurate multi-class detection: `Car`, `Two-Wheeler`, `Person`, `Road Sign`.
* **Secondary Classifier — NVIDIA LPRNet & High-Speed OCR**:
  - Deep sequence recognition network tailored for Indian license plate formats.
  - Supports standard high-security registration plates (HSRP) and 2-wheeler double-row plates.
* **Multi-Target Tracker — BoT-SORT / NvDCF**:
  - Maintains track identity across occlusions, turns, and lane switches.
* **Cross-Camera Vehicle Re-Identification (ReID)**:
  - Deep visual feature embeddings match vehicle signatures across consecutive highway toll plazas.

---

## SLIDE 6: Law Enforcement Database Correlation
* **Real-time Continuous Cross-Referencing**:
  - In-memory Redis lookup engine matches every detected plate in **< 5 milliseconds**.
* **Multi-Agency Database Integration**:
  - **eGujCop (Gujarat Police CCTNS)**: Stolen vehicles, FIR suspects, wanted criminals $\rightarrow$ **Critical Red Alert**.
  - **VAHAN (MoRTH / Transport)**: Blacklisted vehicles, expired fitness, tax defaulters $\rightarrow$ **Amber Alert**.
  - **SARTHI (Driving Licenses)**: Disqualified drivers, repeat offenders $\rightarrow$ **Automated Notice**.
  - **AFIS / NAFIS**: Biometric criminal records for multi-modal person tracking.
* **Automated Dispatch**:
  - Audio-visual alert on ICCC Video Wall.
  - Instant automated notification to nearest PCR van and field officer tablets.

---

## SLIDE 7: Evaluation Test Case: Vehicle Route Reconstruction
* **The Hackathon Test**: Given a target plate (e.g., `GJ01DX5432`), trace its movement across Gujarat.
* **SENTINEL-AI Route Reconstruction Flow**:
  1. Operator inputs vehicle plate into the ICCC search bar.
  2. Spatiotemporal engine retrieves all chronological sightings across the network.
  3. Interactive Leaflet GIS automatically renders the animated journey route.
  4. Each waypoint displays camera ID, exact timestamp, vehicle image crop, and estimated travel speed.
* **One-Click Audit Dossier**:
  - Instant export of court-admissible CSV / PDF investigation reports with timestamped visual evidence.

---

## SLIDE 8: Scalability & Sizing for 80,000 Cameras
* **Edge Infrastructure**:
  - 8,000 roadside edge nodes (1 unit per 10 cameras) powered by **NVIDIA Jetson Orin NX (16GB)**.
  - Energy efficient: ~15W power consumption per edge node.
* **Central Datacenter Compute**:
  - 32 GPU server nodes (NVIDIA L40S / A100) for cross-camera ReID and heavy analytics.
* **Storage Architecture (Tiered Retention)**:
  - **Hot Tier (0–7 Days)**: Fast NVMe SSD array for high-speed alert clips (~120 TB).
  - **Warm Tier (8–30 Days)**: Scalable Ceph object storage for incident review (~800 TB).
  - **Cold Tier (31–365 Days)**: Cost-effective S3/Tape archive for judicial evidence.

---

## SLIDE 9: Cybersecurity, Interoperability & Governance
* **Strict Vendor Neutrality**:
  - Standardized ONVIF (Profiles S, G, T) and RTSP TCP adapters support any camera manufacturer (CP Plus, Hikvision, Dahua, Prama).
* **Enterprise Security**:
  - Mutual TLS (mTLS) 1.3 encryption across all edge-to-cloud communications.
  - AES-256 encrypted storage at rest for video clips and logs.
* **Role-Based Access Control (RBAC)**:
  - Strict department isolation: Police, RTO, Civil Supplies, and Municipal views remain segregated.
* **Immutable Audit Trail**:
  - Digital signatures and hash chains log every query, video view, and report export for judicial admissibility.

---

## SLIDE 10: Operational Impact & Roadmap
* **Tangible Policing Benefits**:
  - Reduces suspect vehicle intercept time from hours to **under 60 seconds**.
  - Recovers stolen vehicles before state border crossings into Maharashtra, Rajasthan, or MP.
  - Provides a single pane of glass for all 26 state departments.
* **Rollout Roadmap**:
  - **Phase 1 (Months 1–3)**: Model 1 GIS Registry onboarding for all 80,000 cameras.
  - **Phase 2 (Months 4–8)**: Edge AI deployment across critical highway junctions and border checkposts.
  - **Phase 3 (Months 9–12)**: Statewide rollout, eGujCop deep sync, and private camera onboarding.
* **Conclusion**: SENTINEL-AI transforms passive CCTV footage into proactive, statewide operational intelligence for Gujarat Police.
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
