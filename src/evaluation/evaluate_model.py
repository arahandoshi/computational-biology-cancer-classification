from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from src.models.logistic_regression_model import train_logistic_regression


def evaluate_logistic_regression():

    (
        model,
        predictions,
        X_test,
        y_test,
        label_encoder,
        scaler,
        gene_variances
    ) = train_logistic_regression()

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions,
        target_names=label_encoder.classes_
    )

    print("\n========== MODEL PERFORMANCE ==========\n")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\n========== CONFUSION MATRIX ==========\n")
    print(matrix)

    print("\n========== CLASSIFICATION REPORT ==========\n")
    print(report)


if __name__ == "__main__":
    evaluate_logistic_regression()