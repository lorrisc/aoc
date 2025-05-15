def read_file(file_path, strip = False):
    with open(file_path, 'r') as file:
        if strip:
            return file.read().strip()
        return file.read()