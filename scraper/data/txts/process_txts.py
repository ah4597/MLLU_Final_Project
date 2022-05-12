#Takes a .txt file and converts it to a jsonl 
import sys

input_filename = sys.argv[1]

filename = input_filename[:input_filename.index('.txt')]
input = open(input_filename, 'r', encoding='utf-8')
output = open(f'../{filename}.jsonl', 'w', encoding='utf-8')


lines = input.readlines()

for line in lines:
    if len(line) > 0:
        output.write(f'{{"prompt":"", "completion":"{line.strip()}"}}\n')


input.close()
output.close()
