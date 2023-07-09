import numpy as np
import rsfs
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, roc_auc_score, f1_score
from sklearn.model_selection import train_test_split, cross_val_score


def rotation_forest(data, labels, k, n_features, n_estimators):
    """
    Performs rotation forest on the given data using RSFS and random forest as the base classifier.

    Args:
        data: The data to be classified.
        labels: The labels of the data.
        k: The number of subsets to be used.
        n_features: The number of features to be used for each subset.
        n_estimators: The number of base classifiers to be used.

    Returns:
        The predictions of the rotation forest.
    """
    Parameters = {
        'RSFS': {
            'Classifier': 'KNN',
            'Classifier Properties': {
                'n_neighbors': 3,
                'weights': 'distance'
            },
            'Dummy feats': 100,
            'delta': 0.05,
            'maxiters': 300000,
            'fn': 'sqrt',

            'cutoff': 0.99,
            'Threshold': 1000,
        },
        'Verbose': 1
    }
    ensemble_predictions = []
    for _ in range(n_estimators):
        rf = RandomForestClassifier(max_features=n_features)
        data_train, data_test, label_train, label_test = train_test_split(
            data, labels, test_size=0.33, random_state=42, stratify=labels)
        c_matrices = []
        for i in range(k):
            subset = rsfs.RSFS(data_train, label_train, data_train, label_train, Parameters)
            c_matrix = np.corrcoef(subset)
            c_matrices.append(c_matrix)
        rotation_matrix = np.mean(c_matrices, axis=0)
        rotate_train = np.dot(data_train, rotation_matrix)
        rf.fit(rotate_train, label_train)
        predictions = rf.predict(data_test)
        ensemble_predictions.append(predictions)
    majority_vote_predictions = np.mean(ensemble_predictions, axis=0)
    return majority_vote_predictions


if __name__ == "__main__":
    data = np.loadtxt(open('data3.csv', "rb"), delimiter=",", skiprows=1)
    labels = data[:, -1]
    data = data[:, :-1]
    scoring_metrics = [
        'accuracy',
        'precision',
        'recall',
        make_scorer(f1_score),  # F-measure
        make_scorer(roc_auc_score)  # AUC
    ]
    fixed_params = {
        'k': 5,
        'n_features': 5,
        'n_estimators': 10
    }
    scores = cross_val_score(rotation_forest, data, labels, scoring=scoring_metrics, cv=10, **fixed_params)
    for metric, score in zip(scoring_metrics, scores):
        print(f"{metric}: {score}")
