import json
import pandas as pd
import os

# desitination format {"image": , "converstaions": }

vqas_path = '/home/bossjobai/LLM_Projects/codes_kelvin/slake_chest/output_size_224/split/clean/train/filter_vqa.jsonl'
ori_path = '/home/bossjobai/LLM_Projects/codes_kelvin/slake_chest/output_size_224/split/clean/train/train.csv'


q_type_prompts = {
    'open_ended_questions': 'Input an open-ended question, and the assistant will output its answer with a detailed reason and corresponding visual location.', 
    'closed_ended_questions': 'Input a closed-ended question, and the assistant will output its answer (yes or no) with a detailed reason and corresponding visual location.',
    'single_choice_questions': 'Input a single-choice question, and the assistant will output its answer (an option) with a detailed reason and corresponding visual location.',
    'multi_choice_questions': 'Input a multi-choice question, and the assistant will output its answer (some options) with a detailed reason and corresponding visual location.'
}
ori_file = pd.read_csv(ori_path)
images_list = ori_file['mimic_image_file_path']

vqas = []
with open(vqas_path, 'r') as file:
    for line in file:
        # Parsing the JSON string into a dict and appending to the list of results
        json_object = json.loads(line.strip())
        vqas.append(json_object)

assert len(ori_file) == len(vqas)


final_vqas = []
for idx, vqa in enumerate(vqas):
    for key, values in vqa.items():
        if key not in q_type_prompts:
            raise ValueError("Wrong question types.")
        for data in values:
            temp = {"conversations": []}
            temp["row_id"] = idx
            temp["q_type"] = key
            temp["type_prompt"] = q_type_prompts[key]
            choices = data.get('choices', None)
            conv_human = {"from": "human", "value":f"<image>\n{data['question']}"}
            if choices is not None:
                choices_str = "["+ ", ".join(choices)  + "]"
                conv_human["value"] += " <choices>: " + choices_str
            conv_gpt = {"from": "gpt", "value": f"<answer> {data['answer']} <reason> {data['reason']} <location> {data['visual_locations']}"}
            temp["conversations"].append(conv_human)
            temp["conversations"].append(conv_gpt)
            temp["image"] = images_list.iloc[idx]
            final_vqas.append(temp)


print(len(vqas))
print(len(final_vqas))

with open('/home/bossjobai/LLM_Projects/codes_kelvin/slake_chest/output_size_224/split/clean/train/instruct_slake_train_data.json', 'w', encoding='utf-8') as f:
    json.dump(final_vqas, f, ensure_ascii=False)