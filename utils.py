import matplotlib.pyplot as plt
import os

def get_num_layers(model):
    num_layers = 0
    for _, _ in model.named_parameters():
        num_layers += 1
    return num_layers
    

def get_num_parameters(model, type:str='str'):
    num_param = 0
    for _, param in model.named_parameters():
        num_param += param.numel()
    
    if type == 'str':
        return _convert_digit(num_param)
    return num_param

def get_num_layers_by_form(model):
    form = {
        '0.Vector': 0,
        '1.Matrix': 0,
    }

    for _, param in model.named_parameters():
        real_shape = param.squeeze().shape
        rank = len(real_shape)
        if rank == 1:
            form['0.Vector'] += 1
        elif rank == 2:
            form['1.Matrix'] += 1
        else:
            key = f'2.Tensor rank {rank}'
            if key not in form.keys():
                form[key] = 0
            form[key] += 1
    
    keys = list(form.keys())
    keys.sort()
    form = {key: form[key] for key in keys}
    return form            

def get_num_parameters_by_form(model):
    form = {
        '0.Vector': 0,
        '1.Matrix': 0,
    }

    for _, param in model.named_parameters():
        real_shape = param.squeeze().shape
        rank = len(real_shape)
        if rank == 1:
            form['0.Vector'] += param.numel()
        elif rank == 2:
            form['1.Matrix'] += param.numel()
        else:
            key = f'2.Tensor rank {rank}'
            if key not in form.keys():
                form[key] = 0
            form[key] += param.numel()

    keys = list(form.keys())
    keys.sort()
    form = {key: form[key] for key in keys}
    return form            

def generate_prop_form_table(model):
    forms = get_num_layers_by_form(model)
    num_layers = get_num_layers(model)
    
    table = '| '

    for form in forms.keys():
        form = form.split('.')[1]
        table += f'{form} | '

    table += '\n| '
    for _ in forms.keys():
        table += ' --- |'
    
    table += '\n| '
    for value in forms.values():
        table += f'{100 * value/num_layers:.2f} | '
    
    return table

def generate_prop_param_table(model):
    forms = get_num_parameters_by_form(model)
    num_params = get_num_parameters(model, 'int')
    
    table = '| '

    for form in forms.keys():
        form = form.split('.')[1]
        table += f'{form} | '

    table += '\n| '
    for _ in forms.keys():
        table += ' --- |'
    
    table += '\n| '
    for value in forms.values():
        table += f'{100 * value/num_params:.2f} | '
    
    return table

def generate_layer_table(model):
    contents = '| Name | Shape | Squeezed shape | Number of parameters | Form |\n'
    contents += '| --- | --- | --- | --- | --- |\n'
    for name, param in model.named_parameters():
        real_shape = tuple(param.squeeze().shape)
        rank = len(real_shape)
        if rank == 1:
            contents += f'| {name} | {tuple(param.shape)} | {real_shape} | {param.numel()} | Vector |\n'
        elif rank == 2:
            contents += f'| {name} | {tuple(param.shape)} | {real_shape} | {param.numel()} | Matrix |\n'
        else:
            key = f'Tensor rank {rank}'
            contents += f'| {name} | {tuple(param.shape)} | {real_shape} | {param.numel()} | {key} |\n'
        
    
    return contents

def generate_params_pie_chart_by_form(model, model_name=None):
    form = get_num_parameters_by_form(model)
    labels = list(form.keys())
    sizes = list(form.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    
    assert model_name is not None, 'Please provide model_name'
    
    DIR = os.path.dirname(os.path.abspath(__file__))
    DOC = os.path.join(DIR, 'docs', 'figs')
    PATH = os.path.join(DOC, f'{model_name}_pie_chart.png')
    
    os.makedirs(DOC, exist_ok=True)
    fig.savefig(PATH)

    content = f'<img src="PATH" alt="pie_chart" width="500"/>'
    return content
    
def _convert_digit(num):
    if num < 1000:
        return str(num)
    elif num < 1000**2:
        return f'{num/1000:.2f}K'
    elif num < 1000**3:
        return f'{num/1000**2:.2f}M'
    elif num < 1000**4:
        return f'{num/1000**3:.2f}G'
    return f'{num/1000**4:.2f}T'