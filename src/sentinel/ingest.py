from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/raw/retail_sales.csv")


def load_sales_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Sales data not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    if df.empty:
        raise ValueError("Sales data is empty")

    return df
