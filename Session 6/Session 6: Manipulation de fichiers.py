def space(filename, n):
    open(filename, 'w').write(n* ' ')
def capitalize(in_, out):
    with open(in_) as f:
        content = f.read()
    with open(out, 'w') as f:
        f.write(content.upper())
line_count = lambda filename: len(open(filename).readlines())
char_count = lambda filename: len(open(filename).read())
