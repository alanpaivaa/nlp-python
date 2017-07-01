from nltk.corpus import gutenberg

print 'File ids:'
print gutenberg.fileids()

for fileid in gutenberg.fileids():
    print fileid
    print 'Len: ', len(gutenberg.raw(fileid))
    print 'Sents: ', len(gutenberg.sents)