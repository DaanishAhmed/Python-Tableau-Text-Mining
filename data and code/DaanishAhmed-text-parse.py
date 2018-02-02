# DATA 620 Assignment 12.1
# TURN IN #1
# Written by Daanish Ahmed
# Semester Spring 2017
# Professor Majed Al-Ghandour

# This program asks the user to enter a file name.  The program will read through
# the file and create a dictionary that keeps track of the number of times each
# word appears in the text.  During this process, it will also count the total
# number of words, characters, and lines in the entire file.  At the end, it will
# return the total number of words, characters, and lines as well as a list of the
# 30 most common words and how often they occurred.  This list will be saved as an
# output file in .csv format.  It will not contain any stop words (such as 'and' or
# 'from') and it will lemmatize words so that words such as 'swim' and 'swimming'
# are counted as the same word.

# The purpose of my analysis is to study the change of word choice within film
# reviews for the Oscar Best Picture winners between the years 1934 and 2014.  The
# files that I used are 'DaanishAhmed-it-happened-1934.txt', 'DaanishAhmed-
# waterfront-1954.txt', 'DaanishAhmed-godfather-1974.txt', 'DaanishAhmed-gump-
# 1994.txt', and 'DaanishAhmed-birdman-2014.txt'.  These files, along with any
# other files used to test this program, must be placed in the same folder where my
# Python code is placed.

# Importing sys allows us to use sys.exit when checking for errors.  Importing 
# string allows us to use commands such as string.punctuation so that we can remove
# the punctuation when counting words.
import sys
import string

# The code below allows us to use the built-in stop words and lemmatizer features
# provided by NLTK (Natural Language Tool Kit).  This will only work if you have
# installed the NLTK add-on for Python.

# Use of these features was inspired by Word Count Starter Program
# Based on Chuck Severance's Python Code - Romeo Section 9.4
# from Python for Informatics 3
# http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
#
# Code changes by Daanish Ahmed for UMUC DATA 620
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# Initialize the variables to be used in this program.
wordCounts = dict()
wordList = []
numChars = 0
numLines = 0
numWords = 0

# Initialize the list of stop words and lemmatizer (based on Severance code).
stopWords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# I created a separate text file called 'DaanishAhmed-stopwords.txt' that contains
# words that I chose to append to the list of NLTK stop words.  Some of these words
# include the names of actors or characters, as well as other common words not
# already in the NLTK stop words list.  Please place this file in the same folder as
# this python code. If the file is not found, an error will be returned to the user.
try:
    stopHand = open('DaanishAhmed-stopwords.txt')
except FileNotFoundError:
    print('The file DaanishAhmed-stopwords.txt cannot be opened.')
    print('This file is needed to eliminate all stop words from the final output.')
    print('Please make sure that it is placed in the same folder as this Python file.')
    sys.exit()

# This loop will go through the words in 'DaanishAhmed-stopwords.txt' and add each
# word to the stopWords list.
for word in stopHand:
    
    # Removes any spaces that appear before or after the text in each line.
    word = word.strip()

    # If the current line contains no characters, then the program will skip to the
    # next line.  It will also skip any comments (lines beginning with '#').
    if len(word) == 0 or word.startswith('#'):
        continue

    # Ensures that no duplicates are added to the list of stop words.
    if word not in stopWords:
        stopWords.append(word)

# Closes the stop words text file.
stopHand.close()

# End of appending words to stopWords list.

# We ask the user to input the name of the file (including the file extension).
fname = input('Please enter the file name: ')

# The following lines of code check to see if the user entered a valid file name
# and that the file exists.  If the program is unable to open the specified file
# (indicating that the file name is not valid), then an error message will be
# returned and the program will close.
try:
    fhand = open(fname)
except FileNotFoundError:
    print('This file cannot be opened.')
    print('Please enter the name of an existing file, including the file extension.')
    sys.exit()

# Use of the NLTK lemmatizer may take a few seconds to process all of the words, so
# we ask the user to wait while the system computes the results.
print('\nPlease wait as we compute the results... \n')

