def write(letter_template, name):
    with open(letter_template) as f:
        content = f.read().replace('#', name)
    with open(letter_template, 'w') as f:
        f.write(content)
