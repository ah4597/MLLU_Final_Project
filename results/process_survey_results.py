import csv
import math
import sys

class Model:
    def __init__(self, model_name):
        self.model_name = model_name
        self.prompt_1_qa_total = 0
        self.prompt_2_qa_total = 0
        self.prompt_3_qa_total = 0
        self.prompt_4_qa_total = 0
        self.prompt_5_qa_total = 0

        self.prompt_1_grammar_total = 0
        self.prompt_2_grammar_total = 0
        self.prompt_3_grammar_total = 0
        self.prompt_4_grammar_total = 0
        self.prompt_5_grammar_total = 0
        self.prompt_1_plausible_total = 0
        self.prompt_2_plausible_total = 0
        self.prompt_3_plausible_total = 0
        self.prompt_4_plausible_total = 0
        self.prompt_5_plausible_total = 0

        self.ranking_total = 0


def initialize_models():
    model_names = [
        'emet_source',
        'hermione_source',
        'gandalf_source',
        'emet_ao3',
        'hermione_ao3',
        'gandalf_ao3',
        'emet_combined',
        'hermione_combined',
        'gandalf_combined',
        'emet_baseline',
        'hermione_baseline',
        'gandalf_baseline'
    ]

    models = {}
    for i in range(len(model_names)):
        models[model_names[i]] = Model(model_names[i])

    return models

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Error. Incorrage Usage. To run: python process_survey_results.py <results_file.csv>')

    results_filename = sys.argv[1]
    model_key = ['baseline', 'source', 'ao3', 'combined']
    char_key = ['emet', 'hermione', 'gandalf']

    ordering_key = [
        [
            [1, 3, 2, 0],
            [1, 0, 2, 3],
            [1, 3, 2, 0],
            [2, 0, 3, 1],
            [3, 2, 1, 0]
        ],
        [
            [1, 2, 0, 3],
            [2, 3, 1, 0],
            [1, 3, 2, 0],
            [3, 1, 0, 2],
            [1, 0, 3, 2]
        ],
        [
            [0, 2, 1, 3],
            [3, 2, 1, 0],
            [1, 2, 3, 0],
            [3, 0, 1, 2],
            [2, 0, 1, 3]
        ]
    ]

    output = open('results.txt', 'w', encoding='utf-8')

    models = initialize_models()
    num_participants = len(open(results_filename, 'r', encoding='utf-8').readlines()) - 1
    with open(results_filename, newline= "", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] == "Timestamp":
                continue

            index = 0
            num_baseline = 0
            for cur_char_num in range(3):
                cur_char = char_key[cur_char_num]
                for cur_prompt_num in range(5):
                    for cur_qa_num in range(8):
                        index += 1

                        key = math.floor(cur_qa_num/2)
                        actual_qa_num = ordering_key[cur_char_num][cur_prompt_num][key]
                        current_model = model_key[actual_qa_num]

                        if row[index] == 'Yes':
                            setattr(models[f'{cur_char}_{current_model}'],
                                    f'prompt_{cur_prompt_num+1}_qa_total',
                                    getattr(models[f'{cur_char}_{current_model}'],
                                            f'prompt_{cur_prompt_num+1}_qa_total') + 1
                            )
                            if index%2 == 1:
                                setattr(models[f'{cur_char}_{current_model}'],
                                        f'prompt_{cur_prompt_num+1}_grammar_total',
                                        getattr(models[f'{cur_char}_{current_model}'],
                                                f'prompt_{cur_prompt_num+1}_grammar_total') + 1
                                )
                            else:
                                setattr(models[f'{cur_char}_{current_model}'],
                                    f'prompt_{cur_prompt_num+1}_plausible_total',
                                    getattr(models[f'{cur_char}_{current_model}'],
                                            f'prompt_{cur_prompt_num+1}_plausible_total') + 1
                                )

                    for cur_ranking_num in range(4):
                        index += 1
                        key = cur_ranking_num
                        actual_num = ordering_key[cur_char_num][cur_prompt_num][key]
                        current_model = model_key[actual_num]
                        models[f'{cur_char}_{current_model}'].ranking_total += int(row[index])



    overall_model_nums = {
        'source': {
            'prompt_1_qa_total': 0,
            'prompt_2_qa_total': 0,
            'prompt_3_qa_total': 0,
            'prompt_4_qa_total': 0,
            'prompt_5_qa_total': 0,
            'prompt_1_grammar_total': 0,
            'prompt_2_grammar_total': 0,
            'prompt_3_grammar_total': 0,
            'prompt_4_grammar_total': 0,
            'prompt_5_grammar_total': 0,
            'prompt_1_plausible_total': 0,
            'prompt_2_plausible_total': 0,
            'prompt_3_plausible_total': 0,
            'prompt_4_plausible_total': 0,
            'prompt_5_plausible_total': 0,
            'ranking_total': 0
        },
        'ao3' : {
            'prompt_1_qa_total': 0,
            'prompt_2_qa_total': 0,
            'prompt_3_qa_total': 0,
            'prompt_4_qa_total': 0,
            'prompt_5_qa_total': 0,
            'prompt_1_grammar_total': 0,
            'prompt_2_grammar_total': 0,
            'prompt_3_grammar_total': 0,
            'prompt_4_grammar_total': 0,
            'prompt_5_grammar_total': 0,
            'prompt_1_plausible_total': 0,
            'prompt_2_plausible_total': 0,
            'prompt_3_plausible_total': 0,
            'prompt_4_plausible_total': 0,
            'prompt_5_plausible_total': 0,
            'ranking_total': 0
        },
        'combined' : {
            'prompt_1_qa_total': 0,
            'prompt_2_qa_total': 0,
            'prompt_3_qa_total': 0,
            'prompt_4_qa_total': 0,
            'prompt_5_qa_total': 0,
            'prompt_1_grammar_total': 0,
            'prompt_2_grammar_total': 0,
            'prompt_3_grammar_total': 0,
            'prompt_4_grammar_total': 0,
            'prompt_5_grammar_total': 0,
            'prompt_1_plausible_total': 0,
            'prompt_2_plausible_total': 0,
            'prompt_3_plausible_total': 0,
            'prompt_4_plausible_total': 0,
            'prompt_5_plausible_total': 0,
            'ranking_total': 0
        },
        'baseline' : {
            'prompt_1_qa_total': 0,
            'prompt_2_qa_total': 0,
            'prompt_3_qa_total': 0,
            'prompt_4_qa_total': 0,
            'prompt_5_qa_total': 0,
            'prompt_1_grammar_total': 0,
            'prompt_2_grammar_total': 0,
            'prompt_3_grammar_total': 0,
            'prompt_4_grammar_total': 0,
            'prompt_5_grammar_total': 0,
            'prompt_1_plausible_total': 0,
            'prompt_2_plausible_total': 0,
            'prompt_3_plausible_total': 0,
            'prompt_4_plausible_total': 0,
            'prompt_5_plausible_total': 0,
            'ranking_total': 0
        }
    }

    for model in models.values():
      
        if 'source' in model.model_name:
            cur_model = 'source'
        elif 'ao3' in model.model_name:
            cur_model = 'ao3'
        elif 'combined' in model.model_name:
            cur_model = 'combined'
        else:
            cur_model = 'baseline'
        
        model.average_ranking = model.ranking_total / (num_participants * 5)

        model.prompt_1_qa_average = model.prompt_1_qa_total / num_participants
        model.prompt_2_qa_average = model.prompt_2_qa_total / num_participants
        model.prompt_3_qa_average = model.prompt_3_qa_total / num_participants
        model.prompt_4_qa_average = model.prompt_4_qa_total / num_participants
        model.prompt_5_qa_average = model.prompt_5_qa_total / num_participants
        
        model.prompt_1_grammar_average = model.prompt_1_grammar_total / num_participants
        model.prompt_2_grammar_average = model.prompt_2_grammar_total / num_participants
        model.prompt_3_grammar_average = model.prompt_3_grammar_total / num_participants
        model.prompt_4_grammar_average = model.prompt_4_grammar_total / num_participants
        model.prompt_5_grammar_average = model.prompt_5_grammar_total / num_participants

        model.prompt_1_plausible_average = model.prompt_1_plausible_total / num_participants
        model.prompt_2_plausible_average = model.prompt_2_plausible_total / num_participants
        model.prompt_3_plausible_average = model.prompt_3_plausible_total / num_participants
        model.prompt_4_plausible_average = model.prompt_4_plausible_total / num_participants
        model.prompt_5_plausible_average = model.prompt_5_plausible_total / num_participants

        model.overall_qa_average = (model.prompt_1_qa_total + model.prompt_2_qa_total + model.prompt_3_qa_total + model.prompt_4_qa_total + model.prompt_5_qa_total) / (num_participants * 5)
        model.overall_grammar_average = (model.prompt_1_grammar_total + model.prompt_2_grammar_total + model.prompt_3_grammar_total + model.prompt_4_grammar_total + model.prompt_5_grammar_total) / (num_participants * 5)
        model.overall_plausible_average = (model.prompt_1_plausible_total + model.prompt_2_plausible_total + model.prompt_3_plausible_total + model.prompt_4_plausible_total + model.prompt_5_plausible_total) / (num_participants * 5)


        overall_model_nums[cur_model]['ranking_total'] += model.ranking_total

        overall_model_nums[cur_model]['prompt_1_qa_total'] += model.prompt_1_qa_total
        overall_model_nums[cur_model]['prompt_2_qa_total'] += model.prompt_2_qa_total
        overall_model_nums[cur_model]['prompt_3_qa_total'] += model.prompt_3_qa_total
        overall_model_nums[cur_model]['prompt_4_qa_total'] += model.prompt_4_qa_total
        overall_model_nums[cur_model]['prompt_5_qa_total'] += model.prompt_5_qa_total

        overall_model_nums[cur_model]['prompt_1_grammar_total'] += model.prompt_1_grammar_total
        overall_model_nums[cur_model]['prompt_2_grammar_total'] += model.prompt_2_grammar_total
        overall_model_nums[cur_model]['prompt_3_grammar_total'] += model.prompt_3_grammar_total
        overall_model_nums[cur_model]['prompt_4_grammar_total'] += model.prompt_4_grammar_total
        overall_model_nums[cur_model]['prompt_5_grammar_total'] += model.prompt_5_grammar_total
        overall_model_nums[cur_model]['prompt_1_plausible_total'] += model.prompt_1_plausible_total
        overall_model_nums[cur_model]['prompt_2_plausible_total'] += model.prompt_2_plausible_total
        overall_model_nums[cur_model]['prompt_3_plausible_total'] += model.prompt_3_plausible_total
        overall_model_nums[cur_model]['prompt_4_plausible_total'] += model.prompt_4_plausible_total
        overall_model_nums[cur_model]['prompt_5_plausible_total'] += model.prompt_5_plausible_total
            
    for overall_model in overall_model_nums.values():
        overall_model['prompt_1_qa_average'] = overall_model['prompt_1_qa_total'] / (num_participants * 3)
        overall_model['prompt_2_qa_average'] = overall_model['prompt_2_qa_total'] / (num_participants * 3)
        overall_model['prompt_3_qa_average'] = overall_model['prompt_3_qa_total'] / (num_participants * 3)
        overall_model['prompt_4_qa_average'] = overall_model['prompt_4_qa_total'] / (num_participants * 3)
        overall_model['prompt_5_qa_average'] = overall_model['prompt_5_qa_total'] / (num_participants * 3)

        overall_model['prompt_1_grammar_average'] = overall_model['prompt_1_grammar_total'] / (num_participants * 3)
        overall_model['prompt_2_grammar_average'] = overall_model['prompt_2_grammar_total'] / (num_participants * 3)
        overall_model['prompt_3_grammar_average'] = overall_model['prompt_3_grammar_total'] / (num_participants * 3)
        overall_model['prompt_4_grammar_average'] = overall_model['prompt_4_grammar_total'] / (num_participants * 3)
        overall_model['prompt_5_grammar_average'] = overall_model['prompt_5_grammar_total'] / (num_participants * 3)
        overall_model['prompt_1_plausible_average'] = overall_model['prompt_1_plausible_total'] / (num_participants * 3)
        overall_model['prompt_2_plausible_average'] = overall_model['prompt_2_plausible_total'] / (num_participants * 3)
        overall_model['prompt_3_plausible_average'] = overall_model['prompt_3_plausible_total'] / (num_participants * 3)
        overall_model['prompt_4_plausible_average'] = overall_model['prompt_4_plausible_total'] / (num_participants * 3)
        overall_model['prompt_5_plausible_average'] = overall_model['prompt_5_plausible_total'] / (num_participants * 3)

        overall_model['overall_grammar_average'] = (overall_model['prompt_1_grammar_total'] + overall_model['prompt_2_grammar_total'] + overall_model['prompt_3_grammar_total'] + overall_model['prompt_4_grammar_total'] + overall_model['prompt_5_grammar_total']) / (num_participants * 3 * 5)
        overall_model['overall_plausible_average'] = (overall_model['prompt_1_plausible_total'] + overall_model['prompt_2_plausible_total'] + overall_model['prompt_3_plausible_total'] + overall_model['prompt_4_plausible_total'] + overall_model['prompt_5_plausible_total']) / (num_participants * 3 * 5)
        overall_model['overall_qa_average'] = (overall_model['prompt_1_qa_total'] + overall_model['prompt_2_qa_total'] + overall_model['prompt_3_qa_total'] + overall_model['prompt_4_qa_total'] + overall_model['prompt_5_qa_total']) / (num_participants * 3 * 5)
        overall_model['average_ranking'] = overall_model['ranking_total'] / (num_participants * 3 * 5)



    # OUTPUT RESULTS
    for model in models.values():
        output.write(model.model_name + '\n')
        for i in range(1, 6):
            output.write(f'Prompt {i} answer average QA score: ' + str(round(getattr(model, f'prompt_{i}_qa_average'), 2)) + '\n')
            output.write(f'Prompt {i} answer average grammar score: ' + str(round(getattr(model, f'prompt_{i}_grammar_average'), 2)) + '\n')
            output.write(f'Prompt {i} answer average plausible score: ' + str(round(getattr(model, f'prompt_{i}_plausible_average'), 2)) + '\n')
        output.write(f'Overall average QA score: {model.overall_qa_average: .2f}\n')
        output.write(f'Overall average grammar score: {model.overall_grammar_average: .2f}\n')
        output.write(f'Overall average plausibile score: {model.overall_plausible_average: .2f}\n')
        output.write(f'Average Ranking (Lower is better, 1=Best): {model.average_ranking: .2f}\n\n')

    for overall_model_name in overall_model_nums:
        overall_model = overall_model_nums[overall_model_name]
        output.write(f'All models based on {overall_model_name}\n')
        for i in range(1, 6):
            output.write(f'Prompt {i} answer average QA score: {overall_model[f"prompt_{i}_qa_average"]: .2f}\n')
            output.write(f'Prompt {i} answer average grammar score: {overall_model[f"prompt_{i}_grammar_average"]: .2f}\n')
            output.write(f'Prompt {i} answer average plausible score: {overall_model[f"prompt_{i}_plausible_average"]: .2f}\n')
        output.write(f'Overall average QA score: {overall_model["overall_qa_average"]: .2f}\n')
        output.write(f'Overall average grammar score: {overall_model["overall_grammar_average"]: .2f}\n')
        output.write(f'Overall average plausible score: {overall_model["overall_plausible_average"]: .2f}\n')
        output.write(f'Average Ranking (Lower is better, 1=Best): {overall_model["average_ranking"]: .2f}\n\n')
        