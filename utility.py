import numpy as np


def rolling_corr(data, window):
    start = 0
    corr_series = np.empty([data.shape[0]-window, data.shape[1], data.shape[1]])
    while start+window < data.shape[0]:
        data_window = data.iloc[start:start+window]
        corr_series[start, :, :] = np.corrcoef(data_window, rowvar=0)
        start += 1
    return corr_series

# data_window.div(data_window.iloc[0])
