import re
from nltk import tokenize

def main():

    with open("MLLU_Final_Project\Plan3\dialogue_emet.txt",
                "r",encoding="utf8") as f:
        data = f.readlines()
    #pat = r"<\|endoftext\|>Emet-Selch: (.+) <\|endoftext\|>"
    #temp = [re.search(pat, x).group(0) for x in data]
    temp = [x.replace("<\|endoftext\|>","").replace("Emet-Selch:","").replace("<|endoftext|>","").strip() for x in data]
    text_cleaned = tokenize.sent_tokenize(' '.join(temp))
    output = open("MLLU_Final_Project\Plan3\data_emet_tsv.tsv", "w")
    output.write("prompt\tcompletion\n")
    for item in text_cleaned:
        output.write(f"\t{item}\n")
    output.close()


if __name__ == '__main__':
    main()
