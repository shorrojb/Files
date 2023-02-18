
#Similarities between cat, monkey and banana.
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#It is interesting that spacy can understand that cat and monkey are similar, as they are both classed as animals
#It is interesting that spacey can see a slight similarity between bananna and monkey as banana is in the monkey diet
#The program says that cat and apple are not similar, which is interesting because cats and apples are not associated in common culture. 

#My example
word1 = nlp("dog")
word2 = nlp("bone")
word3 = nlp("dinosaur")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#In my example, it is interesting that spacy cannot recognise the similarity between dog and bone (dogs chew on bones),
#But can recognise the similarities between dog and dinosaur (both animals), and bone and dinosaur (from fossils).


#Code Extract 2
#Using a for loop to compare vectors.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Code Extract 3
#Working with sentences.
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

#Differences when using en_core_web_sm
#There is now a userwarning saying that the sm model only uses context-sensitive tensors.
#Now the similarites are very different than before.