import pandas as pd

RANGES = {
    "SleepHours": (4, 10),
    "HeartRate": (50, 100),
    "Steps": (1000, 20000),
}

def load_data(file_path: str) -> pd.DataFrame:
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .json")

def data_quality_report(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "missing": df.isnull().sum().to_dict(),
        "describe": df.describe().to_dict(),
    }

def quality_check(df: pd.DataFrame):
    errors = []
    error_mask = pd.Series(False, index=df.index)

    for col, (low, high) in RANGES.items():
        col_err = ~df[col].between(low, high)
        if col_err.any():
            errors.append(f"{col} out of range ({low}-{high}).")
            error_mask |= col_err

    return errors, df[error_mask]

def run_pipeline(file_path: str):
    df = load_data(file_path)
    report = data_quality_report(df)
    errors, error_rows = quality_check(df)

    if not errors:
        print(f"\n✅ {file_path} - No errors found. Showing 5 data lines:\n")
        print(df.head())
    else:
        print(f"\n❌ {file_path} - Data Quality Errors Detected:")
        for err in errors:
            print("-", err)
        print("\nRows with errors:\n", error_rows)

if __name__ == "__main__":
    for file in ["fitness_data.csv", "fitness_data.json"]:
        run_pipeline(file)
