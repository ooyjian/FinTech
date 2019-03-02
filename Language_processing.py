import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.tag import StanfordNERTagger

all_companies = 'I want to use Amazon, Tesla, Oracle, Apple, Google, google, apple, Microsoft, IBM, Intel, Compass, Adobe, SAP, ZOOM, Samsung, TENCENT, Sony, Alibaba, JBL, Dell'
extended_tech = ['google', 'apple', 'tencent', 'ZOOM', 'Zoom', 'microsoft', 'Oracle', 'oracle', 'Compass', 'compass', 'Razer', 'zoom']
immediacy_indicators = ['NOW', 'TODAY', 'PRESENTLY', 'CURRENTLY']
frequency_indicators = ['HOUR','HOURS','MINUTE','MINUTES','SECOND','SECONDS','DAY','DAYS','WEEK','WEEKS','MONTH','MONTHS']
interval_indicators = ['EVERY','PER','ALL','ANY','TOTAL']


st = StanfordNERTagger('/Users/alex/PycharmProjects/HackRice/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/Users/alex/PycharmProjects/HackRice/stanford-ner.jar')


text = "I want a brief every 10 minutes"
test_text = 'Brief me of google'

sents = sent_tokenize(text)

words = word_tokenize(test_text)

#print (nltk.pos_tag(words))








def has_number(postag_list):
    """

    :param postag_list: the list of tag of each word.
    :return: return True or False if the given pos_tag list has number in it
    """
    for i in range(len(postag_list)-1):
        if postag_list[i][1] == 'CD':
            return True
    return False


def get_companies(text,extended_tech):
    """

    :param text: given messege
    :return: set of companies in uppercase
    """
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    companies = []

    for words in classified_text:
        if words[1] == 'ORGANIZATION' or words[1] == 'PERSON' or words[1] == 'LOCATION':
            companies.append(words[0].upper())

    for words in classified_text:
        for company in extended_tech:
            if words[0].casefold() == company.casefold():
                companies.append(words[0].upper())
    return list(set(companies))

#print(get_companies(all_companies, extended_tech))

def brief_now(text,immediacy_indicator):
    """
    Determine whether we need to brief the user right now
    :param text: given message
    :param immediacy_indicator: immediacy indicator base
    :return: True if we need to te brief now, False otherwise.
    """
    original_text = text
    words = word_tokenize(original_text)
    postag_list = nltk.pos_tag(words)

    if has_number(postag_list):
        return False

    for pair in postag_list:
        if pair[1] == 'DT' and pair[0].upper() in interval_indicators:
            return False

    #has keyword now, return
    for pair in postag_list:
        if pair[1] == 'RB':
            if pair[0].upper() in immediacy_indicator:
                return True
    #start with a command verb
    for pair in postag_list:
        if (pair[0].upper() == 'BRIEF' and pair[1] == 'IN')or pair[1] == 'VB' or pair[1] == 'VBP':
            return True

    return False

#print(brief_now(test_text,immediacy_indicators))

def entities(text):
    return ne_chunk(pos_tag(word_tokenize(text)))

def set_interval(text):
    """
    find the interval of set
    :param text: given message
    :return: return the interval (number, time)
    """
    original_text = text
    words = word_tokenize(original_text)
    postag_list = nltk.pos_tag(words)
    for i in range(len(postag_list)-1):
        if postag_list[i][1] == 'CD':
            return (postag_list[i][0],(postag_list[i+1][0]).upper())

#print(set_interval("4 hours brief"))


def alter_companies_caps(name_all_caps):
    """
    return capitalized company name list
    :param name_all_caps: list of company names that are in all cap mode
    :return: capitalized company names
    """
    companies_names = []
    for companies in name_all_caps:
        companies_names.append(companies.lower().capitalize())
    return companies_names

#print(alter_companies_caps(get_companies(all_companies, extended_tech)))




