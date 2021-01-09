def translate(data):
    translation = ""
    try:
        for char in data:
            translation += morse[char]
    except:
        raise TypeError
    return translation
