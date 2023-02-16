#comparing words
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

##Comment:
#The most similar words are word 1 and 2, this is interesting as they don't share any letters but they are both animals.

#My example
word1 = nlp("teacher")
word2 = nlp("student")
word3 = nlp("book")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#using for loops to compare a series of words with each other.
tokens = nlp('cat apple monkey banana chimp hat')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


#comparing sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

##When running the example file with sm I got this error message: 
# The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors.
# The similarity values given were also much lower than when I ran the file with md.