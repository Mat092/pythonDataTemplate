#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import platform
from pathlib import Path

import plotly.io as pio
import seaborn as sns

# Used to differentiate datapath in different OS
dir_dict = {
    "Windows": "OneDrive - Alma Mater Studiorum Università di Bologna",
    "Darwin": "OneDrive - Alma Mater Studiorum Università di Bologna",
    "Linux": "OneDrive",
}

ROOT = Path(__file__).parent.parent.parent.absolute()

DATA_DIR = Path.home() / dir_dict[platform.system()] / "path" / "to" / "data_dir"
IMG_DIR = Path.home() / dir_dict[platform.system()] / "path" / "to" / "img_dir"

# Logs basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# My favourite settings for plotting. When importing something from this file, it will be automatically applied
sns.set_theme(
    style="ticks",
    context="paper",
    font="serif",
    palette="deep",
    font_scale=2.0,
    rc={
        "figure.figsize": (7, 5),
        "axes.labelsize": 15,
        "axes.grid": True,
    },
)

# Plotly settings
pio.templates.default = "simple_white"


if __name__ == "__main__":
    pass
