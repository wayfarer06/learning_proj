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

def uppercase(string):
    string = string.upper()
    return string

def lowercase(string):
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
    spell = SpellChecker()
    index = -1
    words = re.findall(r"[\w']+|[.,!?;]", string)
    for word in words:
        index += 1
        if spell.unknown(word):
            words[index] = spell.correction(word)
    return ' '.join(words)

def wiki_summary(string):
    try:
        summary = wikipedia.page(string, auto_suggest=False).summary
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

print(stop_words('bug, in the \n shoe'))














