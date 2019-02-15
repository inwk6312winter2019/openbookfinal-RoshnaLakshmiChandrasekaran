inputFilename =  "Book1.txt"
def unique_file(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    file_contents = input_file.read()
    input_file.close()
    word_list = file_contents.split()

    file = open(output_filename, 'w')

    for word in word_list:
        if word not in word_list:
            file.write(str(word) + "\n")
    file.close()

def sorted_words[word list]:
    result = []
    for word in word list:
        if word[0] <= word[1:]:
             result.append(word)
print(word)
file.close()

def character_word_count:
    for word in file.read().split():
      if word not in wordcount:
         wordcount[word] = 1
      else:
         wordcount[word] += 1
print (word,wordcount)
file.close()

