def translate(data, lan):
    translation = ""
    for word in data.lower().split(" "):
        if word in lan:
            translation += lan[word] + " "
        else: translation += word + " "
    return translation
