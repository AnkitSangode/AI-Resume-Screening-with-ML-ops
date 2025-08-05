import os
from box.exceptions import BoxValueError
import yaml
from resumeScreening import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()



def clean_resume(text:str) -> str:
    """
    Cleans the input resume text by removing URLs, special characters,
    numbers, and converting to lowercase.
    """
    text = re.sub(r"http\S+", " ", text)  # remove URLs
    text = re.sub(r"RT|cc", " ", text)  # remove retweets
    text = re.sub(r"#\S+", "", text)  # remove hashtags
    text = re.sub(r"@\S+", " ", text)  # remove mentions
    text = re.sub(r"[%s]" % re.escape("""!"$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""), " ", text)  # punctuation
    text = re.sub(r"[^\x00-\x7f]", r" ", text)  # non-ASCII chars
    text = re.sub(r"\s+", " ", text)  # extra spaces
    text = re.sub(r"\d+", "", text)  # remove numbers
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 2]
    return " ".join(tokens)


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list , verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path)as f:
       content =  json.load(f)
    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content)

def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read()) 
    
