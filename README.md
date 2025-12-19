# Car Detection for ADAS using MobileNet CNN (Seminar Project & Paper)

A lightweight CNN-based car detection demo built for Advanced Driver Assistance Systems (ADAS) using MobileNet.

## Features
- Classifies and separates static vs moving car frames
- Uses pre-trained MobileNet for efficient inference
- Runs on CPU in under 10 minutes

## Quick Start
1. Create a virtual environment  
python -m venv .venv


2. Activate it  
- Windows → .venv\Scripts\activate  
- macOS/Linux → source .venv/bin/activate


3. Install dependencies  
pip install -r requirements.txt


4. Run the demo  
python src/main.py


## Dataset
Includes 100 demo frames (≈20 MB total) under data/ for quick testing.

## Results
See visual outputs in assets/.

## License
MIT License
