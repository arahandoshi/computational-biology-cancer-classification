import os
import pandas as pd

# Ensure folders exist (safe even if already created)
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/metadata", exist_ok=True)

# -----------------------------
# TCGA Pan-Cancer Expression Data (TOIL)
# -----------------------------
expression_url = "https://toil.xenahubs.net/download/TcgaTargetGtex_rsem_gene_tpm.gz"

print("Downloading gene expression dataset...")

expr_df = pd.read_csv(
    expression_url,
    sep="\t",
    compression="gzip",
    index_col=0
)

print("Expression shape:", expr_df.shape)

# Save locally (so we don’t re-download every time)
expr_df.to_csv("data/raw/gene_expression.tsv.gz", sep="\t", compression="gzip")

print("Saved gene expression matrix to data/raw/")