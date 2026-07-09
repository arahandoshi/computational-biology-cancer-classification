from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


def evaluate_model(
    model_name,
    y_true,
    predictions,
    label_encoder,
):

    accuracy = accuracy_score(y_true, predictions)

    precision = precision_score(
        y_true,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_true,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_true,
        predictions,
        average="weighted"
    )

    print(f"\n========== {model_name.upper()} ==========\n")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\n========== CONFUSION MATRIX ==========\n")

    print(confusion_matrix(y_true, predictions))

    print("\n========== CLASSIFICATION REPORT ==========\n")

    print(
        classification_report(
            y_true,
            predictions,
            target_names=label_encoder.classes_
        )
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }