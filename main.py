#used this tutorial: https://youtu.be/21FnnGKSRZo?si=4FFpCUjm8x0jBD2K
#creating a story generator similar to madlibs
#it will have stories made in text files that will have interjectable words
#allowing muiltiple stories to be used 

#opening a file, story.txt, in read mode (r), file operations can be done because of the (with)
with open("story.txt", "r") as f:
    #reads in the story
    story = f.read()

#find presence of opening < and closing >, store in a list, then ask user what to input, and replace with word user gave
#enumerate allows us access to position and element at that position

#choose to use a dataset rather than a list because it will only store unique elements
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#locates all the words in the story, getting the index as well as the value
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        #start of word up to i + 1, gives us access to a slice which is a subsection of the whole story
        word = story[start_of_word: i + 1]
        #add word to words list
        words.add(word)
        #set start equal to -1 to reset the process (allowing to find another word)
        start_of_word = -1

#set up a dictionary with word as the key
answers = {}

for word in words:
    #adding two strings together
    answer = input("Enter a word for " + word + ": ")
    #creating a dictionary with all words
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
    
    
