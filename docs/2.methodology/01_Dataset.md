# Dataset

## Overview

This project uses a publicly available **TCGA-derived RNA-Seq gene expression dataset** obtained from the UCSC Xena data repository. The dataset contains processed gene expression measurements for multiple cancer types and serves as the primary data source for model development.

Rather than processing raw sequencing reads, the project utilizes preprocessed transcriptomic data, allowing the focus to remain on computational analysis, feature engineering, machine learning, and deep learning.

---

## Dataset Source

**Repository:** UCSC Xena

**Dataset Type:** TCGA-derived RNA-Seq Gene Expression Data

**Data Format:** Processed gene expression matrix with corresponding cancer class labels

The dataset has been curated and preprocessed for downstream computational analysis, making it suitable for supervised machine learning workflows.

---

## Dataset Characteristics

| Characteristic | Value |
|----------------|-------|
| Patient Samples | **801** |
| Gene Expression Features | **20,531** |
| Cancer Types | **5** |
| Data Type | RNA-Seq Gene Expression |
| Learning Task | Multi-class Classification |

Each row represents an individual patient sample, while each column corresponds to the expression level of a specific gene.

---

## Why This Dataset?

This dataset was selected because it offers several advantages for computational cancer classification:

- Derived from The Cancer Genome Atlas (TCGA), one of the largest publicly available cancer genomics initiatives.
- Contains genome-wide RNA-Seq gene expression measurements.
- Includes multiple cancer classes suitable for supervised classification.
- Publicly available and widely used in computational biology research.
- Well-suited for demonstrating preprocessing, feature engineering, and predictive modeling techniques.

These characteristics make it an appropriate dataset for developing and evaluating machine learning and deep learning models.

---

## Data Organization

The project stores the dataset in the following structure:

```text
data/
├── raw/
│   ├── data.csv
│   └── labels.csv
```

- `data.csv` contains the gene expression matrix.
- `labels.csv` contains the corresponding cancer class labels.

This separation improves clarity and simplifies preprocessing.

---

## External Validation Dataset

In addition to the primary TCGA-derived dataset, this project will evaluate the final model using an **independent public gene expression dataset**.

The external dataset will not be used during model training or development. Instead, it will be reserved exclusively for final validation to assess the model's ability to generalize beyond the primary dataset.

This validation strategy follows best practices in computational biology by evaluating model performance across independent datasets rather than relying solely on a single train-test split.

---

## Dataset Limitations

Although the dataset is well suited for computational analysis, several limitations should be acknowledged:

- The project uses processed expression data rather than raw sequencing reads.
- Only transcriptomic (gene expression) data is considered; other omics data are not included.
- The dataset represents a limited number of cancer types.
- Biological variability and dataset-specific characteristics may influence model performance.

These limitations are addressed, in part, through external validation on an independent public dataset.

---

## Summary

The TCGA-derived RNA-Seq gene expression dataset provides a high-dimensional transcriptomic representation of multiple cancer types, making it an appropriate foundation for developing and evaluating computational models for cancer classification. Combined with independent external validation, it supports the development of a reproducible and scientifically rigorous computational biology pipeline.