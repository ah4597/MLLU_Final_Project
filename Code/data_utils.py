import re
from nltk import tokenize

def preprocess(text):
    pat = r"<\|endoftext\|>Emet-Selch: (.+) <\|endoftext\|>"
    temp = [re.search(pat, x).group[0] for x in text]
    text_cleaned = tokenize.sent_tokenize(' '.join(temp))
    return text_cleaned


def encode_data(data, tokenizer, max_seq_length=128):

    temp = tokenizer(data,
                    padding="max_length",
                    truncation=True,
                    max_length=max_seq_length,
                    return_offsets_mapping=True,
                    return_tensors = "pt")

    input_ids = temp["input_ids"]
    attention_mask = temp["attention_mask"]

    return input_ids, attention_mask
