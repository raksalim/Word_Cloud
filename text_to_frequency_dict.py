
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

#del all non text characters
def del_all_non_letters(text):
    alphabet = """ abcdefghijklmnopqrstuvwxyz"""

    for i in range(len(text)):
        if text[i] not in alphabet:
            text = text.replace(text[i], " ")

    return text

#lower cased everythong for non reapeats just incase of odd capitalization
def lower_case_text_only(text):
    return text.lower()



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
    uninteresting_words = ["the", "a", "in", "for", "so", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "let", "no", "nor", "too", "very", "can", "will", "just"]
    
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
def sorted_frequency_dict(source_text):

    # clean text
    lower_case_text = lower_case_text_only(source_text)
    text_w_o_whitespace = del_whitespace(lower_case_text)
    text_w_o_punct = del_punctuations(text_w_o_whitespace)
    text_only = del_all_non_letters(text_w_o_punct)
    text_w_o_uninteresting = del_uninteresting(text_only)

    cleaned_text = text_w_o_uninteresting


    #clean text list
    text_list = text_to_list(cleaned_text)

    #initiate result dict
    result = {}

    # itterate through text list and add word to list and increment frequency of word
    # format: {word: num_frequency}
    for word in text_list:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1


    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    sorted_dict = {}

    for i in range(len(sorted_result)):
        sorted_dict[sorted_result[i][0].upper()] = sorted_result[i][1]

    return sorted_dict

