
from datetime import datetime
from logging import log
from pathlib import Path

from sentinel.ingest import load_sales_data
from sentinel.validate import validate_sales_data
from sentinel.analyze import analyze_inventory
from sentinel.classify import classify_products
from sentinel.recommend import generate_recommendations



def run_pipeline():
    run_id = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    run_dir = Path("runs") / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    log_file = run_dir / "log.txt"
    report_file = run_dir / "report.md"

    # ---------- LOG ----------
    with open(log_file, "w", encoding="utf-8") as log:
        log.write(f"Run started: {run_id}\n")

        df = load_sales_data()
        log.write(f"Sales data loaded: {len(df)} rows\n")
        log.write(f"Columns found: {list(df.columns)}\n")

        validate_sales_data(df)
        log.write("Data validation passed\n")

        df = analyze_inventory(df)
        log.write("Inventory analysis completed\n")

        log.write(
            f"Risk score stats: "
            f"min={df['risk_score'].min():.2f}, "
            f"mean={df['risk_score'].mean():.2f}, "
            f"max={df['risk_score'].max():.2f}\n"
        )
        
        df = classify_products(df)
        log.write("Product classification completed\n")
        df = generate_recommendations(df)
        log.write("Recommendations generated\n")


    # ---------- REPORT ----------
    with open(report_file, "w", encoding="utf-8") as report:
        report.write("# Store Inventory Sentinel Report\n\n")
        report.write(f"Run ID: {run_id}\n\n")

        report.write("## Inventory Status Summary\n")
        summary = df["status"].value_counts()
        for status, count in summary.items():
            report.write(f"- {status}: {count} products\n")

        report.write("\n## Recommendations Summary\n")
        recommendation_counts = df["recommendation"].value_counts()
        for rec, count in recommendation_counts.items():
            report.write(f"- {rec}: {count} situations\n")

        report.write("\n### High Priority Actions\n")
        top_actions = df[df["status"] == "ACTION_REQUIRED"].head(5)
        for _, row in top_actions.iterrows():
            report.write(
                f"- Risk score: {row['risk_score']:.2f} → {row['recommendation']}\n"
            )
