from nltk.tokenize import word_tokenize as wt
from nltk import pos_tag as tag
import nltk

# text = wt("Ele joga futebol", language='portuguese')
# text = wt("He plays soccer")
# print text
# print tag(tokens=text, tagset='universal', lang='pt')

# print nltk.help.upenn_tagset('NN')

# wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
# word_tag_fd = nltk.FreqDist(wsj)

# print [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB']

from nltk.corpus import brown
# brown_tagged_sents = brown.tagged_sents(categories='news')
# brown_sents = brown.sents(categories='news')
#
# print brown_tagged_sents
# print brown_sents

# raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
# tokens = wt(raw)
# default_tagger = nltk.DefaultTagger('NN')
# default_tagger.tag(tokens)
# print default_tagger.evaluate(brown_tagged_sents)

# fd = nltk.FreqDist(brown.words(categories='news'))
# cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
# most_freq_words = fd.most_common(100)
# print most_freq_words
# print cfd['the'].max()
# likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
# print likely_tags
# baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
# print baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

# Trainning Tagger
# brown_tagged_sents = brown.tagged_sents(categories='news')
# size = int(len(brown_tagged_sents) * 0.9)
# train_sents = brown_tagged_sents[:size]
# test_sents = brown_tagged_sents[size:]
# unigram_tagger = nltk.UnigramTagger(train_sents)
# evaluation = unigram_tagger.evaluate(test_sents)
# print evaluation

brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
e0 = t0.evaluate(test_sents)
print 'E0: ' + str(e0)

t1 = nltk.UnigramTagger(train_sents, backoff=t0)
e1 = t1.evaluate(test_sents)
print 'E1: ' + str(e1)

t2 = nltk.BigramTagger(train_sents, backoff=t1)
e2 = t2.evaluate(test_sents)
print 'E2: ' + str(e2)

t3 = nltk.TrigramTagger(train_sents, backoff=t2)
e3 = t3.evaluate(test_sents)
print 'E3: ' + str(e3)