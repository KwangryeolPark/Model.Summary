#!/bin/bash

for model in "alexnet" "vgg11" "vgg11_bn" "vgg13" "vgg13_bn" "vgg16" "vgg16_bn" "vgg19" "vgg19_bn" resnet18 resnet34 resnet50 resnet101 resnet152 squeezenet1_0 squeezenet1_1 densenet121 densenet169 densenet161 densenet201 inception_v3 googlenet shufflenet_v2_x0_5 shufflenet_v2_x1_0 shufflenet_v2_x1_5 shufflenet_v2_x2_0 mobilenet_v2 resnext50_32x4d resnext101_32x8d wide_resnet50_2 wide_resnet101_2 mnasnet0_5 mnasnet0_75 mnasnet1_0 mnasnet1_3
do
    echo Genearte $model
    python main.py --model=$model
done