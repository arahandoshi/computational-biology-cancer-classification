import pandas as pd


def variance_filter(expression_df, threshold=None):
    """
    Remove genes with low variance.

    Parameters
    ----------
    expression_df : pandas.DataFrame
        Gene expression matrix.

    threshold : float
        Variance threshold. If None, median variance is used.

    Returns
    -------
    filtered_df : pandas.DataFrame
        Expression matrix after removing low-variance genes.

    gene_variances : pandas.Series
        Variance of every gene.
    """

    gene_variances = expression_df.var()

    if threshold is None:
        threshold = gene_variances.median()

    selected_genes = gene_variances[
        gene_variances > threshold
    ].index

    filtered_df = expression_df[selected_genes]

    return filtered_df, gene_variances