import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import FreqDist
import string

nltk.download("punkt")
nltk.download("stopwords")

desired_num = 9

input_paragraph = """
   Once upon a time, in a quiet little village, there was a small bakery with a big secret. The baker, named Emma, had a magical touch. Everything she baked turned into something special.

One sunny morning, a little girl named Lily visited the bakery. She chose a plain-looking cookie and took a bite. To her surprise, it tasted like her favorite ice cream.

Lily told her friends, and soon the bakery became famous. People came from far and wide to taste Emma's magical treats. Each bite brought a smile to their faces.

Emma's bakery wasn't just a place for delicious pastries; it was a place where ordinary moments turned into extraordinary memories. And so, in the heart of the village, Emma's bakery shared the sweetest magic of all—the magic of happiness.
    """

# Tokenize the paragraph into sentences
sentences = nltk.sent_tokenize(input_paragraph)

# Remove stop words
stop_words = set(stopwords.words("english"))


# Create a function to compute sentence similarity using cosine similarity
def sentence_similarity(sent1, sent2):
    sent1 = [word for word in word_tokenize(sent1.lower()) if word not in stop_words]
    sent2 = [word for word in word_tokenize(sent2.lower()) if word not in stop_words]
    words = list(set(sent1 + sent2))
    vector1 = [1 if word in sent1 else 0 for word in words]
    vector2 = [1 if word in sent2 else 0 for word in words]

    return 1 - cosine_similarity([vector1], [vector2])[0][0]


def get_keywords():
    # Create a similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(
                    sentences[i], sentences[j]
                )

    # Use PageRank to rank the sentences
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)

    # Get the most important sentence
    summary_sentence = sentences[max(scores, key=scores.get)]

    # Tokenize the summary sentence
    words = word_tokenize(summary_sentence.lower())

    # Remove punctuation and stop words
    filtered_words = [
        word
        for word in words
        if word not in string.punctuation and word not in stop_words
    ]

    # Use NLTK's FreqDist to find the most common words
    fdist = FreqDist(filtered_words)

    # Get the most common words as keywords
    keywords = [
        word for word, freq in fdist.most_common(desired_num)
    ]  # You can change 5 to any desired number of keywords

    keywords_string = ""
    for word in keywords:
        keywords_string += word + " "

    return keywords_string
