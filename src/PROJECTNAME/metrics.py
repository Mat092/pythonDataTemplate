#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from patsy import dmatrices
from scipy.stats import pearsonr
from statsmodels.stats.outliers_influence import variance_inflation_factor


def r2(true, pred) -> float:
    ss_res = np.sum((true - pred) ** 2)
    ss_tot = np.sum((true - true.mean()) ** 2)
    return 1 - (ss_res / ss_tot)


def adj_r2(true, pred, n: int, p: int) -> float:
    num = (1 - r2(true, pred)) * (n - 1)
    den = n - p - 1
    return 1 - (num / den)


def mse(true, pred) -> float:
    return np.square(true - pred).mean()


def rmse(true, pred) -> float:
    return np.sqrt(mse(true, pred))


def mae(true, pred) -> float:
    return np.abs(true - pred).mean()


def mape(true, pred) -> float:
    return np.abs((true - pred) / true).mean() * 100


def rho(true, pred):
    return pearsonr(true, pred)[0]


def rho_c(true, pred):
    num = 2 * rho(true, pred) * true.std() * pred.std()
    den = true.var() + pred.var() + np.square(true.mean() - pred.mean())
    return num / den


def VIF(df: pd.DataFrame) -> pd.DataFrame:
    """Compute the Variance Inflation Factor (VIF) for a given dataframe

    Parameters
    ----------
    df : pandas DataFrame
        pandas DataFrame with the data

    Returns
    -------
    DataFrame
        pandas Dataframe with the VIF for each variable in the formula
    """
    VIF = pd.DataFrame(
        {
            name: variance_inflation_factor(df.values, i)
            for i, name in enumerate(df.columns)
            if name != "Intercept"
        }.items(),
        columns=["Variable", "VIF"],
    )

    return VIF


if __name__ == "__main__":
    pass
