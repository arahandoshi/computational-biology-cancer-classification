# Data Preprocessing

## Overview

Before training machine learning and deep learning models, the raw gene expression data must be transformed into a format suitable for analysis. This project implements a reproducible preprocessing pipeline that prepares the dataset while maintaining a clear separation between raw data, processed data, and model development.

The preprocessing pipeline is implemented in:

```text
src/data/preprocess.py
```

---

## Preprocessing Workflow

The preprocessing pipeline consists of the following stages:

1. Load the raw gene expression dataset.
2. Load the corresponding cancer class labels.
3. Apply variance-based feature selection.
4. Encode categorical cancer labels into numerical values.
5. Split the dataset into training and testing subsets.
6. Return model-ready datasets for downstream analysis.

---

## Data Loading

The pipeline begins by loading the processed RNA-Seq gene expression matrix and cancer labels from the project's data directory.

```text
data/
└── raw/
    ├── data.csv
    └── labels.csv
```

The gene expression matrix contains numerical expression values, while the label file stores the corresponding cancer type for each patient sample.

---

## Feature Selection

Before model development, variance-based feature selection is applied to reduce the dimensionality of the dataset.

Genes with very low variance across patients contribute limited discriminatory information and may increase computational complexity without improving predictive performance.

Applying variance filtering reduced the dataset from:

- **20,531 genes**
- to **10,265 genes**

This step decreases noise while retaining the most informative features for classification.

---

## Label Encoding

Machine learning algorithms require numerical target labels rather than text categories.

The project uses Scikit-learn's `LabelEncoder` to convert cancer type names into integer labels.

Example:

| Cancer Type | Encoded Label |
|-------------|---------------|
| Cancer A | 0 |
| Cancer B | 1 |
| Cancer C | 2 |
| ... | ... |

The fitted encoder is retained so predictions can later be converted back to their original cancer class names.

---

## Train-Test Split

The processed dataset is divided into training and testing subsets using an **80:20 split**.

| Dataset | Samples |
|----------|---------|
| Training Set | **640** |
| Testing Set | **161** |

The split is performed using Scikit-learn's `train_test_split()` function with:

- `test_size = 0.2`
- `random_state = 42`
- `stratify = encoded_labels`

Using stratification ensures that each cancer class maintains approximately the same proportion in both the training and testing datasets.

The fixed random state ensures that the split is reproducible across multiple executions.

---

## Output

The preprocessing pipeline returns:

- Training feature matrix (`X_train`)
- Testing feature matrix (`X_test`)
- Training labels (`y_train`)
- Testing labels (`y_test`)
- Fitted label encoder
- Gene variance statistics

These outputs are used throughout the subsequent stages of model development and evaluation.

---

## Summary

The preprocessing pipeline transforms the raw gene expression dataset into a reproducible, model-ready format by combining feature selection, label encoding, and stratified train-test splitting. This standardized workflow ensures consistency across all machine learning and deep learning experiments conducted in this project.