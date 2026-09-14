#!/bin/bash
set -e

PROJECT_DIR="/Users/ashutoshrao/Desktop/Road Traffic AI Project"
cd "$PROJECT_DIR"
mkdir -p models
mkdir -p "$HOME/.EasyOCR/model"

echo "========================================================"
echo "📥 DOWNLOADING ALL PRETRAINED AI MODELS FOR SENTINEL-AI"
echo "========================================================"

# 1. YOLOv8n (Vehicle & Pedestrian Detection, 6.2 MB)
if [ ! -f "models/yolov8n.pt" ]; then
    echo "⬇️ [1/4] Downloading YOLOv8n (Vehicle Detection - 6.2 MB)..."
    curl -L -f -o models/yolov8n.pt "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt"
else
    echo "✅ [1/4] YOLOv8n already downloaded."
fi

# 2. YOLO11n (Next-Gen Ultralytics SOTA, 5.4 MB)
if [ ! -f "models/yolo11n.pt" ]; then
    echo "⬇️ [2/4] Downloading YOLO11n (Next-Gen Vehicle Detection - 5.4 MB)..."
    curl -L -f -o models/yolo11n.pt "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt"
else
    echo "✅ [2/4] YOLO11n already downloaded."
fi

# 3. EasyOCR CRAFT Text Detector (4.5 MB)
if [ ! -f "$HOME/.EasyOCR/model/craft_mlt_25k.pth" ]; then
    echo "⬇️ [3/4] Downloading EasyOCR CRAFT Text Detector (4.5 MB)..."
    curl -L -f -o models/craft_mlt_25k.zip "https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/craft_mlt_25k.zip"
    unzip -o -q models/craft_mlt_25k.zip -d "$HOME/.EasyOCR/model"
    cp "$HOME/.EasyOCR/model/craft_mlt_25k.pth" models/
    rm -f models/craft_mlt_25k.zip
else
    echo "✅ [3/4] CRAFT Text Detector already downloaded."
fi

# 4. EasyOCR Latin/English OCR Recognizer (44.8 MB)
if [ ! -f "$HOME/.EasyOCR/model/latin_g2.pth" ]; then
    echo "⬇️ [4/4] Downloading EasyOCR License Plate Character Recognizer (44.8 MB)..."
    curl -L -f -o models/latin_g2.zip "https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/latin_g2.zip"
    unzip -o -q models/latin_g2.zip -d "$HOME/.EasyOCR/model"
    cp "$HOME/.EasyOCR/model/latin_g2.pth" models/
    rm -f models/latin_g2.zip
else
    echo "✅ [4/4] License Plate Character Recognizer already downloaded."
fi

echo "========================================================"
echo "🎉 ALL MODELS SUCCESSFULLY DOWNLOADED AND VERIFIED!"
echo "Total Storage Used: $(du -sh models | cut -f1)"
echo "========================================================"
ls -lh models
