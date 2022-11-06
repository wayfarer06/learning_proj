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

string = 'Whereof one cannot speak, thereof one must be silent.'
result = rm_punctuation(string)
print(result)