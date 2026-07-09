from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from src.models.random_forest_model import train_random_forest


def evaluate():

    (
        model,
        predictions,
        X_test,
        y_test,
        label_encoder,
    ) = train_random_forest()

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

    print("\n========== RANDOM FOREST PERFORMANCE ==========\n")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\n========== CONFUSION MATRIX ==========\n")

    print(confusion_matrix(y_test, predictions))

    print("\n========== CLASSIFICATION REPORT ==========\n")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_
        )
    )


if __name__ == "__main__":
    evaluate()