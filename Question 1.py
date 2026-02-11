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

file_word_counts = Counter(clean_words) #counter counts the amount of each word and stiores it into a list
most_common_words = file_word_counts.most_common(10) #takes the most common 10 words from the list

for word, count in most_common_words: #loops through the most common words list
    print(f'{word} -> {count}') #prints word and count