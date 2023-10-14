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

desired_num = 5

input_paragraph = """
    Hello Kitty once went to shop. She found a cat. Hello Kitty killed the cat. Then she ran away from teh cops and hide in a sewer. Hello Kitty died of starvation
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
