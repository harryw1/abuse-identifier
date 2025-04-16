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
