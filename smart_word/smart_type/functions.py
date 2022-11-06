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







