def get_country(l, name):
    res = list(filter(lambda x: x['City'] == name, l))
    return False if len(res) == 0 else res[0]['Country']
