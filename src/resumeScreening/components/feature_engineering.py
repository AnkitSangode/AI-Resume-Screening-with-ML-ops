import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from resumeScreening import logger
from pathlib import Path
from resumeScreening.config.configuration import FeatureEngineeringConfig

class FeatureEngineering:
    def __init__(self, config: FeatureEngineeringConfig):
        self.config = config

    def run(self):
        logger.info("Reading train and test data...")
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        X_train_texts = train_df["Cleaned_Resume"]
        y_train_labels = train_df["Category"]
        X_test_texts = test_df["Cleaned_Resume"]
        y_test_labels = test_df["Category"]

         # === ML: TF-IDF ===
        logger.info("Fitting TF-IDF Vectorizer...")
        tfidf = TfidfVectorizer(max_features=3000)
        X_train_tfidf = tfidf.fit_transform(X_train_texts)
        X_test_tfidf = tfidf.transform(X_test_texts)

         # Save TF-IDF vectorizer

        with open(Path(self.config.root_dir)/'vectorizer.pkl','wb') as f:
            pickle.dump(tfidf,f)

        # === Label Encoding ===
        logger.info("Encoding labels...")
        label_encoder = LabelEncoder()
        y_train_encoded = label_encoder.fit_transform(y_train_labels)
        y_test_encoded = label_encoder.transform(y_test_labels)

        #Save label encoder
        with open(Path(self.config.root_dir)/'labelEncoder.pkl','wb') as f:
            pickle.dump(label_encoder,f)

         # Save ML features
        with open(Path(self.config.root_dir) / "X_train_tfidf.pkl", "wb") as f:
            pickle.dump(X_train_tfidf, f)
        with open(Path(self.config.root_dir) / "X_test_tfidf.pkl", "wb") as f:
            pickle.dump(X_test_tfidf, f)
        np.save(Path(self.config.root_dir )/ "y_train_ml.npy", y_train_encoded)
        np.save(Path(self.config.root_dir) / "y_test_ml.npy", y_test_encoded)

        # === DL: Tokenizer + Padding ===
        logger.info("Fitting tokenizer for DL...")
        tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
        tokenizer.fit_on_texts(X_train_texts)

        X_train_seq = tokenizer.texts_to_sequences(X_train_texts)
        X_test_seq = tokenizer.texts_to_sequences(X_test_texts)

        X_train_pad = pad_sequences(X_train_seq, maxlen=300)
        X_test_pad = pad_sequences(X_test_seq, maxlen=300)

        y_train_dl = to_categorical(y_train_encoded)
        y_test_dl = to_categorical(y_test_encoded)

        # Save DL features
        with open(Path(self.config.root_dir )/ "tokenizer.pkl", "wb") as f:
            pickle.dump(tokenizer, f)
        np.save(Path(self.config.root_dir)/ "X_train_pad.npy", X_train_pad)
        np.save(Path(self.config.root_dir)/ "X_test_pad.npy", X_test_pad)
        np.save(Path(self.config.root_dir)/ "y_train_dl.npy", y_train_dl)
        np.save(Path(self.config.root_dir)/ "y_test_dl.npy", y_test_dl)

        logger.info("[✓] Feature engineering completed and files saved.")