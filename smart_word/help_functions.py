from spellchecker import SpellChecker
import re
import wikipedia
from wikipedia import DisambiguationError, PageError

def rm_punctuation(string):
    punc_list = [".", "?", "!",
                 ",", ":", ":",
                 "—", "-", "[]",
                 "{}", "()", "'",
                 '"']
    for i in string:
        if i in punc_list:
            string = string.replace(i, '')
    return string

def make_uppercase(string):
    string = string.upper()
    return string

def make_lowercase(string):
    string = string.lower()
    return string

def rm_newline(string):
    string = ''.join(string.splitlines())
    return string

def rm_extra_spaces(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == ' ' and string[i-1] == ' ':
            pass
        else:
            new_string += string[i]
    return new_string

def count_alpha_char(string):
    return len([x for x in string if x.isalpha()])

def spell_check(string):
    try:
        spell = SpellChecker()
        index = -1
        words = re.findall(r"[\w']+|[.,!?;]+|[\n]", string)
        for word in words:
            index += 1
            if spell.unknown(word) and word != '\n':
                words[index] = spell.correction(word)
        words = ' '.join(words)
        new_string = ""
        for i in range(len(words)):
            try:
                if words[i] == ' ' and words[i + 1] in [".", ",", "!", "?", ";"]:
                    pass
                else:
                    new_string += words[i]
            except IndexError:
                pass
    except TypeError:
        new_string = 'Only strings can be spell checked please include text to the input field.'
    return new_string

def wiki_summary(string):
    if len(string.split()) >= 5:
        summary = 'Input is 5 or more words. Please add single or couple words to generate summary'
    else:
        try:
            summary = wikipedia.page(string, auto_suggest=False).summary
            summary = summary.replace('\n', '\n\n')
        except PageError:
            summary = f'{string} page not found try another word'
        except DisambiguationError:
            summary = f'{string} is ambiguous try to be more specific'
    return summary

def stop_words(string):
    stopwords = ['bug', 'tram', 'shoe']
    word_list = re.findall(r"[\w']+|[.,!?;]+|[\n]", string)
    index = -1
    new_string = ""
    for word in word_list:
        index += 1
        if word in stopwords:
            for i in word:
                word = word.replace(i, 'x')
        word_list[index] = word
    string = " ".join(word_list)
    for i in range(len(string)):
        if string[i] == ' ' and string[i + 1] == ',':
            pass
        else:
            new_string += string[i]
    return new_string














