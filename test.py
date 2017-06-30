from nltk.tokenize import word_tokenize as wt

text = 'Bem vindo ao curso de processamento de linguagem natural com Python e NLTK'
tokens = wt(text=text, language='portuguese')
print tokens