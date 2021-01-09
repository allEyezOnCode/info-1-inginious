temp = ""
if not i % 3:
    temp += 'fizz'
if not i % 5:
    temp += 'buzz'
temp = temp if temp != '' else 'no'
