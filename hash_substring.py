# python3

def read_input():
    input_text = input()
    if 'F' in input_text:
        input_file = input()
        input_file = "test/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    pattern = f.readline()
                    text = f.readline()
                    return pattern, text

            except FileNotFoundError:
                return print("File_not_found_error")

    if 'I' in input_text:
        pattern = input()
        text = input()
        return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_string(string):
    hashValue = 0
    for char in string:
        hashValue = (hashValue * 128 + ord(char)) % 257
    return hashValue

def get_occurrences(pattern, text):

    n = len(pattern)
    m = len(text)
    pattern_hash = hash_string(pattern)
    text_hash = hash_string(text[:len(pattern)])
    matches = []

    for i in range(m - n + 1):
        if pattern_hash == text_hash:
            if text[i:i+n] == pattern:
                matches.append(i)
        if i < m - n:
            text_hash = ((text_hash - ord(text[i]) * (128 ** (n - 1))) * 128 + ord(text[i+n])) % 257
    print_occurrences(matches)


if __name__ == '__main__':
    get_occurrences(*read_input())

