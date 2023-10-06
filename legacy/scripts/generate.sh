#!/bin/bash

for model in "alexnet" convnext_tiny convnext_small convnext_base convnext_large efficientnet_b0 efficientnet_b1 efficientnet_b2 efficientnet_b3 efficientnet_b4 efficientnet_b5 efficientnet_b6 efficientnet_b7 efficientnet_v2_s efficientnet_v2_m efficientnet_v2_l "vgg11" "vgg11_bn" "vgg13" "vgg13_bn" "vgg16" "vgg16_bn" "vgg19" "vgg19_bn" vit_b_16 vit_b_32 vit_l_16 vit_l_32 vit_h_14 maxvit_t resnet18 resnet34 resnet50 resnet101 resnet152 squeezenet1_0 squeezenet1_1 swin_t swin_v2_t swin_v2_s swin_v2_b densenet121 swin_s swin_b densenet169 densenet161 densenet201 inception_v3 googlenet shufflenet_v2_x0_5 shufflenet_v2_x1_0 shufflenet_v2_x1_5 shufflenet_v2_x2_0 mobilenet_v2 mobilenet_v3_large regnet_x_16gf regnet_x_32gf regnet_y_16gf regnet_x_8gf regnet_x_3_2gf regnet_x_1_6gf regnet_y_128gf regnet_x_800mf regnet_x_400mf regnet_y_32gf regnet_y_800mf regnet_y_8gf regnet_y_1_6gf regnet_y_3_2gf mobilenet_v3_small resnext50_32x4d resnext101_64x4d resnext101_32x8d wide_resnet50_2 wide_resnet101_2 mnasnet0_5 mnasnet0_75 mnasnet1_0 mnasnet1_3 regnet_y_400mf
do
    # echo Generating $model
    python main.py --model=$model &
done

echo done