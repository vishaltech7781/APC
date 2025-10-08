def write(filepath, content):
    with open(filepath, 'w') as f:
        f.writelines(content)
