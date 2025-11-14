import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_distribution(df, label_col='predicted_label'):
    counts = df[label_col].value_counts()
    ax = counts.plot(kind='bar')
    ax.set_title("Sentiment distribution")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.show()

def wordcloud_for_label(df, label, label_col='predicted_label', text_col='clean_text'):
    text = " ".join(df[df[label_col]==label][text_col].astype(str).tolist())
    if not text:
        print(f"No text for {label} to generate wordcloud.")
        return
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"WordCloud for {label}")
    plt.show()
