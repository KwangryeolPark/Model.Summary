# %%
import os
from torchvision.models import mobilenet_v3_large






model = mobilenet_v3_large()
model_name = 'mobilenet_v3_large'





DIR = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(DIR, 'docs', 'trainable_parameter_shapes', f'{model_name}.md')

file = '| Name | Shape | Form | \n| --- | --- | --- |\n'

count = 0
num_el = 0
form = {
    'vector': 0,
    'matrix': 0,
    'tensor': 0
}
form_count = {
    'vector': 0,
    'matrix': 0,
    'tensor': 0
}

for name, param in model.named_parameters():
    print(name, param.shape)
    count += 1
    num_el += param.numel()
    rank = len(param.shape)
    if rank == 1:
        file += f'| {name} | {param.shape} | Vector |\n'
        form['vector'] += 1
        form_count['vector'] += param.numel()
    elif rank == 2:
        file += f'| {name} | {param.shape} | Matrix |\n'
        form['matrix'] += 1
        form_count['matrix'] += param.numel()
    else:
        file += f'| {name} | {param.shape} | Tensor |\n'
        form['tensor'] += 1
        form_count['tensor'] += param.numel()
    
with open(DOC, 'w') as f:
    f.write(f'# {model_name}\n\n')
    f.write(f'**Total layers: {count}**\n\n')
    f.write(f'**Number of elements: {num_el}**\n\n')
    f.write(f'**Proportional of each form**\n\n')
    f.write(f'| Vector | Matrix | Tensor |\n | --- | --- | --- |\n')
    f.write(f'| %.2f | %.2f | %.2f |\n\n' % (100 * form["vector"]/count, 100 * form["matrix"]/count, 100 * form["tensor"]/count))
    f.write(f"**Proportional of each form's parameters**\n\n")
    f.write(f'| Vector | Matrix | Tensor |\n | --- | --- | --- |\n')
    f.write(f'| %.2f | %.2f | %.2f |\n\n' % (100 * form_count["vector"]/num_el, 100 * form_count["matrix"]/num_el, 100 * form_count["tensor"]/num_el))
    f.write(file)
    