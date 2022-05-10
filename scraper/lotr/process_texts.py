from nltk import tokenize
PRINT_LIMIT = 189
texts = ['The_Fellowship_Of_The_Ring.txt',
        'The_Two_Towers.txt',
        'The_Return_Of_The_King.txt']

mentions_gandalf = open('../data/gandalf_source.jsonl', 'w', encoding='utf-8')
num_lines_printed = 0
for text in texts:
    if num_lines_printed < PRINT_LIMIT + 5:
        print(f'Processing {text}...')
        read_text = open(f'./texts/{text}', 'r', encoding='iso-8859-1').read()
        tokens = tokenize.sent_tokenize(read_text)

        for token in tokens:
            if ('Gandalf' in token) and (len(token.split()) > 10):
                output = token.strip().replace('\"', '\\"')
                mentions_gandalf.write(f'{{"prompt":"", "completion":"{output}"}}\n')
                num_lines_printed += 1
                if num_lines_printed >= PRINT_LIMIT + 5:
                    break

mentions_gandalf.close()