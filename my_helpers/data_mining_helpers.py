import nltk

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.text:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.corpus import wordnet
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))


    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            if remove_stopwords:
                syn = wordnet.synsets(word.lower())[0] if wordnet.synsets(word.lower()) else None
                if word == '.' or word == ',' or word == ';' or word == ':' or word == '!' or word == '?' or word == '``' or word == "''" or word == "'" or word == '"' or word == '(' or word == ')' or word == '[' or word == ']' or word == '{' or word == '}' or word == '--' or word == '-' or word.isdigit():
                    continue
                elif word.lower() in stop_words:
                    continue
                elif syn and syn.pos() == 'r':
                    continue
                else:
                    tokens.append(word.lower())
            else:
                tokens.append(word.lower())
    return tokens
