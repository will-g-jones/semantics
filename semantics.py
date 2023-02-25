#This will import space and the language analysis model en_core_web_md.
import spacy
nlp = spacy.load('en_core_web_md')

#This tokenizes and analysis similarity between the three words.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#This analyses all possible combinations of cat, monkey and banana including with themselves.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
#cat and banana (0.2) is far less associated than cat and monkey (0.64) which is interesting because I would not associate a cat anymore with a monkey than a banana.
#monkey and banana being less correlated than cat and monkey likely relates to them both being animals, although you'd mentally associate a monkey with a banana more than a cat. 


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)

#This section details three words of my own choosing and their analysis:
word4 = nlp("tree")
word5 = nlp("bird")
word6 = nlp("tortoise")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))
tokens2 = nlp('tree bird tortoise ')

for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

#This creates a hold so previous values can be read
input("Press enter to continue:")
print("\n\n\n")

#This changes nlp to the -sm model instead of -md, then performs the same tasks again.
nlp = spacy.load('en_core_web_sm')
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)