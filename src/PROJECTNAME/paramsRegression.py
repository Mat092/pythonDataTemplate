#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File for storing dictionaries of hyper-parameters for classification to be used in Randomized Cross
Validation or Nested cross validations with pipelines.
"""

import numpy as np

# Parameters to be used with pipeline and randomized search CV for Regressions

SCORES = [
    "r2",
    "neg_mean_squared_error",
    "neg_mean_absolute_error",
]

LM_PARAMS = (
    {
        "model__alpha": np.random.uniform(0, 100, 100),
    },
)

SGD_PARAMS = (
    {
        "model__loss": ["squared_loss", "huber", "epsilon_insensitive"],
        "model__penalty": ["l2", "l1", "elasticnet"],
        "model__alpha": np.random.uniform(0.001, 10, 100),
        "model__l1_ratio": np.random.uniform(0, 1, 100),
    },
)

SVR_PARAMS = {
    "model__kernel": ["poly", "rbf", "sigmoid"],
    "model__degree": np.random.randint(0, 10, 100),
    "model__gamma": ["scale", "auto"],
    "model__C": np.random.uniform(0, 10, 100),
}

RF_PARAMS = (
    {
        "model__criterion": ["squared_error", "absolute_error", "poisson"],
        "model__max_features": [1.0, "sqrt", "log2"],
        "model__bootstrap": [True, False],
        "model__max_depth": np.random.randint(1, 15, 100),
        "model__min_samples_leaf": np.random.randint(1, 15, 100),
        "model__min_samples_split": np.random.randint(2, 15, 100),
    },
)

ADB_PARAMS = (
    {
        "model__n_estimators": np.random.randint(1, 100, 100),
        "model__loss": ["linear", "square", "exponential"],
        "model__learning_rate": np.random.exponential(scale=1.0, size=100),
    },
)

XGB_PARAMS = {
    "model__learning_rate": np.random.uniform(0, 1, 100),
    "model__gamma": [0, 0.01, 1, 10, 100, 200, 1000],
    "model__max_depth": np.arange(3, 20, 1),
    "model__alpha": np.random.uniform(0, 100, 1000),
    "model__lambda": np.random.uniform(0, 100, 1000),
}

if __name__ == "__main__":
    pass
