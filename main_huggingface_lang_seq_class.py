import os
import json
from transformers import RobertaForSequenceClassification, BertConfig
from utils import *
from convert import Converter

modality = 'language'
task = 'sequence_classification'
model_name = 'roberta-base'

model = RobertaForSequenceClassification.from_pretrained(model_name)
model._require_grad = True

with open('./basic_info.json', 'r') as f:
    file_tree = json.load(f)
    DOC_PATH = file_tree['docs_path']
    JSON_PATH = file_tree['json_path']
    IMAGE_PATH = file_tree['image_path']
    JSON_NAME = file_tree['json_name']
    RANK_NAME = file_tree['rank_name']
    DOC_PATH = os.path.join(DOC_PATH, modality, task)
    RANK_PATH = os.path.join(DOC_PATH, RANK_NAME)
    JSON_PATH = os.path.join(JSON_PATH, modality, task)
    IMAGE_PATH = os.path.join(IMAGE_PATH, modality, task)
    
check_path(file_tree)

if not os.path.exists(JSON_PATH):
    os.makedirs(JSON_PATH)
if not os.path.exists(IMAGE_PATH):
    os.makedirs(IMAGE_PATH)
if not os.path.exists(DOC_PATH):
    os.makedirs(DOC_PATH)

num_layers = get_num_layers(model)
num_parameters = get_num_parameters(model, 'param2bit')
num_trainable_parameters = get_num_trainable_parameters(model, 'param2bit')
prop_table = generate_prop_form_table(model)
prop_param_table = generate_prop_param_table(model)
layer_table = generate_layer_table(model)

if not os.path.exists(os.path.join(JSON_PATH, JSON_NAME)):
    rank_json = {
        "top_param_models": {
                model_name: get_num_parameters(model, 'int')
        }
    }
    with open(os.path.join(JSON_PATH, JSON_NAME), 'w') as f:
        json.dump(rank_json, f, indent=4, sort_keys=True)
    
else:
    rank_json = json.load(open(os.path.join(JSON_PATH, JSON_NAME), 'r'))["top_param_models"]
    model_list = list(rank_json.keys())
    rank_json[model_name] = get_num_parameters(model, 'int')
    rank_json = dict(sorted(rank_json.items(), key=lambda x: x[1], reverse=True))
    rank_json = dict(list(rank_json.items()))
    rank_json = {
        "top_param_models": rank_json
    }
    with open(os.path.join(JSON_PATH, JSON_NAME), 'w') as f:
        json.dump(rank_json, f, indent=4, sort_keys=True)

rank_json = rank_json["top_param_models"]

rank_content = ['# Top parameter models\n\n']
rank_content.append('| Rank | Model | Number of parameters (unit: bytes) |\n')
rank_content.append('| --- | --- | --- |\n')
for idx, model in enumerate(rank_json.keys()):
    rank_content.append(f'| {idx+1} | <a href="{model}.md">{model}</a> | {converter.num2str(rank_json[model], "param2bit")} |\n')
    
with open(RANK_PATH, 'w') as f:
    for content in rank_content:
        f.write(content)

current_model_rank = list(rank_json.keys()).index(model_name) + 1

contents = ['# %s parameter information\n' % (model_name)]
contents.append('**Number of layers: [ %d ]**\n' % (num_layers))
contents.append('**Number of parameters: [ %s ] [Top %s ]**\n' % (num_parameters, f"<a href='./{RANK_NAME}'>Check rank</a>"))
contents.append('**Number of trainable parameters: [ %s ]**\n' % (num_trainable_parameters))
contents.append('**Proportional of each form** (%)\n')
contents.append(prop_table)
contents.append('\n**Proportional of parameters by form** (%)\n')
contents.append('\n' + prop_param_table)
contents.append('\n# Layer information\n')
contents.append('\n' + layer_table)

with open(os.path.join(DOC_PATH, f'{model_name}.md'), 'w') as f:
    for content in contents:
        f.write(content)
        f.write('\n')

os.system("git add . && git commit -m 'update' && git push origin master")