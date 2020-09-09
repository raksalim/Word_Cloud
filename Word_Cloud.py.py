import matplotlib as mp
import wordcloud as wc


file_contents = open('Michelle_Obama_Thoughts_On_Trump.txt', 'r').read()

might_del = """def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]"""
    
# LEARNER CODE START HERE

# strip all unneccessary whitespace
def del_whitespace(text):

    # split text at unneccessary whitespaces
    whitespace = ["\n", "\t"]
    for ws in whitespace:
        text = text.split(ws)

        # get rid of unnesscary ws in list indexes
        for i in range(len(text)):
            text[i] = text[i].strip()
        
        # join text
        text = " ".join(text)

    return text


# get rid of all punctuations   
def del_punctuations(text):
    # itterate through whole text and get rid of any puncuations that are not neccessary
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in range(len(text)):
        if text[i] in punctuations:
            text = text.replace(text[i], " ")

    return text

# get rid of all uninteresting words and orphaned apostrophe contractions
def del_uninteresting(text):
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # orphaned apostrophe contractions from removing punctuations "you've", "you'll", "I'm"...
    apostrophe_contractions = ["s", "t", "ve", "m", "ll", "re"]

    # Total list for removal
    uninteresting = apostrophe_contractions + uninteresting_words

    text = text.split()

    i = 0
    while i in range(len(text)):
        if text[i] in uninteresting:
            text.pop(i)
        else:
            i += 1
        
    text = " ".join(text)
            
    return text

# take in a text file and make all words a list
def text_to_list(text):
    return text.split(" ")

# takes in a list of words and returns a dict of how many times the words appears
def dict_of_word_frequency(source_text):

    # clean text
    text_w_o_whitespace = del_whitespace(source_text)
    text_w_o_punct = del_punctuations(text_w_o_whitespace)
    text_w_o_uninteresting = del_uninteresting(text_w_o_punct)

    #clean text list
    text_list = text_to_list(text_w_o_uninteresting)

    #initiate result dict
    result = {}

    # itterate through text list and add word to list and increment frequency of word
    # format: {word: num_frequency}
    for word in text_list:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result



def main():

    result = dict_of_word_frequency()

    print(result)





main()
