from nltk import tokenize

texts = ['The_Fellowship_Of_The_Ring.txt',
        'The_Two_Towers.txt',
        'The_Return_Of_The_King.txt']

mentions_gandalf = open('gandalf.txt', 'w', encoding='utf-8')
for text in texts:
    print(f'Processing {text}...')
    read_text = open(f'./texts/{text}', 'r', encoding='iso-8859-1').read()
    tokens = tokenize.sent_tokenize(read_text)

    for token in tokens:
        if 'Gandalf' in token:
            mentions_gandalf.write(f'<|endoftext|>{token}<|endoftext|>\n')

    mentions_gandalf.write('\n')

mentions_gandalf.close()