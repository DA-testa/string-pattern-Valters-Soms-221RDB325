def read_input():
    input_format = input().upper().rstrip()
    if 'F' in input_format:
        input_file = '06'
        input_file = "tests/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    pattern = f.readline().rstrip()
                    text = f.readline().rstrip()
            except FileNotFoundError:
                return "File not found error"

    elif input_format == 'I':
        pattern = input().rstrip()
        text = input().rstrip()

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

    return matches

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))