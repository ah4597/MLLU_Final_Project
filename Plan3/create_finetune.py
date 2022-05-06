import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.create(training_file="C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\data\gandalf_ao3_prepared.jsonl",
    model="davinci",)
