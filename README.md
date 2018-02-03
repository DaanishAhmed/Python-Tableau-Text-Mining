Text Mining Analysis on Film Reviews
----------------

This project involves using Python to analyze five film review texts written between 1934 and 2014.  My goal is to perform a text analysis on these reviews to study how critics' word choices changed over time.  I created a Python script that returns the 30 most common words in each document and how often those words appeared.  The program filters out stop words (such as "and," "like," and "but"), removes punctuation, and handles stemming (i.e. words such as "write" and "writing" are listed as the same word).  After running the program on all five reviews, I combined the results into a single spreadsheet and examined them using visualizations in Tableau.  I used these visualizations to study whether these word choices reflect audiences' changing tastes in films over time.

The full report can be found in the file "Film Text Analysis.pdf".  This report shows a complete breakdown of my analysis, including executive summary, problem identification, motivation, text mining methods, model analysis, results comparison, and proposed solutions.  Tables and visualizations are included in the main body of the report.

The data sources used in this project are all text files obtained from film reviews written at The New York Times between 1934 and 2014.  The selected films are the winners of the Academy Awards' Best Picture during the years 1935, 1955, 1975, 1995, and 2015.  These films are "It Happened One Night" (1934), "On the Waterfront" (1954), "The Godfather, Part II" (1974), "Forrest Gump" (1994), and "Birdman" (2014).  All of these reviews have been published on The New York Times' website.

Additionally, I have included the file "DaanishAhmed-output-1934-2014.csv", which contains the combined outputs from running my Python file on all five reviews.  It includes the top 30 most common words for each year.  This .csv file was created manually, since the output file is replaced every time my code is successfully executed.

The Python script is included in the file "DaanishAhmed-text-parse.py".  The requirements are described in the file "requirements.txt".  Instructions on how to use the program are included as comments in the .py file.  Please read the instructions carefully before executing the code to ensure that the program functions correctly.  Please note that the file requires NLTK (Natural Language Tool Kit), and the program will not work if you have not installed the NLTK add-on for Python.  I have also included an extended list of stop words ("DaanishAhmed-stopwords.txt"), which adds additional uninteresting words not included in the NLTK stop words list.  This file must be in the same location as the main Python code.

Finally, I have included the Tableau file "film word choice display.twb".  This file includes all of the visualizations used in my report.  It uses the data source "DaanishAhmed-output-1934-2014.csv".


References:

Canby, V. (1974, December 13). 'Godfather, Part II' Is Hard to Define: The Cast. The New York
Times. Retrieved May 3, 2017, from http://www.nytimes.com

Dargis, M. (2014, October 16). Former Screen Star, Molting on Broadway. The New York
Times. Retrieved May 3, 2017, from https://www.nytimes.com/2014/10/17/movies/birdman-stars-michael-keaton-and-emma-stone.html?_r=0

Hall, M. (1934, February 23). Claudette Colbert and Clark Gable in a Merry Jaunt From Miami
to New York. The New York Times. Retrieved May 3, 2017, from http://www.nytimes.com

Maslin, J. (1994, July 6). FILM REVIEW; Tom Hanks as an Interloper in History. The New
York Times. Retrieved May 3, 2017, from http://www.nytimes.com

W., A. (1954, July 29). Astor Offers 'On the Waterfront'; Brando Stars in Film Directed by
Kazan. The New York Times. Retrieved May 3, 2017, from http://www.nytimes.com
