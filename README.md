Twitter Sentiment Analysis using BERT & Streamlit
This project implements an end-to-end sentiment analysis system that:

Fetches tweets from Twitter using the API

Cleans and preprocesses text data

Classifies sentiment using a HuggingFace Transformer model (DistilBERT)

Visualizes results in an interactive Streamlit web application

It demonstrates skills in NLP, API integration, and web deployment.

Features
Tweet Fetching: Retrieve recent tweets with specific keywords using Tweepy.

Text Cleaning: Remove URLs, mentions, hashtags, punctuation, emojis, and stopwords.

Sentiment Classification: Classify tweets as positive, neutral, or negative using DistilBERT.

Visualization: Display sentiment distribution using Matplotlib bar charts.

Interactive Web App: Streamlit interface for real-time sentiment analysis.

Modular Code: Structured project for easy maintenance and scalability.

Technology Stack
Model: DistilBERT (HuggingFace Transformers)

Text Preprocessing: NLTK, Regex

Visualization: Matplotlib

Web App: Streamlit

Data Fetching: Tweepy (Twitter API v2)

Environment Management: python-dotenv

Project Structure
graphql
Copy code
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
Environment Variables
Create a .env file in the project root:

ini
Copy code
BEARER_TOKEN=your_twitter_bearer_token
Do not upload .env to GitHub.

Use .env.example as a template for contributors.

Installation & Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add .env file:

bash
Copy code
cp .env.example .env
Fill in your Twitter API bearer token.

Running the Streamlit App
Run the app:

bash
Copy code
streamlit run app.py
Open in browser at:

arduino
Copy code
http://localhost:8501
How the Model Works
Tweets are fetched from Twitter API using a keyword.

Text is cleaned (removing URLs, mentions, hashtags, punctuation, stopwords, emojis).

Cleaned text is passed to DistilBERT sentiment analysis pipeline.

Each tweet is classified as positive, neutral, or negative.

Results are visualized using Matplotlib and displayed in Streamlit.

Future Improvements
Fine-tune BERT on custom Twitter dataset for higher accuracy.

Support for non-English tweets.

Deploy the app on HuggingFace Spaces or Heroku.

Add a database to track sentiment trends over time.

Implement batch tweet analysis for large datasets.
