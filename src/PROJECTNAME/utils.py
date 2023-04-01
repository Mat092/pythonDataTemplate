#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
List of data utility functions useful for handling data with pandas and numpy
"""

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.preprocessing import StandardScaler


def stdize_dataframe(
    df: pd.DataFrame, to_stdize: list[str] = None
) -> tuple(pd.DataFrame, StandardScaler):
    """Standardize a pandas DataFrame with a sklearn StandardScaler keeping the original structure of the dataframe

    Parameters
    ----------
    df : pandas DataFrame
    to_stdize : list of str.
        columns of the dataframe to standardize

    Returns
    -------
    DataFrame
        Standardized pandas DataFrame
    """

    scaled = df.copy()
    scaler = StandardScaler().fit(scaled[to_stdize])
    scaled[to_stdize] = scaler.transform(scaled[to_stdize])

    return scaled, scaler


CORR_METHODS = {"spearman": spearmanr, "pearson": pearsonr}


def get_correlations(
    df, target: str, drops: list[str] = [], method: str = "spearman"
) -> tuple[np.array, np.array, np.array]:
    """Compute correlations with target columns and order the results from highest to lowest"""
    features = df.drop(columns=[target] + drops).columns

    corrs = []

    for col in features:
        corrs.append(CORR_METHODS[method](df[col], df[target])[0])

    # Order from highest to lowest the 3 arrays
    idx = np.argsort(corrs)[::-1]
    labels = features.to_numpy()[idx]
    ydata = np.sort(corrs)[::-1]
    xdata = np.arange(0, len(features))

    return labels, xdata, ydata


if __name__ == "__main__":
    pass
