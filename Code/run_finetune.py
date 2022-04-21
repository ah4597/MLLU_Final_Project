from transformers import DataCollatorForLanguageModeling
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json
import argparse
import random
from characterDataset import *


parser = argparse.ArgumentParser(
    description="Finetuning a GPT-J model"
)
parser.add_argument(
    "data_dir",
    type=str,
    help="Directory containing the original tested dataset. Can be downloaded from GITHUB PAGE.", # TODO: Upload the github page
)
parser.add_argument(
    "ds_config",
    type=str,
    help="DeepSpeed configuration file.", # TODO: Upload the github page
)

args = parser.parse_args()
ds_config_dict = json.loads(args.ds_config)
with open(f"{args.data_dir}/dialogue_emet.txt") as f:
    data = f.readlines()

tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/tiny-random-gptj")
tokenizer.pad_token = tokenizer.eos_token
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm_probability=0.15)

if torch.cuda.is_available():
    model =  AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16, deepspeed=ds_config_dict).cuda()
else:
    model =  AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16, deepspeed=ds_config_dict, low_cpu_mem_usage=True)

random.seed(7)
random.shuffle(data)
n = int(len(data)*0.8)
train_data = characterDataset(data[:n], tokenizer)
val_data = characterDataset(data[n:], tokenizer)

trainArgs = transformers.TrainingArguments(evaluation_strategy="steps",
                                    eval_steps=500,
                                    save_strategy="epoch",
                                    num_train_epochs=5,
                                    logging_dir="/scratch/${USER}/",
                                    logging_strategy="epoch",
                                    learning_rate=2e-5,
                                    seed=7,
                                    load_best_model_at_end=True)

trainer = transformer.Trainer(TrainingArguments=trainArgs,
                    model=model,
                    train_dataset=train_data,
                    eval_dataset=val_data,
                    data_collator=data_collator)

trainer.train()

prompt = ("Why did the Amaurot ruined?")
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.8,
    max_length=200)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)