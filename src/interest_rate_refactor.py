#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename, encoding='SHIFT_JIS', header=2, index_col=0)

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(['系列名称'], axis=0)
    df = df.drop(['単位'], axis=0)
    df = df.drop(['データコード'], axis=0)
    df = df.drop(['収録開始期'], axis=0)
    df = df.drop(['収録終了期'], axis=0)
    df = df.drop(['最終更新日'], axis=0)
    return df

def display_fig_save(df: pd.DataFrame, figurename: str) -> None:
    plt.figure(figsize = (12,6))
    plt.plot(df["基準貸付利率（月次）"].astype(float))
    plt.savefig(figurename)

def main():
    filename = "data/input/interest_rate1.csv"
    figurename = "data/output/Japanese_interest_rate_transition2.png"
    df = load(filename)
    df = preprocess(df)
    display_fig_save(df,figurename)

if __name__=='__main__':
    main()

