import pandas as pd
import pickle
from sklearn.metrics import accuracy_score,classification_report
import mlflow
import mlflow.sklearn
from resumeScreening import logger
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
import json
import mlflow.keras
from pathlib import Path
from resumeScreening.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        #load test data
        test_df = pd.read_csv(self.config.test_data_path)
        X_test_text = test_df['Cleaned_Resume']
        y_test_labels = test_df['Category']

        #Load label encoder and vectorizer
        with open(self.config.label_encoder_path,'rb') as f:
            label_encoder = pickle.load(f)

        y_test_encoded = label_encoder.transform(y_test_labels)

        with open(self.config.vectorizer_path,'rb') as f:
            vectorizer = pickle.load(f)

        X_test_vectorized = vectorizer.transform(X_test_text)

        #Evaluate ML Models
        evaluation_results = {}

        for name, path in self.config.ml_model_path.items():
            with open(path,'rb') as f:
                model = pickle.load(f)

            y_pred = model.predict(X_test_vectorized)
            acc = accuracy_score(y_test_encoded, y_pred)
            cr = classification_report(y_test_encoded,y_pred,target_names=label_encoder.classes_)
            logger.info(f"{name} Accuracy: {acc}")
            logger.info(f"Classifcation report: {cr}")

            with mlflow.start_run(run_name=f"{name}_eval"):
                # mlflow.log_param("model_type", "ML")
                # mlflow.log_metric("accuracy", acc)
                # mlflow.sklearn.log_model(model, name)

            # Store metrics for saving later
                evaluation_results[name] = {
                    "accuracy": acc,
                    "classification_report": cr
                }

    #Deep learning

        # Load vectorizer used during training
        with open(self.config.vectorizer_path, "rb") as f:
            vectorizer = pickle.load(f)

        X_test_vectorized = vectorizer.transform(X_test_text)
        X_test_dl = X_test_vectorized.toarray().astype("float32")

# Load trained DL model
        deep_model = load_model(self.config.dl_model_path)

        # Confirm shapes match
        assert deep_model.input_shape[1] == X_test_dl.shape[1], \
            f"Shape mismatch: Model expects {deep_model.input_shape[1]}, but got {X_test_dl.shape[1]}"

        # Prediction
        y_pred_probs = deep_model.predict(X_test_dl)
        y_pred_dl = y_pred_probs.argmax(axis=1)

        # Evaluation
        acc_dl = accuracy_score(y_test_encoded, y_pred_dl)
        cr_dl = classification_report(y_test_encoded, y_pred_dl, target_names=label_encoder.classes_)

        with mlflow.start_run(run_name="DL_eval"):
            # mlflow.log_param("model_type", "DL")
            # mlflow.log_metric("accuracy", acc_dl)
            # mlflow.keras.log_model(deep_model, "DeepModel")

            evaluation_results["deep_learning"] = {
                "accuracy": acc_dl,
                "classification_report": cr_dl
            }

        # Save evaluation results JSON
        eval_path = Path(self.config.evaluation_json_path)
        eval_path.parent.mkdir(parents=True, exist_ok=True)

        with open(eval_path, "w") as f:
            json.dump(evaluation_results, f, indent=4)

        logger.info(f"Saved evaluation results to {eval_path}")

    
            