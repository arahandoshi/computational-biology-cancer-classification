import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

expression_df = pd.read_csv(
    "data/raw/data.csv",
    index_col=0
)

labels_df = pd.read_csv(
    "data/raw/labels.csv"
)

print("Expression dataset shape:")
print(expression_df.shape)

print("\nLabels dataset shape:")
print(labels_df.shape)

print("\nExpression Data")
print(expression_df.head())

print("\nLabels")
print(labels_df.head())

print("\nExpression columns:")
print(expression_df.columns)

print("\nLabel columns:")
print(labels_df.columns)

print("\nMissing values in expression data:")
print(expression_df.isnull().sum().sum())

print("\nMissing values in labels:")
print(labels_df.isnull().sum().sum())

print("\nUnique cancer types:")
print(labels_df["Class"].unique())

print("\nNumber of cancer types:")
print(labels_df["Class"].nunique())

print("\nPatients per cancer type:")
print(labels_df["Class"].value_counts())

