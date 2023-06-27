import os
import argparse
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, help='model name', required=True)
args = parser.parse_args()

DIR = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(DIR, 'docs', 'image_model_info', f'{args.model}.md')

module = __import__('torchvision.models', fromlist=['*'])
model = getattr(module, args.model)()

contents = ['# %s parameter information\n' % (args.model)]
contents.append('**Number of layers: [ %d ]**\n' % (get_num_layers(model)))
contents.append('**Number of parameters: [ %s ]**\n' % (get_num_parameters(model, 'str')))
contents.append('**Proportional of each form** (%)\n')
contents.append(generate_prop_form_table(model))
contents.append('\n' + generate_prop_param_table(model))
contents.append('\n' + generate_params_pie_chart_by_form(model, args.model))
contents.append('\n**Layer information**\n')
contents.append('\n' + generate_layer_table(model))

os.makedirs(os.path.dirname(DOC), exist_ok=True)
with open(DOC, 'w') as f:
    for content in contents:
        f.write(content)
        f.write('\n')
