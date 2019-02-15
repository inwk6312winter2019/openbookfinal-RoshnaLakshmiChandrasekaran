file = open('Book1.txt','\r')
file = open('Book2.txt','\r')
file = open('Book3.txt','\r')

common = []
for line in txtFile:
    words = line.split()
    for word in words:
        if word not in common:
            common.append(word)
for word in words:
    while i<len(common):
        i+=1
        if word in uniques:
             count += 1
print count

def most_common(hist):
  t = []
  for key, value in hist.items():
    t.append((value, key))
    t.sort(reverse=True)
  return t

