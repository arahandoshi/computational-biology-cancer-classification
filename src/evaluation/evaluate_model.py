from src.models.logistic_regression_model import train_logistic_regression
from src.evaluation.evaluate import evaluate_model


def main():

    (
        model,
        predictions,
        X_test,
        y_test,
        label_encoder,
    ) = train_logistic_regression()

    evaluate_model(
        model_name="Logistic Regression",
        y_true=y_test,
        predictions=predictions,
        label_encoder=label_encoder,
    )


if __name__ == "__main__":
    main()