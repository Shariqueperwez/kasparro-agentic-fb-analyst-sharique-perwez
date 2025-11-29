#!/bin/bash

# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate data
python setup_data.py

# 3. Run the analysis
python run.py "Analyze why ROAS dropped"