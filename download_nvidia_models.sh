#!/bin/bash
set -e

PROJECT_DIR="/Users/ashutoshrao/Desktop/Road Traffic AI Project"
cd "$PROJECT_DIR/models"

echo "========================================================"
echo "📥 DOWNLOADING NVIDIA NGC PRODUCTION MODELS (.etlt)"
echo "========================================================"

# 1. Download NVIDIA TrafficCamNet (Pruned INT8/FP16 TAO Model)
if [ ! -f "trafficcamnet.etlt" ]; then
    echo "⬇️ Downloading NVIDIA TrafficCamNet from NGC Catalog..."
    curl -L -f -o trafficcamnet.zip "https://api.ngc.nvidia.com/v2/models/nvidia/tao/trafficcamnet/versions/pruned_v1.0/zip"
    unzip -o -q trafficcamnet.zip
    # Rename for consistency with our DeepStream configs
    mv resnet18_trafficcamnet_pruned.etlt trafficcamnet.etlt || true
    rm trafficcamnet.zip
    echo "✅ TrafficCamNet downloaded."
else
    echo "✅ TrafficCamNet already downloaded."
fi

# 2. Download NVIDIA LPRNet (Pruned License Plate Recognition TAO Model)
if [ ! -f "lprnet.etlt" ]; then
    echo "⬇️ Downloading NVIDIA LPRNet from NGC Catalog..."
    curl -L -f -o lprnet.zip "https://api.ngc.nvidia.com/v2/models/nvidia/tao/lprnet/versions/pruned_v1.0/zip"
    unzip -o -q lprnet.zip
    # Rename for consistency
    mv us_lprnet_baseline18_pruned.etlt lprnet.etlt || true
    rm lprnet.zip
    echo "✅ LPRNet downloaded."
else
    echo "✅ LPRNet already downloaded."
fi

echo "========================================================"
echo "🎉 NVIDIA MODELS SUCCESSFULLY DOWNLOADED!"
ls -lh *.etlt
echo "========================================================"
