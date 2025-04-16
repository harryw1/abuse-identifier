"""Module for data ingestion."""

import pandas as pd


def parquet_ingest(file_path: str) -> pd.DataFrame:
    """Ingest data from a HuggingFace parquet into a pandas DataFrame.

    Args:
        file_path (str): Remote HuggingFace parquet path.

    Returns:
        pd.DataFrame: DataFrame containing the ingested data.
    """
    return pd.read_parquet(file_path)

def read_datapath(datapath_file: str) -> str:
    """Read the remote HuggingFace dataset path from a file.

    Args:
        datapath_file (str): Path to the file containing the HuggingFace dataset path.

    Returns:
        str: The HuggingFace dataset path.
    """
    with open(datapath_file, 'r') as f:
        return f.read().strip()

def main():
    # Use a relative path with os.path for better portability
    import os
    from pathlib import Path

    # Get the project root directory
    # This assumes ingestion.py is in src/preprocessing/
    project_root = Path(__file__).parent.parent.parent

    # Path to the datapath file using relative path from project root
    datapath_file = os.path.join(project_root, "mutables", "hf-datapath.data")

    # Read the HuggingFace dataset path from the file
    hf_path = read_datapath(datapath_file)

    # Ingest the data using the path from the file
    df = parquet_ingest(hf_path)
    print(f"Successfully loaded data from {hf_path}")
    print(f"DataFrame columns: {df.columns}")
    print(f"DataFrame shape: {df.shape}")

if __name__ == "__main__":
    main()
