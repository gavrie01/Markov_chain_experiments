
# import of libraries -----------------------------------------------------
import string
import os
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, pos_tag # parts of speech
# -------------------------------------------------------------------------
# variables

generated_text = []
maximum_generated_text_length = 10
# Initialize the dictionary for Markov chain
mc_dict = {}

# --------------------------------------------
# clear console on start
clear = lambda: os.system('cls')  # on Windows System
os.system('clear')  # on Linux System
clear()
# ---------------------------------------------

# Load the text from a file
with open('data/Dorian_Grey.txt', encoding='UTF-8') as file:
    text = file.read()

# Remove punctuation and convert to lowercase
exclude = set(string.punctuation)
text = ''.join(ch for ch in text if ch not in exclude).lower().strip()
text = ''.join(s for s in text if s not in ('“', '”', '’'))
text = ''.join([i for i in text if not i.isdigit()])
# Tokenize the text into words
words = word_tokenize(text)
#-------------------------------


# Remove stopwords
stops = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stops]
words = filtered_words

# Create a frequency distribution of words
fr = FreqDist(filtered_words)
fr_dict = dict(fr.most_common(300))

# Print the most common words
for word, frequency in fr_dict.items():
    print(word, ':', frequency)
# Populate the mc_dict
#for i in range(len(words) - 1):
#    word = words[i]
#    next_word = words[i + 1]
#    if word in mc_dict:
#        if next_word in mc_dict[word]:
#            mc_dict[word][next_word] += 1
#        else:
#            mc_dict[word][next_word] = 1
#    else:
#        mc_dict[word] = {next_word: 1}

# Populate the mc_dict with bigrams
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word in mc_dict:
        if next_word in mc_dict[current_word]:
            mc_dict[current_word][next_word] += 1
        else:
            mc_dict[current_word][next_word] = 1
    else:
        mc_dict[current_word] = {next_word: 1}


# Calculate transition probabilities within mc_dict
for word, next_word_counts in mc_dict.items():
    total_transitions = sum(next_word_counts.values())
    probabilities = {next_word: count / total_transitions for next_word, count in next_word_counts.items()}
    mc_dict[word] = probabilities


# Filter non meaningful keys
unwanted_keys = ('e', 'isnt', 'xix', 'p', 'downloading', 'concerning', 'federal', 'computer','damages', 'legal', 'machinereadable', 'b', 'ein', 'regulating', 'donations', 'donors', 'array', 'approach', 'tax', 'legally', 'pg', 'ut', 'irs', '•', 'f', 'offers', 'accepted', 'swamp', 'hart', 'checks', 'international', 'michael', 'addresses', 'staff', 'volunteer', 'main', 'c', 'donation', 'facility', 'foundations', 'includes', 'subscribe', 'network', 'originator', 'newsletter', 'wwwgutenbergorgdonate', 'wwwgutenbergorgcontact', 'widespread', 'licensed')
mc_dict = {key: value for key, value in mc_dict.items() if key not in unwanted_keys}
#------------------------------------------------------------------------------
# breakdown to parts of speech
tagged_text = pos_tag(words)

#write into file to explore better
with open('data/POS_mark_up.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        f.write(f"{word}: {pos}\n")
# separate by part of speech: Noun
with open('data/POS_Noun.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        if pos in ['NN', 'NNS', 'NNP', 'NNPS']:
            f.write(f"{word}: {pos}\n")
#nouns = [word for word, pos in tagged_text if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
#print("Nouns:", nouns)

## separate by part of speech: Verb
with open('data/POS_Verb.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            f.write(f"{word}: {pos}\n")
# separate by part of speech: Adverb
with open('data/POS_Adverb.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        if pos in ['RB', 'RBR', 'RBS']:
            f.write(f"{word}: {pos}\n")

# separate by part of speech: Adjective
with open('data/POS_Adjective.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        if pos in ['JJ', 'JJR', 'JJS']:
            f.write(f"{word}: {pos}\n")


# separate by part of speech: Determiner
with open('data/POS_Determiner.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        if pos in ['DT', 'PDT']:
            f.write(f"{word}: {pos}\n")

# separate by part of speech: Rest
with open('data/POS_Determiner.txt', 'w', encoding='UTF-8') as f:
    for word, pos in tagged_text:
        if pos in ['CC', 'CD', 'IN', 'MD', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB']:
            f.write(f"{word}: {pos}\n")









random_word = random.choice(list(mc_dict.keys()))
generated_text.append(random_word)

# Continue generating text
current_word = random_word  # Start with the randomly selected word
while len(generated_text) < maximum_generated_text_length:
    # Look up the transition probabilities for the current word
    next_word_probabilities = mc_dict.get(current_word, {})
    if next_word_probabilities:
        # Select the next word based on transition probabilities (weighted random choice)
        next_word = random.choices(list(next_word_probabilities.keys()), 
                                   weights=list(next_word_probabilities.values()))[0]

        # Append the next word to the generated text
        generated_text.append(next_word)

        # Set the next word as the current word for the next iteration
        current_word = next_word
        
    else:
        break  # If there are no probabilities for the current word, break the loop

for key, value in mc_dict.items():
    print(key, ':', value) 
# Print the generated text
print("Throw a random word from corpus to start:", random_word)
print("Generated Text:")
print(" ".join(generated_text))


# Generate and display the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(fr_dict)
plt.figure(figsize=(10, 5))
plt.title("Dorian Gray words' frequency")
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.show()

# Calculate perplexity using the generated_text
import math

def calculate_perplexity(test_data, model):
    n = len(test_data)
    log_sum = 0

    for i in range(n - 1):
        current_word = test_data[i]
        next_word = test_data[i + 1]
        probabilities = model.get(current_word, {})
        if next_word in probabilities:
            probability = probabilities[next_word]
            log_sum += -math.log(probability)

    avg_log_likelihood = log_sum / n
    perplexity = math.exp(avg_log_likelihood)
    return perplexity

# function call:
perplexity = calculate_perplexity(generated_text, mc_dict)
print("Perplexity:", round(perplexity, 2))
