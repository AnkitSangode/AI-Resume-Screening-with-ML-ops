import pickle
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from resumeScreening.entity import ModelTrainerConfig
from resumeScreening import logger

class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config
        self.X_train = pickle.load(open(self.config.X_train_path, "rb"))
        self.y_train = np.load(self.config.y_train_path)
        self.X_test = pickle.load(open(self.config.X_test_path, "rb"))
        self.y_test = np.load(self.config.y_test_path)

    def train_model(self,model,param_grid,name):
        logger.info(f"Training: {name}")
        grid = GridSearchCV(model,param_grid,cv=5,n_jobs=-1,verbose=1)
        grid.fit(self.X_train,self.y_train)
        best_model = grid.best_estimator_
        logger.info(f"Best model is {best_model}")


         # Save the best model
        with open(f"{self.config.root_dir}/{name.lower().replace(' ', '_')}.pkl", "wb") as f:
            pickle.dump(best_model, f)

    def train_all(self):
        self.train_model(
            LogisticRegression(max_iter=1000),
            self.config.params.logistic_regression,
            "LogisticRegression"
        )

        self.train_model(
            RandomForestClassifier(),
            self.config.params.random_forest,
            "RandomForestClassifier"
        )

        self.train_model(
            SVC(),
            self.config.params.svm,
            "SVM"
        )
