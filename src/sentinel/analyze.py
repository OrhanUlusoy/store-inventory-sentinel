def analyze_inventory(df):
    """
    Computes a normalized risk score based on demand and price pressure.
    """

    # --- Normalize inputs ---
    df["footfall_norm"] = df["footfall"] / df["footfall"].max()
    df["promo_norm"] = df["promotion_intensity"] / df["promotion_intensity"].max()
    df["price_pressure"] = df["competitor_price"] / df["price"]

    # --- Demand pressure ---
    df["demand_pressure"] = df["footfall_norm"] * df["promo_norm"]

    # --- Risk score (safe denominator) ---
    df["risk_score"] = (
        df["demand_pressure"] * df["price_pressure"]
    ) / (df["stock_level"] + 1)

    return df
