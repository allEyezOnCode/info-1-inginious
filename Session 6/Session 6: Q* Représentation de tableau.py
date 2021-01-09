def table(filename_in,  filename_out, width):
    with open(filename_in) as f: file_content = f.readlines()
    tirets = '-'* width
    new_content = f'+-{tirets}-+\n'
    for line in file_content:
        space_l = ' ' * (width + 1- len(line))
        if len(line.strip()) > width: 
            new_content += f'| {line.strip()[:8]}{space_l} |\n'
        else: new_content += f'| {line.strip()}{space_l} |\n'
    new_content += f'+-{tirets}-+'
    with open(filename_out, 'w') as f: f.write(new_content)
