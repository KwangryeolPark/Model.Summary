import os
from transformers import T5ForConditionalGeneration, T5Tokenizer
from utils import *

model_name = 't5-11b'
model = T5ForConditionalGeneration.from_pretrained(model_name)

DIR = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(DIR, 'docs', 'image_model_info', f'{model_name}.md')

contents = ['# %s parameter information\n' % (model_name)]

contents.append('**Number of layers: [ %d ]**\n' % (get_num_layers(model)))
contents.append('**Number of parameters: [ %s ]**\n' % (get_num_parameters(model, 'str')))
contents.append('**Proportional of each form** (%)\n')
contents.append(generate_prop_form_table(model))
contents.append('\n**Proportional of parameters by form** (%)\n')
contents.append('\n' + generate_prop_param_table(model))
contents.append('\n' + generate_params_pie_chart_by_form(model, model_name))
contents.append('\n**Layer information**\n')
contents.append('\n' + generate_layer_table(model))

os.makedirs(os.path.dirname(DOC), exist_ok=True)
with open(DOC, 'w') as f:
    for content in contents:
        f.write(content)
        f.write('\n')
