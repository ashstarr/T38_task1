# ====== Import Libraries ======
# Import spacy
import spacy
nlp = spacy.load('en_core_web_md')

# ====== SIMILARITY WITH SPACY ======
print('\nSIMILARITY WITH SPACY EXAMPLE')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Write a note about what you found interesting about the similarities
# between cat, monkey and banana and think of an example of your own.
print('''
It's interesting that:
1: Monkey and Cat are the most similar, presumably because they are both animals
2: Monkey and Banana are twice as similar than Cat and Banana presumably because
Monkey's eat Bananas and Cats don't!
''')

# think of an example of your own.
print('\nSIMILARITY WITH SPACY MY EXAMPLE')
word1 = nlp("cow")
word2 = nlp("milk")
word3 = nlp("grass")
print(f'{word1} {word2} similarity score:{word1.similarity(word2)}')
print(f'{word3} {word2} similarity score:{word3.similarity(word2)}')
print(f'{word3} {word1} similarity score:{word3.similarity(word1)}')

print('''
It's interesting that:
1: Cow and milk are most similar, presumably because a cow makes milk
2: Grass and Cow are more similar than Grass and Milk presumably because
a cow eats Grass but without Grass there would be no milk!!!
''')


# ====== WORKING WITH VECTORS ======
print('\nWORKING WITH VECTORS EXAMPLE')
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# ====== WORKING WITH SENTENCES ======
print('\nWORKING WITH SENTENCES EXAMPLE')
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

# ====== EXAMPLE FILE WITH EN_CORE_WEB_SM ======
# Run the example file with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice is different from the model
# 'en_core_web_md
print('''
1. When you run the file with en_core_web_sm you get a warning to say: 

UserWarning: [W007] The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger, parser and NER, 
which may not give useful similarity judgements.'

2. The similarity scores are all lower except the exact matches 
when you run the file with en_core_web_sm
''')
