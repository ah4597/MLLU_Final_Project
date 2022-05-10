dialogue_emet = open('../data/dialogue_emet.jsonl', 'w', encoding='utf-8')

with open('dialogue_emet.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        dialogue_emet.write(f'{{"prompt":"", "completion":"{line.strip()}"}}\n')