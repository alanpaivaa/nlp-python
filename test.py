# encoding: utf-8

# text = 'Bem vindo ao curso de processamento de linguagem natural com Python e NLTK'
# tokens = wt(text=text, language='portuguese')
# print tokens

file = open('jobs.csv', 'rb')

all_jobs = []
for line in file:
    all_jobs.append(line.replace('\n', ''))
file.close()

print all_jobs
print 'Count all_jobs: ', len(all_jobs)

count = 6
slice = len(all_jobs) / 6

matrix = []
for i in range(0, count):
    x = i * slice
    matrix.append(all_jobs[x:(x + slice)])

# Saving the remaing elements to the matrix
matrix[len(matrix) - 1] += all_jobs[(count * slice) - len(all_jobs):]

for array in matrix:
    print array
    print 'Count: ', len(array)

for i in range(0, count):
    file = open('jobs_%d.txt' % (i + 1), 'w')
    for word in matrix[i]:
        file.write(word + '\n')
    file.close()