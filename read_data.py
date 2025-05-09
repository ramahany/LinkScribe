import pandas as pd
import numpy as np


def get_data(file_path, na=None):
    return pd.read_excel(file_path, na_values=na)
