def count_lines(name):
    with open(name, 'r') as file:
        return (len(file.readlines()))