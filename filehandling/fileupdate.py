def insert_after_n(filepath, new_content, n):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines = lines[:n] + new_content + lines[n:]
    with open(filepath, 'w') as f:
        f.writelines(lines)
