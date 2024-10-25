import os
import sys
import json

import pandas as pd
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# %%
# STEP 1A: Initial Read Ops and JSON Data Overview
with open('data/products.json', 'r') as file:
    products_data = json.load(file)
# %%
