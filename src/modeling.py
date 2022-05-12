import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

def modeling(X_train, y_train):
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)

    with open("../models/gnb.pkl", "wb") as file:
        pickle.dump(obj=gnb, file=file)

    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    with open("../models/lr.pkl", "wb") as file:
        pickle.dump(obj=lr, file=file)

    return gnb, lr