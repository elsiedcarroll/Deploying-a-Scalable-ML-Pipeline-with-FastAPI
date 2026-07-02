import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import math
from ml.model import train_model, compute_model_metrics

# TODO: implement the first test. Change the function name and input as needed
def test_proper_split():
    """
    Check if the data is properly split into training and testing sets.
    """
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)

    train, test = train_test_split(
        data,
        test_size=0.2,
        random_state=42,
        stratify=data['salary']
    )

    assert not train.empty, "Training dataset is empty."
    assert not test.empty, "Test dataset is empty."
    assert math.isclose(len(test) / len(data), 0.2, rel_tol=0.01), f"Test dataset to precision: {len(test) / len(data):.4f}"


# TODO: implement the second test. Change the function name and input as needed
def test_proper_classifier():
    """
    Makes sure that train_model() returns a RandomForestClassifier.
    """
    x = [[1], [2], [3], [4]]
    y = [1, 0, 1, 0]
    model = train_model(x, y)

    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier."


# TODO: implement the third test. Change the function name and input as needed
def test_metrics():
    """
    Tests that compute_model_metrics returns correct values
    """
    y_true = np.array([1,0,1,0])
    y_pred = np.array([1,0,1,0])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert recall == 1.0, "recall is incorrect"
    assert precision == 1.0, "precision is incorrect"
    assert fbeta == 1.0, "fbeta is incorrect"
