import string
from collections import Counter

with open("sample-file.txt","r") as file: #opens the file and reads its contents
    file_contents = file.read() #adds the file contents to a string variable

text_tokens = file_contents.split() #splits the file contents into a list of words (tokens)

clean_words = [] #initalized empty list

for word in text_tokens: #loops through the list of words
    token = word.lower() #sets the words to lowercase
    token = token.strip(string.punctuation) #strips any punctuation found on the word

    if sum(char.isalpha() for char in token) >=2: #checks if all the characters in the word are letters and of a length greater than or equal to 2
        clean_words.append(token) #adds it to the clean words list

list_of_bigrams= []
for i in range(len(clean_words)-1):
    bigram = (clean_words[i],clean_words[i+1])
    list_of_bigrams.append(bigram)

bigram_counts = Counter(list_of_bigrams)
most_common_bigrams= bigram_counts.most_common(5)
for bigram, count in most_common_bigrams:
    print(f"{bigram[0]} {bigram[1]} -> {count}")