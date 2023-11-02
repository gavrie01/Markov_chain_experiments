# Markov_chain_experiments

1. run "pip install -r requirements.txt" or install latest versions of libraries using pip on your own
2. /data folder contains the text for experimentation: https://www.gutenberg.org/files/174/174-h/174-h.htm
3. Below are results of simple experimentation of Markov's chains with different orders: unigram and bigram:
   * Random word for sentence generation;
   * Generated text itself (10 words);
   * Evaluation metric, ideally it is around 1, however the best value is 1.54, which you see below;
   * Words cloud plot as bonus



A few examples of results:

UNIGRAM

Throw a random word from corpus to start: stained
Generated Text:
stained cloth rumble omnibuses clatter streetcabs could easily get annoyed
Perplexity: 3.72

BIGRAM
Throw a random word from corpus to start: ruisselant
Generated Text:
ruisselant la consolation des gorges rondes que soulève un soupir
Perplexity: 1.54

Throw a random word from corpus to start: necessarily
Generated Text:
necessarily immobile smile bright dawn either bruise bend either selby
Perplexity: 4.13