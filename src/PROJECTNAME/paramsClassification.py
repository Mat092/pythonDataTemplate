#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
File for storing dictionaries of hyper-parameters for classification to be used in Randomized Cross
Validation or Nested cross validations.
"""

import numpy as np

from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

from xgboost import XGBClassifier

# To be used with RandomizedSearchCV for Classification

SCORES = [
    "roc_auc",
    "recall",
    "precision",
    "f1_weighted",
    "accuracy",
    "neg_log_loss",
]

LM_PARAMS = (
    {
        "alpha": np.linspace(0, 10, 100),
    },
)

SGD_PARAMS = (
    {
        "loss": ["squared_loss", "huber", "epsilon_insensitive"],
        "penalty": ["l2", "l1", "elasticnet"],
        "alpha": np.linspace(0.001, 10, 100),
        "l1_ratio": np.linspace(0, 1, 100),
    },
)

SVR_PARAMS = {
    "kernel": ["poly", "rbf", "sigmoid"],
    "degree": np.random.randint(0, 10, 100),
    "gamma": ["scale", "auto"],
    "C": np.random.uniform(0, 10, 100),
}

RF_PARAMS = (
    {
        "criterion": ["gini", "entropy"],
        "max_features": ["auto", "sqrt", "log2"],
        "class_weight": ["balanced"],
        "bootstrap": [True, False],
        "max_depth": np.random.randint(1, 15, 100),
        "min_samples_leaf": np.random.randint(1, 15, 100),
        "min_samples_split": np.random.randint(2, 15, 100),
    },
)

ADB_PARAMS = (
    {
        "loss": ["linear", "square", "exponential"],
        "learning_rate": np.power(10.0, -np.random.randint(1, 10, 100)),
    },
)

XGB_PARAMS = {
    "n_estimators": [],
    "max_depth": [],
    "learning_rate": [],
    "reg_alpha": [],
    "reg_lambda": [],
}

MODELS_PARAMS = {
    RidgeClassifier(): LM_PARAMS,
    SGDClassifier(): SGD_PARAMS,
    SVC(): SVR_PARAMS,
    RandomForestClassifier(): RF_PARAMS,
    AdaBoostClassifier(): ADB_PARAMS,
    XGBClassifier(): XGB_PARAMS,
}


if __name__ == "__main__":
    pass
