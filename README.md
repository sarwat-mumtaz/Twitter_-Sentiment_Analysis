# Twitter Sentiment Analysis using DistilBERT & Streamlit
An end-to-end sentiment analysis system that fetches tweets from Twitter, analyzes sentiment using DistilBERT, and displays results in an interactive Streamlit web application.

## Overview

This project implements an end-to-end sentiment analysis system that:

* **Fetches tweets** from Twitter using the API  
* **Cleans and preprocesses** text data  
* **Classifies sentiment** using a HuggingFace Transformer model (DistilBERT)  
* **Visualizes results** in an interactive Streamlit web application  

It demonstrates skills in **NLP**, **API integration**, and **web deployment**.

---

## Features

* **Tweet Fetching**: Retrieve recent tweets with specific keywords using Tweepy
* **Text Cleaning**: Remove URLs, mentions, hashtags, punctuation, emojis, and stopwords
* **Sentiment Classification**: Classify tweets as `positive`, `neutral`, or `negative` using DistilBERT
* **Visualization**: Display sentiment distribution using Matplotlib bar charts
* **Interactive Web App**: Streamlit interface for real-time sentiment analysis
* **Modular Code**: Structured project for easy maintenance and scalability

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| **Model** | DistilBERT (HuggingFace Transformers) |
| **Text Preprocessing** | NLTK, Regex |
| **Visualization** | Matplotlib |
| **Web App** | Streamlit |
| **Data Fetching** | Tweepy (Twitter API v2) |
| **Environment Management** | python-dotenv |

---

## Project Structure

```
twitter-sentiment-analysis/
│
├── app.py                     # Streamlit user interface
├── notebook.ipynb             # Data exploration and model testing
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Files to ignore in GitHub
├── .env.example               # Template for API keys
│
├── src/
│   ├── preprocessing.py       # Text cleaning functions
│   ├── model.py               # HuggingFace pipeline and prediction functions
│   ├── twitter_api.py         # Fetching tweets from Twitter API
│   ├── visualize.py           # Functions to visualize sentiment
│   └── utils.py               # Helper functions
│
├── models/                    # Optional: saved custom models
├── data/
│   ├── raw/                   # Raw tweets CSV
│   └── processed/             # Cleaned tweets CSV
├── images/                    # Screenshots for README or reports
└── logs/                      # Optional: app logs
```

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Twitter Developer Account ([Sign up here](https://developer.twitter.com/))
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then edit `.env` and add your Twitter API bearer token:

```env
BEARER_TOKEN=your_twitter_bearer_token
```

**Important**: Do not upload `.env` to GitHub. It's already included in `.gitignore`.

---

## Environment Variables

### Getting Your Twitter Bearer Token

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new Project and App
3. Navigate to **"Keys and tokens"** tab
4. Generate and copy your **Bearer Token**
5. Paste it in your `.env` file

### `.env.example` Template

```env
BEARER_TOKEN=your_twitter_bearer_token
```

Use this as a template for contributors.

---

## Usage

### Running the Streamlit App

1. **Start the application:**

```bash
streamlit run app.py
```

2. **Open in browser:**

The app will automatically open at:
```
http://localhost:8501
```

3. **Use the interface:**
   - Enter a keyword or hashtag (e.g., "artificial intelligence", "#AI")
   - Choose number of tweets to analyze (10-100)
   - Click "Analyze Sentiment"
   - View results and visualizations

### Using Individual Modules

#### Fetch Tweets

```python
from src.twitter_api import fetch_tweets

tweets = fetch_tweets(query="machine learning", max_results=50)
```

#### Preprocess Text

```python
from src.preprocessing import clean_tweet

cleaned = clean_tweet("Check this out! @user #AI https://example.com")
# Output: "check"
```

#### Predict Sentiment

```python
from src.model import predict_sentiment

result = predict_sentiment("I love this product!")
# Output: {'label': 'positive', 'score': 0.9876}
```

#### Visualize Results

```python
from src.visualize import plot_sentiment_distribution

plot_sentiment_distribution(sentiments)
```

---

## How It Works

### Pipeline Overview

```
1. User Input (Keyword)
         ↓
2. Fetch Tweets (Twitter API)
         ↓
3. Text Cleaning
   - Remove URLs, mentions, hashtags
   - Remove punctuation, emojis
   - Remove stopwords
         ↓
4. Sentiment Analysis (DistilBERT)
   - Classify as positive/neutral/negative
   - Calculate confidence scores
         ↓
5. Visualization (Matplotlib)
   - Bar charts
   - Distribution plots
         ↓
6. Display Results (Streamlit)
```

### Text Preprocessing Steps

1. **Remove URLs**: `https://t.co/xyz` → ` `
2. **Remove Mentions**: `@username` → ` `
3. **Remove Hashtags**: `#AI` → `AI`
4. **Remove Punctuation**: `Hello!!!` → `Hello`
5. **Remove Emojis**: emojis → ` `
6. **Remove Stopwords**: `the, is, at, which` → ` `
7. **Lowercase**: `HELLO` → `hello`

### Sentiment Classification

- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Classes**: 
  - **Positive** (score > 0.6)
  - **Neutral** (score 0.4-0.6)
  - **Negative** (score < 0.4)
- **Confidence**: 0-100% for each prediction

---

## Example Output

### Sample Tweets Analysis

| Tweet | Cleaned Text | Sentiment | Confidence |
|-------|--------------|-----------|-----------|
| "I love this product!" | "love product" | Positive | 94.2% |
| "Worst experience ever @company" | "worst experience ever" | Negative | 91.7% |
| "It's okay, nothing special" | "okay nothing special" | Neutral | 78.5% |

### Sentiment Distribution

```
Positive: 45.2% (226 tweets)
Neutral:  28.4% (142 tweets)
Negative: 26.4% (132 tweets)
```

---

## Future Improvements

* Fine-tune BERT on custom Twitter dataset for higher accuracy
* Support for non-English tweets (multilingual models)
* Deploy the app on HuggingFace Spaces or Heroku
* Add a database to track sentiment trends over time
* Implement batch tweet analysis for large datasets
* Add emotion detection (joy, anger, fear, sadness)
* Real-time streaming analysis
* Export results to CSV/JSON
* Add user authentication
* Dark mode for Streamlit interface

---

