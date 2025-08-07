from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class FeatureEngineeringConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: str
    X_train_path: str
    y_train_path: str
    X_test_path: str
    y_test_path: str
    params: dict

@dataclass(frozen=True)
class DeepModelTrainerConfig:
    root_dir: str
    X_train_path: str
    y_train_path: str
    X_test_path: str
    y_test_path: str
    params: dict

@dataclass(frozen=True)
class ModelEvaluationConfig:
    test_data_path : Path
    label_encoder_path: Path
    vectorizer_path: Path
    ml_model_path: dict
    dl_model_path: Path
    evaluation_json_path: Path