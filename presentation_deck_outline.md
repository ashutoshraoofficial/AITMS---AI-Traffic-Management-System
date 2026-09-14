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
