pip install --upgrade openai
export OPENAI_API_KEY="<MY_APT_KEYS>"
openai tools fine_tunes.prepare_data -f "C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\Plan3\data_emet_csv.csv"
openai api fine_tunes.create -t "C:\Users\fyqaw\Documents\NYU\2022-2023\DS203\finalProject\MLLU_Final_Project\Plan3\data_emet_tsv_prepared.jsonl" -m "davinci"
