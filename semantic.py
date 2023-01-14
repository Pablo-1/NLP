import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("screwdriver")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")
print(word1.similarity(word4))
print(word2.similarity(word4))
print(word3.similarity(word4))
print("\n")

#--------------------------------

tokens = nlp('cat apple monkey banana screwdriver')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#----------------------------------

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ",  similarity)


'''
It makes sense that monkey is more similar to banana than a cat is. Similarly cat and monkey are more similar then previous comparison
as they are both animals. I find it really interesting that when you put screwdriver in the mix it comes up with almost the same similarity
to both monkey and banana. 
-------------------------------
When you run en_core_web_sm the debugger gives a message that the model has no word vectors loaded and results may be different. 
The results in fact come out different then with the other model.
'''