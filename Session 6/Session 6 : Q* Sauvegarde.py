def save_data(filename, life, mana, position_x, position_y):
    with open(filename, 'w') as f:
        f.write(f'{life}\n{mana}\n{position_x}\n{position_y}')
def load_data(filename):
    with open(filename) as f:
        return tuple([int(val) for val in f.read().split(sep='\n')])
