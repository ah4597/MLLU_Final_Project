dialogue_emet = open('../data/emet_source.jsonl', 'w', encoding='utf-8')

with open('dialogue_emet.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        output = line.strip().replace('\"', '\\"')
        dialogue_emet.write(f'{{"prompt":"", "completion":"{output}"}}\n')