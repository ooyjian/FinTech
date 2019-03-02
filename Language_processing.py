import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.tag import StanfordNERTagger


extended_tech = ['google', 'apple', 'tencent', 'ZOOM', 'Zoom', 'microsoft', 'Oracle', 'oracle', 'Compass', 'compass', 'Razer', 'zoom']
immediacy_indicators = ['NOW', 'TODAY', 'PRESENTLY', 'CURRENTLY']
frequency_indicators = ['HOUR','HOURS','MINUTE','MINUTES','SECOND','SECONDS','DAY','DAYS','WEEK','WEEKS','MONTH','MONTHS']

text = "I want a newly get brief now"

sents = sent_tokenize(text)

words = word_tokenize(text)

print (nltk.pos_tag(words))

st = StanfordNERTagger('/Users/alex/PycharmProjects/HackRice/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/Users/alex/PycharmProjects/HackRice/stanford-ner.jar')

all_companies = 'I want to use Amazon, Tesla, Oracle, Apple, Google, google, apple, Microsoft, IBM, Intel, Compass, Adobe, SAP, ZOOM, Samsung, TENCENT, Sony, Alibaba, JBL, Dell'

text2 = 'I want to use google'
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)





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
    return set(companies)

#print(get_companies(all_companies, extended_tech))

def brief_now(text,immediacy_indicator):
    original_text = text
    words = word_tokenize(original_text)
    postag_list = nltk.pos_tag(words)

    for pair in postag_list:
        if pair[1] == 'RB':
            if pair[0].upper() in immediacy_indicator:
                return True
    return False

#print(brief_now(text,immediacy_indicators))

def entities(text):
    return ne_chunk(pos_tag(word_tokenize(text)))

def set_interval(text):
    original_text = text
    words = word_tokenize(original_text)
    postag_list = nltk.pos_tag(words)
    for i in range(len(postag_list)-1):
        if postag_list[i][1] == 'CD':
            return (postag_list[i][0],(postag_list[i+1][0]).upper())

#print(set_interval("4 hours brief"))
