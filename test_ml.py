import pytest
# TODO: add necessary import
import pandas as pd
from ml.data import process_data
from ml.model import train_model
from ml.model import inference
from ml.model import compute_model_metrics
#from ml.model import
import numpy as np 
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.ensemble import RandomForestClassifier


# TODO: implement the first test. Change the function name and input as needed
# test_one function test wheather every categorical function was encode

@pytest.fixture
def sample_df():
    """Small stable dataset with both categorical and continuous features."""
    return pd.DataFrame({
        "workclass": ["Private", "Self-emp", "Private", "Federal-gov"],
        "education": ["Bachelors", "HS-grad", "Masters", "Some-college"],
        "age": [25, 45, 35, 50],
        "salary": ["<=50K", ">50K", "<=50K", ">50K"],   # label column
    })
@pytest.fixture
def categorical_features():
    return ["workclass", "education"]


@pytest.fixture
def label():
    return "salary"


"""def test_categorical_encoding(sample_df, categorical_features, label):
    
    # add description for the first test
    X, _, encoder, _ = process_data(data, categorical_features, label, training=True)
    encoded_features = encoder.get_feature_names_out()

    for feature in categorical_features:
        assert any(name.startswith(feature + "_") for name in encoded_features), \
            f"Feature '{feature}' was not encoded."
   
    _, _, encoder, _ = process_data(
        sample_df, categorical_features, label, training=True
    )

    encoded_feature_names = encoder.get_feature_names_out()

    for feature in categorical_features:
        assert any(name.startswith(feature + "_") for name in encoded_feature_names), \
            f"Categorical feature '{feature}' was not encoded properly."
"""
# Teat Model training returns a valid model object
def test_train_model_returns_correct_type(sample_df, categorical_features, label):

    """
    Ensure that train_model() returns a trained sklearn model.
    Expected: sklearn.linear_model.LogisticRegression
    """
    X_train, y_train, encoder, lb = process_data(
        sample_df, categorical_features, label, training=True
    )

    model = train_model(X_train, y_train)

    # Check that model has the expected "predict" method
    assert hasattr(model, "predict"), "Trained model does not have predict() method."
    assert hasattr(model, "predict_proba"), "Trained model does not have predict_proba()."

    


# TODO: implement the second test. Change the function name and input as needed
#def test_two():
# Test compute_model_metrics returns expected numeric types
def test_compute_metrics_output_type(sample_df, categorical_features, label):
    """
    The Matrix must return float for precision, recall, F-beta
    """
    X_train, y_train, encoder, lb = process_data(
        sample_df, categorical_features, label, training=True
    )

    model = train_model(X_train, y_train)
    preds = inference(model, X_train)

    precision, recall, fbeta = compute_model_metrics(y_train, preds)

    assert isinstance(precision, float), "Precision should be float."
    assert isinstance(recall, float), "Recall should be float."
    assert isinstance(fbeta, float), "F-beta should be float."


# TODO: implement the third test. Change the function name and input as needed
#def test_three():
    """
    # add description for the third test
    """
def test_categorical_encoding(sample_df, categorical_features, label):
    """
    Test that all categorical features are one-hot encoded.
    Ensures encoder.feature_names_out() contains categories for every feature.
    """
    _, _, encoder, _ = process_data(
        sample_df, categorical_features, label, training=True
    )

    encoded_feature_names = encoder.get_feature_names_out()

    for feature in categorical_features:
        assert any(name.startswith(feature + "_") for name in encoded_feature_names), \
            f"Categorical feature '{feature}' was not encoded properly."
