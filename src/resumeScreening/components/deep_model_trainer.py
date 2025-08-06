import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from resumeScreening import logger
import os


class DeepModelTrainer:
    def __init__(self, config):
        self.config = config
        self.X_train = np.load(self.config.X_train_path)
        self.y_train = np.load(self.config.y_train_path)
        self.X_test = np.load(self.config.X_test_path)
        self.y_test = np.load(self.config.y_test_path)

    def build_model(self):
        layers = self.config.params.model.layers
        dropout = self.config.params.model.dropout
        activation = self.config.params.model.activation
        output_activation = self.config.params.model.output_activation

        model = Sequential()
        model.add(Dense(layers[0], activation=activation, input_shape=(self.X_train.shape[1],)))
        model.add(Dropout(dropout))

        for units in layers[1:]:
            model.add(Dense(units, activation=activation))
            model.add(Dropout(dropout))

        model.add(Dense(self.y_train.shape[1], activation=output_activation))

        compile_cfg = self.config.params.compile

        model.compile(
            loss=compile_cfg.loss,
            optimizer=compile_cfg.optimizer,
            metrics=compile_cfg.metrics
        )

        return model

    def train_and_save(self):
        model = self.build_model()

        history = model.fit(
            self.X_train,
            self.y_train,
            epochs=self.config.params.training.epochs,
            batch_size=self.config.params.training.batch_size,
            validation_data=(self.X_test, self.y_test)
        )

        model_path = os.path.join(self.config.root_dir, "deep_model.h5")
        model.save(model_path)
        logger.info(f"Model saved to {model_path}")
