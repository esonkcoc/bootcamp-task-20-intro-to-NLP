import spacy
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."]

for sentence in gardenpathSentences:
# The code enters a loop that iterates over each sentence in the `gardenpathSentences` list.

    doc = nlp(sentence)
# For each sentence, `doc = nlp(sentence)` applies the nlp model to process the sentence.

    print(f"\nSentence: {sentence}")
    for token in doc:

# Another loop is initiated to iterate over each token (individual word or punctuation) in the processed sentence.

        print(f"Token: {token.text}, POS: {token.pos_}, Tag: {token.tag_}, Entity: {token.ent_type_}")

# Within this loop, the code prints information about each token, such as its text, part-of-speech, tag and named entity type.

print(spacy.explain("NN"))
print(spacy.explain("VBZ"))

#I looked up the entities NN and VBZ which stood for noun (singular or mass) and verb (3rd person singular present), both of which made sense in realtion to their words, 'cotton' and 'is'.