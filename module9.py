# Python script that counts the frequency of words in a given text using dictionaries,
# conditional sentences, loops, and recursive functions.


string_of_words = "A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result."
frequency_dict = {}  # Initialize the word frequency dictionary


def remove_punctuation(raw_text):
    return raw_text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")


def split_to_single_words(raw_text):
    return raw_text.split()


def process_words(split_words, index):
    if index == len(split_words):
        return
    single_word = split_words[index]

    if single_word in frequency_dict:
        frequency_dict[single_word] += 1
    else:
        frequency_dict[single_word] = 1

    process_words(split_words, index + 1)

    return frequency_dict



def get_word_occurrence(text_sentence):
    # Use conditional sentences to handle special cases (e.g., empty input).
    if not text_sentence:
        return {}
    words = split_to_single_words(remove_punctuation(text_sentence))
    return process_words(words,0)


string_without_punctuation = remove_punctuation(string_of_words)

dict_word_result = get_word_occurrence(string_without_punctuation)

# loop over dictionary to print number of words in string
for word, count in dict_word_result.items():
    print(f"{word}: {count}")
