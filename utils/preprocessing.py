import re
import pandas as pd
import json
import os
from nltk.stem import SnowballStemmer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_stopwords() -> list:
    """Load stopwords from file.

    Returns: List of stopwords.

    """
    with open(os.path.join(BASE_DIR, "no_stopwords.json"), encoding="utf-8") as file:
        stopwords = json.load(file)

    return stopwords


def remove_stopwords(dataframe, column_name, stopwords) -> pd.DataFrame:
    """Remove stopwords from dataframe.

    Args:
        dataframe: Dataframe to clean.
        column_name: Column name to clean.
        stopwords: List of stopwords.

    Returns: Cleaned dataframe.

    """
    dataframe[column_name] = dataframe[column_name].apply(lambda x: " ".join(
        [word for word in x.split() if word not in stopwords]))
    return dataframe


def remove_punctuation(dataframe, column_name) -> pd.DataFrame:
    """Remove punctuations from dataframe.

        Args:
            dataframe: Dataframe to clean.
            column_name: Column name to clean.

    Returns: Cleaned dataframe.
    """

    def clean(text):
        text = text.replace("\n", " ")
        text = re.sub(r'[^a-zæøå]+', ' ', text)
        text = re.sub(r'\s+', ' ', text)  # remove extra spaces
        return text

    dataframe[column_name] = dataframe[column_name].apply(lambda x: clean(x))
    return dataframe


def convert_to_lowercase(dataframe, column_name) -> pd.DataFrame:
    """Convert text to lowercase.

        Args:
            dataframe: Dataframe to clean.
            column_name: Column name to clean.

    Returns: Cleaned dataframe.

    """
    dataframe[column_name] = dataframe[column_name].apply(lambda x: x.lower())
    return dataframe


def stem_words(dataframe, column_name) -> pd.DataFrame:
    """Stem words from dataframe.

        Args:
            dataframe: Dataframe to clean.
            column_name: Column name to clean.

    Returns: Cleaned dataframe.

    """

    stemmer = SnowballStemmer("norwegian", ignore_stopwords=False)
    dataframe[column_name] = dataframe[column_name].apply(lambda x: " ".join(
        [stemmer.stem(word) for word in x.split()]))
    return dataframe


def clean_text(dataframe, column_name) -> pd.DataFrame:
    """ Clean text from dataframe.

        Args:
            dataframe: Dataframe to clean.
            column_name: Column name to clean.

    Returns: Cleaned dataframe.

    """
    stopwords = load_stopwords()
    dataframe = convert_to_lowercase(dataframe, column_name)
    dataframe = remove_punctuation(dataframe, column_name)
    dataframe = remove_stopwords(dataframe, column_name, stopwords)
    dataframe = stem_words(dataframe, column_name)
    return dataframe
