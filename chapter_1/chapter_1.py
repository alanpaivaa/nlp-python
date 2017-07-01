# encoding: utf-8

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize as wt

print 'Text:'
text = u"A História do Brasil tem seu início comumente apontado a partir da chegada dos portugueses, quando Pedro Álvares Cabral e sua esquadra atracaram na região de Porto Seguro, em 1500. Porém, os portugueses não foram os primeiros seres humanos a chegarem nessa região, pois existiam já inúmeras sociedades indígenas no local. Isso ocorre porque a historiografia brasileira sempre privilegiou o estudo da História do Brasil depois da chegada de Cabral. A divisão da história do país foi feita levando em consideração as formas políticas adotadas na organização da população e do território. Dessa forma, temos o Brasil Colônia, período de conquista dos portugueses no Novo Mundo e, posteriormente, temos o Brasil Império, momento em que os descendentes da coroa portuguesa que haviam ficado no país tornaram a colônia independente e criaram um novo Império."
tokens = wt(text)
# print tokens
print text

dist = FreqDist(word.lower() for word in tokens)
vocab = set(dist)

print ''
print 'Most common words:'
common = dist.most_common(10)
for word, count in common:
    print "%s: %d" % (word, count)

print ''
print 'Words that appear only once:'
print dist.hapaxes()

word_size_filter = 5
frequency_filter = 1
long_words = [word for word in vocab if len(word) > word_size_filter and dist[word] > frequency_filter]
print "\nLong Words:"
print long_words