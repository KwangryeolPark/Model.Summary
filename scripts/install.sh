#!/bin/bash

pip install \
    torch==2.1.0 \
    transformers=4.34.0 \
    torchsummary==1.5.1

python generate_basic_info.py