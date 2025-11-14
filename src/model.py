"""
Model utilities:
- Option 1: Use Hugging Face pipeline with a pre-finetuned model (quick inference)
- Option 2: Load a locally fine-tuned model (after running train.py)
"""
import os
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
import logging
load_dotenv()

LOGGER = logging.getLogger(__name__)

def load_pipeline(use_local: bool = False, local_path: str = "./models/distilbert-finetuned-tweets"):
    """
    If use_local is True and the local_path exists, load that model.
    Otherwise, load a reliable HF model fine-tuned for sentiment.
    """
    if use_local and os.path.isdir(local_path):
        LOGGER.info(f"Loading local model from {local_path}")
        tokenizer = AutoTokenizer.from_pretrained(local_path)
        model = AutoModelForSequenceClassification.from_pretrained(local_path)
        nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        return nlp

    # Default: use DistilBERT finetuned on SST-2 for general sentiment
    LOGGER.info("Loading remote model 'distilbert-base-uncased-finetuned-sst-2-english'")
    nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return nlp
