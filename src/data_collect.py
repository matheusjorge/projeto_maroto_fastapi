import os
import pandas as pd
import requests
import zipfile

def data_collect():
    # Collect data from url
    dataset_url = "https://sites.google.com/site/miningbrgroup/home/resources/consumer_sentiment_analysis_corpus.zip?attredirects=0&d=1"
    response = requests.get(dataset_url)

    # Create temp dir
    os.makedirs("../data/tmp")

    # Save zip to disk    
    with open("../data/tmp/consumer_sentiment_analysis_corpus.zip", "wb") as f:
        f.write(response.content)

    # Uncompress zip file
    with zipfile.ZipFile("../data/tmp/consumer_sentiment_analysis_corpus.zip", 'r') as zip_ref:
        zip_ref.extractall("../data/tmp/")

    # Read data
    df = pd.read_csv("../data/tmp/unbalanced_corpus/corpus_two_class_unbalanced/tweets-total-csv-2-class-unbalanced.csv", encoding="latin-1", sep=";")

    # Save data to disk
    df.to_csv("../data/raw_data.csv")

    return df

if __name__ == "__main__":
    data_collect()

    