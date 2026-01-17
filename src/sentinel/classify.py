from sentinel.config import RISK_THRESHOLDS

def classify_products(df):
    def classify(row):
        if row["risk_score"] > RISK_THRESHOLDS["ACTION_REQUIRED"]:
            return "ACTION_REQUIRED"
        elif row["risk_score"] > RISK_THRESHOLDS["RISK"]:
            return "RISK"
        else:
            return "OK"

    df["status"] = df.apply(classify, axis=1)
    return df
