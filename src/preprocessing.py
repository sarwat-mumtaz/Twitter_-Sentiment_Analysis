"""
Robust tweet cleaning:
- Lowercase
- Convert emojis to text (emoji.demojize)
- Remove urls, mentions, hashtags symbols (keep hashtag words)
- Expand contractions (small set)
- Remove punctuation except keep word tokens
- Remove stopwords
- Simple negation handling (keeps 'not' + word)
"""
import re
from typing import Optional
import emoji
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)

STOPWORDS = set(stopwords.words('english'))

CONTRACTIONS = {
    "can't": "cannot",
    "won't": "will not",
    "don't": "do not",
    "i'm": "i am",
    "it's": "it is",
    "i've": "i have",
    "you're": "you are",
    "we're": "we are",
    "they're": "they are",
    "that's": "that is",
    "what's": "what is",
    "there's": "there is",
}

URL_PATTERN = re.compile(r"http\S+|www\.\S+")
MENTION_PATTERN = re.compile(r"@\w+")
HASHTAG_SYMBOL = re.compile(r"#")  # remove symbol only
NON_ALPHANUM = re.compile(r"[^a-zA-Z0-9\s:]")  # keep colon from emoji demojize

def expand_contractions(text: str) -> str:
    for k, v in CONTRACTIONS.items():
        text = re.sub(r'\b' + re.escape(k) + r'\b', v, text)
    return text

def emoji_to_words(text: str) -> str:
    # demoji style: :smiling_face:
    return emoji.demojize(text, language='en')

def clean_tweet(text: str, remove_stopwords: bool = True) -> str:
    if not isinstance(text, str):
        return ""
    # 1. emoji -> :grinning_face:
    text = emoji_to_words(text)
    # 2. lowercase
    text = text.lower()
    # 3. expand contractions
    text = expand_contractions(text)
    # 4. remove URLs and mentions
    text = URL_PATTERN.sub('', text)
    text = MENTION_PATTERN.sub('', text)
    # 5. remove hashtag symbol only
    text = HASHTAG_SYMBOL.sub('', text)
    # 6. remove unwanted characters (keep emoji colons and alnum)
    text = NON_ALPHANUM.sub(' ', text)
    # 7. tokenize and remove stopwords (but keep negations like 'not')
    tokens = text.split()
    if remove_stopwords:
        tokens = [t for t in tokens if (t not in STOPWORDS) or (t == 'not')]
    cleaned = ' '.join(tokens).strip()
    return cleaned
