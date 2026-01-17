def generate_recommendations(df):
    """
    Adds a business recommendation based on risk status.
    """

    def recommend(row):
        if row["status"] == "ACTION_REQUIRED":
            if row["stock_level"] < 20:
                return "Increase stock immediately"
            elif row["price"] > row["competitor_price"]:
                return "Consider price adjustment"
            else:
                return "Reduce promotion intensity"
        elif row["status"] == "RISK":
            return "Monitor closely"
        else:
            return "No action needed"

    df["recommendation"] = df.apply(recommend, axis=1)
    return df
