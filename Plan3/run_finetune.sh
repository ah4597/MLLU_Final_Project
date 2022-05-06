# pip install --upgrade openai
# set OPENAI_API_KEY=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
# openai tools fine_tunes.prepare_data -f C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\data\gandalf_ao3.tsv
openai api fine_tunes.create -t C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\data\Prepared\hermione_ao3_prepared.jsonl -m davinci
openai api fine_tunes.create -t C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\data\Prepared\emet_ao3_prepared.jsonl -m davinci
# openai api fine_tunes.create -t C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\data\Prepared\gandalf_dialogue_prepared.jsonl -m davinci
# openai api fine_tunes.create -t C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\data\Prepared\hermione_dialogue_prepared.jsonl -m davinci
