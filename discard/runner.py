from result_generation import *
from fprompt import *
import json

parser = argparse.ArgumentParser(
    description="Prompting a GPT-3/J model"
)

parser.add_argument(
    "data_dir",
    type=str,
    help="Directory containing the original tested dataset. Can be downloaded from GITHUB PAGE.", # TODO: Upload the github page
)

parser.add_argument(
    "model_used",
    type=str,
    help="The name of model which will be used.", # TODO
)

args = parser.parse_args()

prompts = text2prompt(f"{args.data_dir}/prompts.jsonl")

if args.model_used in "gpt-3":
    completion = run_gpt3(prompts)
elif args.model_used in "gpt-j":
    completion = run_gptj6B(prompts)
else:
    print("Nothing happened, please check the model input") # TODO: raise error here

output = open("result.txt","w")
output.writelines(completions)
output.close()
