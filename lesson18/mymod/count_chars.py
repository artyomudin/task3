def count_chars(name):
    with open(name, 'r') as file:
        return (len(file.read()))
