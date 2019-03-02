import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.tag import StanfordNERTagger

text = "Brief me with stock price"

sents = sent_tokenize(text)
print(sents)

words = word_tokenize(text)
print(words)

print (nltk.pos_tag(words))

st = StanfordNERTagger('/Users/alex/PycharmProjects/HackRice/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/Users/alex/PycharmProjects/HackRice/stanford-ner.jar')

text = 'I want to use Amazon, Tesla, Oracle, Apple, Google'
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)



def get_companies(text):
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    companies = []

    for words in classified_text:
        if words[1] == 'ORGANIZATION' or words[1] == 'PERSON' or words[1] == 'LOCATION':
            companies.append(words[0])

    return companies 







def entities(text):
    return ne_chunk(pos_tag(word_tokenize(text)))

def process_language(text, vocabulary):


    original_text = text
    sents = sent_tokenize(original_text)
    words = word_tokenize(original_text)
    postag = nltk.pos_tag(words)




    return
