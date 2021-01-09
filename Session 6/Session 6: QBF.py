def get_max(filename):
    max_val = -1
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                try:
                    if float(line) >= 0 and max_val < float(line):
                        max_val = float(line)
                except: pass
    except Exception as error:
        print(error)
        return max_val
    return max_val
    
