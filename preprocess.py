import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources safely
@nltk.download('stopwords', quiet=True)
@nltk.download('wordnet', quiet=True)
@nltk.download('omw-1.4', quiet=True)
def download_nltk_resources():
    pass

download_nltk_resources()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)

    words = text.split()

    tokens = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalpha() and word not in stop_words
    ]

    return tokens

