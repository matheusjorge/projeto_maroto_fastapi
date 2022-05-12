from data_collect import data_collect
from evaluation import evaluate
from modeling import modeling
from preprocessing import preprocessing

if __name__ == "__main__":
    # Coleta de dados
    df = data_collect()

    # Preprocessamento
    X_train, X_test, y_train, y_test = preprocessing(df)

    # Modelagem
    gnb, lr = modeling(X_train, y_train)

    # Avaliação
    acc, f1 = evaluate(gnb, X_test, y_test)
    print(f"Naive Bayes: acc = {acc:.3} / f1 = {f1:.3}")

    acc, f1 = evaluate(lr, X_test, y_test)
    print(f"Logistic Regression: acc = {acc:.3} / f1 = {f1:.3}")
