from nltk.corpus import gutenberg

# for fileid in gutenberg.fileids():
#     # num_chars = len(gutenberg.raw(fileid)) # With white spaces
#     num_chars = 0
#     for word in gutenberg.words(fileid):
#         num_chars += len(word)
#     num_words = len(gutenberg.words(fileid))
#     num_sents = len(gutenberg.sents(fileid))
#     num_vocab = len(set(word.lower() for word in gutenberg.words(fileid)))
#     print round(num_chars / num_words), round(num_words / num_sents), round(num_words / num_vocab), fileid


# from nltk.corpus import webtext
# for fileid in webtext.fileids():
#     print fileid, webtext.raw(fileid)[:65], '...'


# from nltk.corpus import nps_chat
# chatroom = nps_chat.posts('10-19-20s_706posts.xml')
# print chatroom[123]


# from nltk.corpus import brown
# print brown.categories()
# print brown.words(categories='news')
# print brown.words(fileids=['cg22'])
# print brown.sents(categories=['news', 'editorial', 'reviews'])

# from nltk.corpus import brown
# from nltk import FreqDist
# news_text = brown.words(categories='news')
# fdist = FreqDist(word.lower() for word in news_text)
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for modal in modals:
#     print "%s: %d" % (modal, fdist[modal])
#
# print 'Wh words'
# reg_text = brown.words(categories='religion')
# fdist = FreqDist(word.lower() for word in reg_text)
# wh_words = ['what', 'when', 'where', 'who', 'why', 'whom']
# for wh in wh_words:
#     print "%s: %d" % (wh, fdist[wh])

# from nltk.corpus import reuters # Contains 10788 news documents divided in training and test sets
# print reuters.fileids()
# print reuters.categories()
# print reuters.categories('training/9865')
# print reuters.categories(['training/9865', 'training/9880'])
# reuters.fileids('barley')
# reuters.fileids(['barley', 'corn'])
# print reuters.words('training/9865')[:14]
# print reuters.words(['training/9865', 'training/9880'])
# print reuters.words(categories='barley')
# print reuters.words(categories=['barley', 'corn'])

# Genesis
# MacMorpho
# Names
# Stopwords
# Swadesh
# Wordlist


# Univ Decl of Human Rights
# from nltk.corpus import udhr
# from nltk import FreqDist
# language = 'Portuguese_Portugues-Latin1'
# pt_words = udhr.words(language)
# pt_sents = udhr.sents(language)
# pt_raw = udhr.raw(language)
# print 'Words: ', pt_words
# print 'Words count: ', len(pt_words)
# print 'Sents: ', pt_sents
# print 'Sents count: ', len(pt_sents)
# print 'Raw: %s...' % pt_raw[:50]
# dist = FreqDist(char.lower() for char in pt_raw if char.isalpha())
# print dist['a']
# print dist['b']
# dist.plot(cumulative=False)

# Floresta
# from nltk.corpus import floresta
# print floresta.words()
# print floresta.readme()
# print floresta.fileids()

"""
- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents
"""

# from nltk.corpus import PlaintextCorpusReader
# from nltk import FreqDist
# corpus_root = 'historia'
# custom = PlaintextCorpusReader(corpus_root, '.*\\.txt')
# print custom.fileids()
# country = 'brasil'
# file = country + '.txt'
# words = custom.words(file)
# sents = custom.sents(file)
# raw = custom.raw(file)
# print len(words), words
# print len(sents), sents
# freq = FreqDist(word.lower() for word in words if word.isalpha())
# print freq.freq('brasil')
# print freq.most_common(10)
# freq.plot(cumulative=False)




# from nltk.corpus import brown
# from nltk import ConditionalFreqDist
# categories = ['news', 'romance']
# days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
# words = brown.words(categories=categories)
# cdf = ConditionalFreqDist(
#     (category, day)
#     for category in categories
#     for day in days
#     for word in brown.words(categories=category) if word.lower().startswith(day)
# )
#
# cdf.tabulate(conditions=categories, samples=days, cumulative=False)
#
# freq = cdf['news']
# print freq
# cdf.plot()



# from nltk.corpus import swadesh
# print swadesh.words('pt')
# print swadesh.entries(['pt', 'en'])



from nltk.corpus import wordnet as wn
print wn.synsets('motorcar')
print wn.synset('car.n.01').lemma_names()

print wn.synset('car.n.01').definition()
print wn.synset('car.n.01').examples()
print wn.synset('car.n.01').lemmas()
print wn.synset('car.n.01').lemma_names()