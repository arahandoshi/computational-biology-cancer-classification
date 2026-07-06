import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.features.feature_selection import variance_filter


def load_and_preprocess_data():
    """
    Load the raw TCGA dataset and preprocess it.

    Returns
    -------
    X_train : pandas.DataFrame
    X_test : pandas.DataFrame
    y_train : numpy.ndarray
    y_test : numpy.ndarray
    label_encoder : LabelEncoder
    gene_variances : pandas.Series
    """

    # Load gene expression data
    expression_df = pd.read_csv(
        "data/raw/data.csv",
        index_col=0
    )

    # Load cancer labels
    labels_df = pd.read_csv(
        "data/raw/labels.csv"
    )

    # Apply variance filtering
    filtered_expression_df, gene_variances = variance_filter(
        expression_df
    )

    # Encode cancer labels into numbers
    label_encoder = LabelEncoder()

    encoded_labels = label_encoder.fit_transform(
        labels_df["Class"]
    )

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        filtered_expression_df,
        encoded_labels,
        test_size=0.2,
        random_state=42,
        stratify=encoded_labels
    )

    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    return (
        X_train,
        X_test,
        y_train,
        y_test,
        label_encoder,
        scaler,
        gene_variances
    )


if __name__ == "__main__":

    X_train, X_test, y_train, y_test, label_encoder, scaler, gene_variances = load_and_preprocess_data()

    print("Training samples:", X_train.shape)
    print("Testing samples:", X_test.shape)

    print("Training labels:", len(y_train))
    print("Testing labels:", len(y_test))