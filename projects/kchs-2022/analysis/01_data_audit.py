"""
KCHS 2022 — Step 1: Data ingestion and automated audit.

This script deliberately does not modify source files.
Place authorised KNBS files under projects/kchs-2022/data/raw/.

Supported formats:
- CSV
- Excel (.xlsx, .xls)
- Stata (.dta)
- SPSS (.sav)

Outputs are written to projects/kchs-2022/outputs/audit/.
"""

from pathlib import Path
import json
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUT_DIR = ROOT / "outputs" / "audit"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SUPPORTED = {".csv", ".xlsx", ".xls", ".dta", ".sav"}


def clean_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_").lower()


def read_file(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(path, low_memory=False)

    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)

    if suffix == ".dta":
        return pd.read_stata(path)

    if suffix == ".sav":
        return pd.read_spss(path)

    raise ValueError(f"Unsupported file type: {path}")


def audit_dataframe(df: pd.DataFrame) -> dict:
    missing = df.isna().sum()
    missing_pct = (missing / len(df) * 100).round(2) if len(df) else missing

    numeric = df.select_dtypes(include="number")

    numeric_summary = {}
    for col in numeric.columns:
        series = numeric[col].dropna()
        if len(series):
            numeric_summary[col] = {
                "min": float(series.min()),
                "max": float(series.max()),
                "mean": float(series.mean()),
                "median": float(series.median()),
            }

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "columns_with_missing_values": int((missing > 0).sum()),
        "columns": [
            {
                "name": col,
                "dtype": str(df[col].dtype),
                "missing": int(missing[col]),
                "missing_pct": float(missing_pct[col]),
                "unique_values": int(df[col].nunique(dropna=True)),
            }
            for col in df.columns
        ],
        "numeric_summary": numeric_summary,
    }


def main() -> None:
    if not RAW_DIR.exists():
        raise FileNotFoundError(
            f"Raw-data directory not found: {RAW_DIR}. "
            "Create it and place authorised KCHS files there."
        )

    files = sorted(
        path for path in RAW_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED
    )

    if not files:
        raise FileNotFoundError(
            "No supported data files found in data/raw/. "
            "Download the authorised KCHS 2022 files from KNBS first."
        )

    manifest = []

    for path in files:
        print(f"Auditing: {path.name}")
        df = read_file(path)

        result = audit_dataframe(df)
        result["file"] = path.name
        result["relative_path"] = str(path.relative_to(ROOT))

        manifest.append(result)

        # Save a compact variable-level audit.
        variables = pd.DataFrame(result["columns"])
        variables.to_csv(
            OUT_DIR / f"{clean_name(path.stem)}_variables.csv",
            index=False,
        )

    with open(OUT_DIR / "data_audit.json", "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)

    overview = pd.DataFrame(
        [
            {
                "file": item["file"],
                "rows": item["rows"],
                "columns": item["columns"],
                "duplicate_rows": item["duplicate_rows"],
                "missing_cells": item["missing_cells"],
                "columns_with_missing_values": item["columns_with_missing_values"],
            }
            for item in manifest
        ]
    )

    overview.to_csv(OUT_DIR / "file_overview.csv", index=False)

    print("\nAudit complete.")
    print(overview.to_string(index=False))


if __name__ == "__main__":
    main()