# This loop will check each line in the file and break down each line into a list
# of words.  It will go through that list, count the number of times that each word
# appears, and record that information into the wordCounts dictionary.
for line in fhand:

    # Removes any spaces that appear before or after the text in each line.
    line = line.strip()

    # If the current line does not contain any words, then the program will skip
    # the current iteration of the loop and move on to the next line.  It will also
    # skip any comments (lines beginning with '#').  Skipping comments is necessary
    # because I added some comments at the top of the text files that I used to
    # append my name, course number, assignment number, etc.
    if len(line) == 0 or line.startswith('#'):
        continue

    # Increments the count for the number of lines.
    numLines += 1

    # Increments the count for the number of characters in each line (before removing
    # punctuation).
    numChars += len(line)

    # The following code counts the number of words (before removing all of the stop
    # words).  Each line is split into words, and each word increments the count.
    initWords = line.split()
    for word in initWords:
        numWords += 1

    # Removes all punctuation within the current line.
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.replace('—', ' ')

    # Set all words to lower case so that each word will be included only once in
    # the dictionary, regardless of whether the letters are upper or lower case.
    line = line.lower()

    # The following loop is designed to remove all stop words from the sentence.
    # It is designed in a way to ensure that it does not remove parts of words that
    # contain contain stop words within them, but only individual words that are
    # found in the stopWords list.
    for word in stopWords:
        if line.startswith(word + ' '):
            line = line.replace(word + ' ', '')
        elif line.endswith(' ' + word):
            line = line.replace(' ' + word, '')
        else:
            line = line.replace(' ' + word + ' ', ' ')

    # Splits the line into a list of words.
    words = line.split()

    # The following loop goes through each word listed in the current line and
    # lemmatizes it (replaces it with its root word).  The code makes sure that
    # words are lemmatized appropriately, regardless of whether they are nouns
    # or verbs.  The code then checks to see whether that word exists in our
    # dictionary.  If the word does not exist yet, it will be added with a count
    # of 1.  If it already exists, then its count will be incremented by 1.
    for word in words:
        word = lemmatizer.lemmatize(word, pos = 'n')
        word = lemmatizer.lemmatize(word, pos = 'v')
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1

# Closes our input file.
fhand.close()

# End of generating wordCounts dictionary.

# The rest of the code is used to generate the output.  This includes returning
# the count of words, characters, and lines.  It also includes returning a list of
# the 30 most frequently-occurring words with their word counts and saving this
# output to a .csv file.

# The following code is from Starter Code -
# Based on Toby Donaldson's Python: Visual QuickStart Guide
# function print_file_stats (location 5347)
#
# Modified for UMUC DATA 620 by Daanish Ahmed

# Prints the number of words, characters, and lines in the file.
print('This file has ' + str(numWords) + ' words.')
print('This file has ' + str(numChars) + ' characters.')
print('This file has ' + str(numLines) + ' lines.')

# Converts the dictionary into a list to display the words in numeric order.
wordList = [(wordCounts[word], word) for word in wordCounts]

# Sorts the words numerically from highest count to lowest.
wordList.sort()
wordList.reverse()

# Index is used to number each word in the list.
countList = 1

# Prepares the header of the .csv file that we will produce.
output = 'Rank,Word,Count\n'

# If there are at least 30 words in the list, then the program will only print the
# 30 most common words and their counts, numbered from 1 to 30.  If there are zero
# words in the list, then the program will return a message asking for the user to
# input a file that does not have zero words.  Otherwise, the program will return
# every word recorded in the list along with the count for each word, numbered in
# order.  In most cases, the input file will have more than 30 unique words, but the
# program will still function if this is not the case.  During this process, the
# code will also append the words and their counts to the output.
if len(wordList) >= 30:
    print('\nHere are the 30 most common words: \n')
    for count, word in wordList[:30]:
        output += str(countList) + ',' + str(word) + ',' + str(count) + '\n'
        print('%2s.  %4s %s' % (countList, count, word))
        countList += 1
elif len(wordList) == 0:
    print('\nThere are no words in this file.')
    print('Please enter a file with words.')
else:
    print('\nHere are the ' + str(len(wordList)) + ' most common words: \n')
    for count, word in wordList[:len(wordList)]:
        output += str(countList) + ',' + str(word) + ',' + str(count) + '\n'
        print('%2s.  %4s %s' % (countList, count, word))
        countList += 1

# End of Donaldson output code segment.

# The following code will create the file 'DaanishAhmed-output.csv' and write the
# list of words and their counts into this file.  If the file already exists, then
# it will be overwritten with a new file.  To save any particular version of the
# output, you can rename the file or move it to another folder.
outFile = open('DaanishAhmed-output.csv', 'w')
outFile.write(output)
outFile.close()

# End of script.
