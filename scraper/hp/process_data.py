import csv
PRINT_LIMIT = 189

dialogue_hermione = open('../data/hermione_source.jsonl', 'w', encoding='utf-8')
num_lines_printed = 0
with open('Dialogue.csv', newline='', encoding='iso-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Character ID'] == '3':
            output = row["Dialogue"].strip().replace('\"', '\\"')
            dialogue_hermione.write(f'{{"prompt":"", "completion":"{output}"}}\n')
            num_lines_printed += 1
            if num_lines_printed >= PRINT_LIMIT:
                break

dialogue_hermione.close()