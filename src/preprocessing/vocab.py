"""Module for building vocabulary."""

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize


def build_vocab(df: pd.DataFrame, column: str) -> set:
    """Builds a vocabulary from a DataFrame column.

    Args:
        df (pd.DataFrame): The DataFrame containing the text data.
        column (str): The name of the column containing the text data.

    Returns:
        set: The vocabulary built from the text data.
    """
    nltk.download('punkt_tab')
    vocab = set()
    for text in df[column]:
        tokens = word_tokenize(text)
        vocab.update(tokens)
    return vocab
