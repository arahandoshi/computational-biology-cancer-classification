# Biological Background

## Introduction

Cancer is a group of diseases characterized by uncontrolled cell growth resulting from genetic and molecular alterations. While cancers may originate from different tissues, they exhibit distinct patterns of gene activity that can be measured and analyzed computationally.

Advances in high-throughput sequencing technologies have enabled researchers to study these molecular differences at the transcriptomic level, making gene expression analysis an important tool in modern cancer research.

---

## Gene Expression and Cancer

Gene expression refers to the process by which genetic information is transcribed into RNA, reflecting the activity of genes within a cell. Unlike DNA, which remains largely constant across cells, gene expression varies depending on cell type, biological function, and disease state.

Cancer cells often activate or suppress specific genes that regulate processes such as cell division, apoptosis, metabolism, and immune response. These altered expression patterns create molecular signatures that differ between cancer types.

As a result, gene expression profiles can be used to distinguish cancers based on their underlying biology rather than solely on their tissue of origin.

---

## RNA Sequencing

RNA sequencing (RNA-Seq) is a high-throughput technology used to quantify gene expression across the entire genome. The output is a matrix of numerical expression values, where each row represents a patient sample and each column represents a gene.

Such datasets contain thousands of measured genes simultaneously, providing a comprehensive representation of cellular activity and making RNA-Seq one of the most informative data sources for computational cancer classification.

---

## Why Gene Expression for Cancer Classification?

Gene expression data is particularly well suited for machine learning because it captures the functional state of cells. Different cancer types exhibit characteristic transcriptional profiles that can be learned by computational models to identify complex biological patterns.

Compared with traditional diagnostic methods that rely primarily on histopathology or imaging, transcriptomic analysis enables classification using genome-wide molecular information, offering opportunities for improved precision and biological insight.

---

## Relevance to This Project

This project uses a publicly available TCGA-derived RNA-Seq gene expression dataset containing five cancer types. The biological objective is not to discover new biomarkers but to develop a computational pipeline capable of learning cancer-specific expression patterns and accurately classifying previously unseen patient samples.

The project further strengthens its biological relevance by validating the trained model on an independent public gene expression dataset, allowing assessment of whether the learned molecular patterns generalize beyond the original training data.