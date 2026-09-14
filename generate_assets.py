import os
import markdown
from fpdf import FPDF
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# --- 1. Documentation Content ---
md_content = """# SENTINEL-AI: Comprehensive Technical Documentation
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
"""

# Write to MD
with open("SENTINEL_Technical_Documentation.md", "w") as f:
    f.write(md_content)

# Convert to PDF
class DocPDF(FPDF):
    pass

pdf = DocPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=11)
html = markdown.markdown(md_content)
pdf.write_html(html)
pdf.output("SENTINEL_Technical_Documentation.pdf")

# --- 2. PPTX Generation ---
prs = Presentation()

slides_data = [
    ("SENTINEL-AI", "Integrated CCTV & AI Traffic Management System\n\nGujarat Police Innovation Challenge 2026"),
    ("The 80,000 Camera Problem", "- 80K cameras generate ~320 Gbps of raw video data\n- Cost-prohibitive bandwidth requirements\n- Fragmented systems across departments (Police, RTO)"),
    ("Our Solution: Edge-AI Architecture", "- Process video LOCALLY at the junction (NVIDIA Jetson)\n- Transmit lightweight JSON metadata (96% bandwidth savings)\n- Unified GIS Command Center"),
    ("Why We Stand Out (USPs)", "- Edge-AI Bandwidth Eradication\n- Zero-Latency eGujCop/VAHAN Database Correlation (<400ms)\n- Hardware Agnostic (Apple MPS + NVIDIA TensorRT)\n- Interactive Spatiotemporal Route Tracing"),
    ("Key Feature: Live Video Wall", "- Interactive WebSockets Dashboard\n- Seamless Multi-Stream RTSP playback\n- Expandable HUD with hardware telemetry"),
    ("Key Feature: Route Reconstruction", "- Input a suspect plate number (e.g. GJ01DX5432)\n- View chronological path on OpenStreetMap\n- Auto-generates court-admissible audit PDFs"),
    ("Technical Stack", "- AI: YOLOv11, NVIDIA TrafficCamNet, DeepStream\n- Backend: Python, FastAPI, WebSockets, Kafka\n- DB: PostgreSQL, Elasticsearch\n- UI: HTML5, Leaflet.js"),
    ("Thank You!", "Ready for Deployment across Gujarat.\n\nDemonstration ready on local feeds & Government RTSP Sandbox.")
]

for title, content in slides_data:
    slide_layout = prs.slide_layouts[1] # Title and Content
    slide = prs.slides.add_slide(slide_layout)
    title_placeholder = slide.shapes.title
    body_placeholder = slide.placeholders[1]
    
    title_placeholder.text = title
    body_placeholder.text = content
    
prs.save("SENTINEL_Pitch_Deck.pptx")

# --- 3. PPTX to PDF via FPDF (Landscape) ---
class SlidePDF(FPDF):
    pass

pdf_ppt = SlidePDF(orientation='L', unit='mm', format='A4')
pdf_ppt.set_auto_page_break(auto=True, margin=15)

for title, content in slides_data:
    pdf_ppt.add_page()
    pdf_ppt.set_fill_color(30, 41, 59) # Dark background
    pdf_ppt.rect(0, 0, 297, 210, 'F')
    
    pdf_ppt.set_text_color(255, 255, 255)
    pdf_ppt.set_font("Helvetica", style="B", size=28)
    pdf_ppt.set_y(40)
    pdf_ppt.cell(0, 15, title, ln=True, align="C")
    
    pdf_ppt.set_y(80)
    pdf_ppt.set_font("Helvetica", size=18)
    for line in content.split('\n'):
        pdf_ppt.cell(0, 10, line, ln=True, align="C")

pdf_ppt.output("SENTINEL_Pitch_Deck.pdf")

print("Successfully generated all documents, PPTX, and PDFs.")
