#Description:
#Write a function word_frequency(text) that takes a string text and returns a dictionary, where:

#key is the word,

#value is the number of times the word appears in the text.


def word_frequency(text):
    result = {}
    for x in text.split():
        result[x] = result.get(x, 0) + 1

    return result
print(word_frequency("apple banana apple orange banana apple")) 