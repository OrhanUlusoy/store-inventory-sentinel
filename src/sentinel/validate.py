REQUIRED_COLUMNS = {
    "price",
    "stock_level",
    "footfall",
    "promotion_intensity",
    "competitor_price",
}


def validate_sales_data(df):
    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(sorted(missing))}"
        )

    if (df["stock_level"] < 0).any():
        raise ValueError("Stock level contains negative values")

    if (df["price"] <= 0).any():
        raise ValueError("Price contains non-positive values")

    return True
