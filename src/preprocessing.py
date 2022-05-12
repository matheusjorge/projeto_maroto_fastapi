import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def preprocessing(df):
    # Dividir datdos
    df_train, df_test = train_test_split(df, test_size=0.1, stratify=df["OPINIAO"])

    # Criar vetorizador
    tf_idf = TfidfVectorizer(
        encoding="latin-1",
        strip_accents='ascii',
        lowercase=True, 
        min_df= 0.01,
        ngram_range=(1,3),
    )

    # Fit
    X_train = np.array(tf_idf.fit_transform(df_train["tweet"]).todense())
    X_test = np.array(tf_idf.transform(df_test["tweet"]).todense())

    # Salvar vetorizador
    with open("../models/tfidf.pkl", "wb") as file:
        pickle.dump(obj=tf_idf, file=file)


    y_train = df_train["OPINIAO"]
    y_test = df_test["OPINIAO"]

    return X_train, X_test, y_train, y_test
