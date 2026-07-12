from src.models.random_forest_model import train_random_forest
from src.evaluation.evaluate import evaluate_model


def main():

    (
        model,
        predictions,
        X_test,
        y_test,
        label_encoder,
    ) = train_random_forest()

    evaluate_model(
        model_name="Random Forest",
        y_true=y_test,
        predictions=predictions,
        label_encoder=label_encoder,
    )


if __name__ == "__main__":
    main()