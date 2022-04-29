import csv

dialogue_hermione = open('dialogue_hermione.txt', 'w', encoding='utf-8')

with open('Dialogue.csv', newline='', encoding='iso-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Character ID'] == '3':
            dialogue_hermione.write(f'<|endoftext|>{row["Dialogue"]}<|endoftext|>\n')

dialogue_hermione.close()