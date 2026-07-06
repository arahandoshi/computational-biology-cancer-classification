# Feature Engineering

## Overview

Feature engineering is the process of transforming raw data into a representation that improves model performance while reducing unnecessary complexity. In this project, feature engineering focuses on identifying the most informative genes before model development.

The feature engineering pipeline is implemented in:

```text
src/features/feature_selection.py
```

---

## Objective

The primary objective of feature engineering is to reduce the dimensionality of the gene expression dataset while preserving genes that contribute meaningful information for cancer classification.

Reducing the number of input features improves computational efficiency, decreases noise, and helps reduce the risk of overfitting.

---

## Variance-Based Feature Selection

The first feature engineering technique applied in this project is **variance-based feature selection**.

For each gene, the variance of its expression values was calculated across all patient samples. Genes exhibiting higher variance show greater differences in expression between patients and are therefore more likely to contain useful discriminatory information for classification.

Genes with very low variance were removed because they provide limited information for distinguishing cancer types.

---

## Feature Reduction

Applying variance-based feature selection reduced the dimensionality of the dataset by approximately 50%.

| Stage | Number of Features |
|--------|-------------------:|
| Original Gene Features | **20,531** |
| Selected Gene Features | **10,265** |

This reduction decreases computational requirements while retaining genes with greater expression variability.

---

## Rationale

Variance filtering was selected because it is:

- Simple to implement.
- Computationally efficient.
- Independent of class labels, preventing information leakage.
- Well suited as an initial feature reduction technique for high-dimensional transcriptomic datasets.

The filtered dataset provides a more manageable feature space for downstream machine learning and deep learning models.

---

## Current Feature Engineering Pipeline

The current pipeline consists of:

1. Load gene expression data.
2. Calculate variance for every gene.
3. Rank genes based on variance.
4. Remove low-variance genes.
5. Pass the reduced feature matrix to the preprocessing pipeline.

---

## Future Enhancements

As the project progresses, additional feature engineering techniques may be evaluated, including:

- Feature scaling and normalization where required.
- Model-based feature importance analysis.
- Recursive feature elimination.
- Dimensionality reduction techniques for visualization and comparison.

These techniques will be investigated only if they provide measurable improvements over the current variance-based approach.

---

## Outcome

Variance-based feature selection successfully reduced the feature space from **20,531** to **10,265** genes while preserving highly variable genes that are more likely to contribute to accurate cancer classification. The resulting feature matrix serves as the input for all subsequent machine learning and deep learning experiments.