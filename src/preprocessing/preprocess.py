"""Main entry point for preprocessing."""

def main():
    # Use a relative path with os.path for better portability
    import os
    from pathlib import Path

    from src.preprocessing.ingestion import parquet_ingest, read_datapath
    from src.preprocessing.vocab import build_vocab

    # Get the project root directory
    # This assumes ingestion.py is in src/preprocessing/
    project_root = Path(__file__).parent.parent.parent

    # Path to the datapath file using relative path from project root
    datapath_file = os.path.join(project_root, "mutables", "hf-datapath.txt")

    # Read the HuggingFace dataset path from the file
    hf_path = read_datapath(datapath_file)

    # Ingest the data using the path from the file
    df = parquet_ingest(hf_path)
    print(f"Successfully loaded data from {hf_path}")
    print(f"DataFrame columns: {df.columns}")
    print(f"DataFrame shape: {df.shape}")

    # Build a vocabulary from the text data
    vocab = build_vocab(df, "tweet")
    print(vocab)

if __name__ == "__main__":
    main()
