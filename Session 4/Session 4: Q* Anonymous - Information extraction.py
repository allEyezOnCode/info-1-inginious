def extract(code):
    dic = {'int': 'number', }
    str_result = None
    for el in code:
        str_result = '' if str_result is None else str_result + " "
        if el.isnumeric():
            str_result += 'number'
            continue
        elif el.lower() in 'aeiouy':
            str_result += 'vowel'
        else: str_result += 'consonant'
        if el.isupper():
            str_result += '-up'
        else:
            str_result += '-low'
    return str_result
        
