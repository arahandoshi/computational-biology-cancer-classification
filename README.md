# Multi-Cancer Classification Using TCGA-Derived RNA-Seq Gene Expression Data

## Overview

This repository presents a complete computational biology pipeline for multi-class cancer classification using TCGA-derived RNA sequencing (RNA-Seq) gene expression data.

The project demonstrates the complete workflow required to build reproducible machine learning models for transcriptomic cancer classification, including data preprocessing, exploratory data analysis, feature engineering, classical machine learning, deep learning, and comparative model evaluation.

The study emphasizes reproducibility, modular software design, and transparent computational analysis while comparing multiple predictive models on the same transcriptomic feature set. The repository is organized as a notebook-based research workflow in which each stage of the analysis is documented independently.

Rather than focusing solely on predictive accuracy, the project also evaluates computational efficiency, model complexity, and practical suitability for high-dimensional transcriptomic classification tasks.

---

## Objectives

The primary objectives of this project are:

* Develop a fully reproducible computational biology workflow for transcriptomic cancer classification.
* Perform exploratory analysis of high-dimensional RNA-Seq gene expression data.
* Construct a feature engineering pipeline to reduce dimensionality while preserving predictive information.
* Implement and evaluate multiple classical machine learning algorithms, including Logistic Regression, Random Forest, and Support Vector Machine.
* Develop and evaluate a deep learning classifier using TensorFlow/Keras.
* Compare model performance using predictive accuracy, training time, and confusion matrices.
* Demonstrate an end-to-end workflow suitable for computational biology and bioinformatics research.

---

## Repository Structure

```text
computational-biology-cancer-classification/

├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
│   ├── 01_Dataset_Understanding.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Machine_Learning.ipynb
│   ├── 06_Deep_Learning.ipynb
│   └── 07_Model_Comparison.ipynb
├── results/
│   └── figures/
├── src/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Computational Workflow

The computational pipeline implemented in this repository consists of the following stages:

1. Dataset acquisition and organization
2. Data preprocessing and quality assessment
3. Exploratory transcriptomic data analysis
4. Feature engineering and dimensionality reduction
5. Classical machine learning model development
6. Deep learning model development
7. Model evaluation using classification metrics
8. Comparative analysis of predictive models

---

## Models Implemented

### Classical Machine Learning Models

* Logistic Regression
* Random Forest
* Support Vector Machine (Linear Kernel)

### Deep Learning Model

* Feedforward Artificial Neural Network (TensorFlow/Keras)

---

## Results Summary

All evaluated models achieved excellent predictive performance on the selected transcriptomic feature set.

| Model                     | Accuracy | Purpose                              |
| ------------------------- | -------- | ------------------------------------ |
| Logistic Regression       | 100%     | Interpretable baseline model         |
| Random Forest             | 100%     | Ensemble learning approach           |
| Support Vector Machine    | 100%     | Computationally efficient classifier |
| Artificial Neural Network | 100%     | Deep learning benchmark              |

Comparative evaluation demonstrated that the selected transcriptomic features possess strong discriminative capability across multiple cancer classes.

The project also compares model training time, predictive performance, and practical suitability for transcriptomic classification tasks.

---

## Technologies Used

### Programming Language

* Python

### Data Analysis

* NumPy
* Pandas

### Visualization

* Matplotlib

### Machine Learning

* Scikit-learn

### Deep Learning

* TensorFlow
* Keras

---

## Reproducibility

All analyses are implemented in Jupyter notebooks with a modular structure.

The repository includes:

* Raw and processed datasets
* Feature engineering workflow
* Machine learning notebooks
* Deep learning implementation
* Comparative evaluation
* Figures and exported results

This structure enables complete reproducibility of the computational pipeline.

---

## Future Work

Potential future extensions include:

* External validation using independent transcriptomic datasets
* Multi-omics integration
* Explainable artificial intelligence approaches
* Biological interpretation of selected transcriptomic features
* Clinical translation studies

---

## Author

Arahan Atulya Doshi

B.Tech Biotechnology and Bioinformatics
D.Y. Patil School of Biotechnology and Bioinformatics
Navi Mumbai, India

---

