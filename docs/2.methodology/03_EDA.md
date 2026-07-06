# Exploratory Data Analysis (EDA)

## Overview

Exploratory Data Analysis (EDA) was performed to understand the structure, quality, and statistical characteristics of the gene expression dataset before feature engineering and model development.

The analysis was implemented in:

```text
notebooks/03_EDA.ipynb
```

EDA provides an initial understanding of the dataset and helps identify important characteristics that influence downstream machine learning and deep learning models.

---

## Objectives

The primary objectives of EDA were to:

- Verify dataset dimensions.
- Inspect the distribution of gene expression values.
- Summarize statistical properties of the dataset.
- Measure variability across genes.
- Identify informative genes for feature selection.
- Establish a foundation for subsequent preprocessing steps.

---

## Dataset Inspection

The dataset consists of:

| Property | Value |
|----------|-------|
| Patient Samples | **801** |
| Gene Expression Features | **20,531** |
| Cancer Classes | **5** |

Each row represents an individual patient sample, while each column represents the expression level of a single gene.

---

## Statistical Summary

Descriptive statistics were calculated for the variance of all genes to understand the overall distribution of feature variability.

The summary included:

- Mean
- Standard deviation
- Minimum
- Quartiles
- Maximum

These statistics provided a quantitative overview of how gene expression variability is distributed across the dataset.

---

## Gene Expression Distribution

To visualize the overall distribution of gene expression values, all non-zero expression values were combined into a single array and displayed using a histogram.

The histogram illustrates:

- The concentration of low-expression genes.
- The presence of highly expressed genes.
- The overall spread of transcriptomic measurements.

**Figure 1. Distribution of Gene Expression Values Across All Tumor Samples**

*(Insert histogram generated in `03_EDA.ipynb`.)*

---

## Gene Variance Analysis

The variance of each gene was calculated across all patient samples.

Genes exhibiting higher variance demonstrate greater expression differences between patients and are generally more informative for classification tasks.

The analysis identified the most variable genes within the dataset, providing the basis for subsequent variance-based feature selection.

---

## Feature Reduction

Based on the variance analysis, genes with low variability were removed.

| Stage | Number of Genes |
|--------|----------------:|
| Original Features | **20,531** |
| After Variance Filtering | **10,265** |

This reduced the dimensionality of the dataset by approximately **50%**, decreasing computational complexity while retaining the most informative features.

---

## Key Findings

The exploratory analysis revealed several important characteristics:

- The dataset contains a high-dimensional gene expression matrix.
- Gene expression values are unevenly distributed, with many low-expression observations.
- A relatively small subset of genes exhibits high variability across patients.
- Variance-based filtering substantially reduces the number of features while preserving informative genes.
- The processed dataset is suitable for downstream machine learning and deep learning applications.

---

## Outcome

The EDA confirmed that the dataset is appropriate for computational cancer classification and provided the statistical foundation for feature engineering and preprocessing. The insights obtained during this stage directly informed the variance-based feature selection strategy adopted in the project.