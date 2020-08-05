import pandas as pd 
import tensorflow as tf
import tensorflow.keras.backend as K
import transformers
from transformers import TFCamemBERT
from transformers import TFBertTokenizer

# Defining some key variables that will be used later on in the training

MAX_LEN = 2000
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 32
EPOCHS = 1
LEARNING_RATE = 1e-05
tokenizer = CamembertTokenizer.from_pretrained('camembert-base-cased')

def build_model():
    config = 
    
    
