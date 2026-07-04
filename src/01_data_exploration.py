# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# %%
# Path to this script's own folder (src/)
SCRIPT_DIR = Path(__file__).parent
# Go up one level to the repo root, then down into data/raw/
DATA_PATH = SCRIPT_DIR.parent / "data" / "raw" / "Nigeria_Immunisation_Dashboard_Data.xlsx"
df = pd.read_excel(DATA_PATH)

# %%
df.shape
df.info()
df.describe(include='all')

# %%
df.columns = (
    df.columns
    .str.lower()
    .str.replace(' ', '_', regex=False)
    .str.replace(r'[^\w]', '', regex=True)
)
df.columns

# %%
# Zero-dose, dropout rate, stockout, and access barrier are whole-child 
# indicators, not vaccine-specific. Recorded once per LGA-month on the 
# Penta1 row (standard NPHCDA/UNICEF tracer antigen for zero-dose reporting),
# not repeated across all 19 vaccine rows. Hence 1,080 non-null values
# (30 LGAs x 36 months) rather than 20,520.
zero_dose = df[df['vaccine'] == 'Penta1'].copy()
zero_dose.shape
# %%
