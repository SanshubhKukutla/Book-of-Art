import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import FreqDist
import string


input_paragraph = """
    Once upon a time in a charming village nestled between emerald forests and crystal-clear streams, there lived a kind-hearted blacksmith named Oliver. Oliver was known throughout the village for his remarkable craftsmanship and the gentle spirit with which he approached his work.

    One sunny morning, a traveling circus arrived in the village, bringing with it a sense of wonder and excitement. People from all around gathered to witness the acrobats, clowns, and exotic animals. Among the circus performers was a captivating, yet melancholic, mime named Isabella. She had a talent for expressing deep emotions through her silent performances, but a heavy sorrow seemed to linger in her eyes.

    As the days passed, Oliver noticed Isabella often sitting alone by the riverbank, lost in her thoughts. His heart went out to her, and he decided to extend an act of kindness. One day, he crafted a delicate silver necklace with a tiny heart-shaped pendant. On it, he engraved the word "Joy" and carefully placed it in a small box.

    That evening, after Isabella's performance, Oliver approached her and, without saying a word, presented the gift. Isabella's eyes widened in surprise, and she held the necklace in her hand, tears glistening in her eyes. She understood that Oliver was offering her a piece of happiness.

    From that day on, Isabella wore the necklace during her performances. Her mime acts transformed as if a weight had been lifted from her heart. She expressed joy, love, and laughter like never before, and the audience could feel the sincerity in her art.

    The village was enchanted by Isabella's performances, and word of her newfound happiness spread far and wide. Visitors came from neighboring villages to see the circus, and the village itself became a place of joy and merriment.

    Oliver and Isabella's friendship grew stronger with each passing day, as they shared their love for the simple joys of life. They found that in the midst of the circus and the blacksmith's forge, they had discovered something more precious than silver or gold: they had found the joy of kindness and the beauty of friendship.

    And so, in that quaint village, amidst laughter and applause, Oliver and Isabella's story became a testament to the transformative power of a simple act of kindness, reminding everyone that in sharing joy, we often find the truest and most beautiful treasures in life.

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


"""
# Create a similarity matrix
similarity_matrix = np.zeros((len(sentences), len(sentences)))

for i in range(len(sentences)):
    for j in range(len(sentences)):
        if i != j:
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j])

# Use PageRank to rank the sentences
nx_graph = nx.from_numpy_array(similarity_matrix)
scores = nx.pagerank(nx_graph)

# Get the most important sentence
summary_sentence = sentences[max(scores, key=scores.get)]

# Tokenize the summary sentence
words = word_tokenize(summary_sentence.lower())

# Remove punctuation and stop words
filtered_words = [
    word for word in words if word not in string.punctuation and word not in stop_words
]

# Use NLTK's FreqDist to find the most common words
fdist = FreqDist(filtered_words)

# Get the most common words as keywords
keywords = [
    word for word, freq in fdist.most_common(5)
]  # You can change 5 to any desired number of keywords

keywords_string = ""
for word in keywords:
    keywords_string += word + " "

print(keywords_string)
"""


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
        word for word, freq in fdist.most_common(5)
    ]  # You can change 5 to any desired number of keywords

    keywords_string = ""
    for word in keywords:
        keywords_string += word + " "

    return keywords_string


"get_keywords()"
