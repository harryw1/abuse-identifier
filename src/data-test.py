
def main():
    import pandas as pd

    df = pd.read_parquet("hf://datasets/tdavidson/hate_speech_offensive/data/train-00000-of-00001.parquet")

    print(df.head())

if __name__ == "__main__":
    main()
