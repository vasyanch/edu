def anti_vowel(text):
    vow = "aeiouAEIOU"
    t = ''
    for i in text:
        if i in  vow:
            t = t + ''
        else:
            t = t + i
    return t 
