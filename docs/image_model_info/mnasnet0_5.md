# mnasnet0_5 parameter information

**Number of layers: [ 158 ]**

**Number of parameters: [ 2.22M ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.46 | 22.15 | 10.76 | 0.63 | 
**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.97 | 95.31 | 3.69 | 0.02 | 

<img src="../figs/mnasnet0_5_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| layers.0.weight | (16, 3, 3, 3) | (16, 3, 3, 3) | 432 | Tensor rank 4 |
| layers.1.weight | (16,) | (16,) | 16 | Vector |
| layers.1.bias | (16,) | (16,) | 16 | Vector |
| layers.3.weight | (16, 1, 3, 3) | (16, 3, 3) | 144 | Tensor rank 3 |
| layers.4.weight | (16,) | (16,) | 16 | Vector |
| layers.4.bias | (16,) | (16,) | 16 | Vector |
| layers.6.weight | (8, 16, 1, 1) | (8, 16) | 128 | Matrix |
| layers.7.weight | (8,) | (8,) | 8 | Vector |
| layers.7.bias | (8,) | (8,) | 8 | Vector |
| layers.8.0.layers.0.weight | (24, 8, 1, 1) | (24, 8) | 192 | Matrix |
| layers.8.0.layers.1.weight | (24,) | (24,) | 24 | Vector |
| layers.8.0.layers.1.bias | (24,) | (24,) | 24 | Vector |
| layers.8.0.layers.3.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| layers.8.0.layers.4.weight | (24,) | (24,) | 24 | Vector |
| layers.8.0.layers.4.bias | (24,) | (24,) | 24 | Vector |
| layers.8.0.layers.6.weight | (16, 24, 1, 1) | (16, 24) | 384 | Matrix |
| layers.8.0.layers.7.weight | (16,) | (16,) | 16 | Vector |
| layers.8.0.layers.7.bias | (16,) | (16,) | 16 | Vector |
| layers.8.1.layers.0.weight | (48, 16, 1, 1) | (48, 16) | 768 | Matrix |
| layers.8.1.layers.1.weight | (48,) | (48,) | 48 | Vector |
| layers.8.1.layers.1.bias | (48,) | (48,) | 48 | Vector |
| layers.8.1.layers.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| layers.8.1.layers.4.weight | (48,) | (48,) | 48 | Vector |
| layers.8.1.layers.4.bias | (48,) | (48,) | 48 | Vector |
| layers.8.1.layers.6.weight | (16, 48, 1, 1) | (16, 48) | 768 | Matrix |
| layers.8.1.layers.7.weight | (16,) | (16,) | 16 | Vector |
| layers.8.1.layers.7.bias | (16,) | (16,) | 16 | Vector |
| layers.8.2.layers.0.weight | (48, 16, 1, 1) | (48, 16) | 768 | Matrix |
| layers.8.2.layers.1.weight | (48,) | (48,) | 48 | Vector |
| layers.8.2.layers.1.bias | (48,) | (48,) | 48 | Vector |
| layers.8.2.layers.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| layers.8.2.layers.4.weight | (48,) | (48,) | 48 | Vector |
| layers.8.2.layers.4.bias | (48,) | (48,) | 48 | Vector |
| layers.8.2.layers.6.weight | (16, 48, 1, 1) | (16, 48) | 768 | Matrix |
| layers.8.2.layers.7.weight | (16,) | (16,) | 16 | Vector |
| layers.8.2.layers.7.bias | (16,) | (16,) | 16 | Vector |
| layers.9.0.layers.0.weight | (48, 16, 1, 1) | (48, 16) | 768 | Matrix |
| layers.9.0.layers.1.weight | (48,) | (48,) | 48 | Vector |
| layers.9.0.layers.1.bias | (48,) | (48,) | 48 | Vector |
| layers.9.0.layers.3.weight | (48, 1, 5, 5) | (48, 5, 5) | 1200 | Tensor rank 3 |
| layers.9.0.layers.4.weight | (48,) | (48,) | 48 | Vector |
| layers.9.0.layers.4.bias | (48,) | (48,) | 48 | Vector |
| layers.9.0.layers.6.weight | (24, 48, 1, 1) | (24, 48) | 1152 | Matrix |
| layers.9.0.layers.7.weight | (24,) | (24,) | 24 | Vector |
| layers.9.0.layers.7.bias | (24,) | (24,) | 24 | Vector |
| layers.9.1.layers.0.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| layers.9.1.layers.1.weight | (72,) | (72,) | 72 | Vector |
| layers.9.1.layers.1.bias | (72,) | (72,) | 72 | Vector |
| layers.9.1.layers.3.weight | (72, 1, 5, 5) | (72, 5, 5) | 1800 | Tensor rank 3 |
| layers.9.1.layers.4.weight | (72,) | (72,) | 72 | Vector |
| layers.9.1.layers.4.bias | (72,) | (72,) | 72 | Vector |
| layers.9.1.layers.6.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| layers.9.1.layers.7.weight | (24,) | (24,) | 24 | Vector |
| layers.9.1.layers.7.bias | (24,) | (24,) | 24 | Vector |
| layers.9.2.layers.0.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| layers.9.2.layers.1.weight | (72,) | (72,) | 72 | Vector |
| layers.9.2.layers.1.bias | (72,) | (72,) | 72 | Vector |
| layers.9.2.layers.3.weight | (72, 1, 5, 5) | (72, 5, 5) | 1800 | Tensor rank 3 |
| layers.9.2.layers.4.weight | (72,) | (72,) | 72 | Vector |
| layers.9.2.layers.4.bias | (72,) | (72,) | 72 | Vector |
| layers.9.2.layers.6.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| layers.9.2.layers.7.weight | (24,) | (24,) | 24 | Vector |
| layers.9.2.layers.7.bias | (24,) | (24,) | 24 | Vector |
| layers.10.0.layers.0.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| layers.10.0.layers.1.weight | (144,) | (144,) | 144 | Vector |
| layers.10.0.layers.1.bias | (144,) | (144,) | 144 | Vector |
| layers.10.0.layers.3.weight | (144, 1, 5, 5) | (144, 5, 5) | 3600 | Tensor rank 3 |
| layers.10.0.layers.4.weight | (144,) | (144,) | 144 | Vector |
| layers.10.0.layers.4.bias | (144,) | (144,) | 144 | Vector |
| layers.10.0.layers.6.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| layers.10.0.layers.7.weight | (40,) | (40,) | 40 | Vector |
| layers.10.0.layers.7.bias | (40,) | (40,) | 40 | Vector |
| layers.10.1.layers.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| layers.10.1.layers.1.weight | (240,) | (240,) | 240 | Vector |
| layers.10.1.layers.1.bias | (240,) | (240,) | 240 | Vector |
| layers.10.1.layers.3.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| layers.10.1.layers.4.weight | (240,) | (240,) | 240 | Vector |
| layers.10.1.layers.4.bias | (240,) | (240,) | 240 | Vector |
| layers.10.1.layers.6.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| layers.10.1.layers.7.weight | (40,) | (40,) | 40 | Vector |
| layers.10.1.layers.7.bias | (40,) | (40,) | 40 | Vector |
| layers.10.2.layers.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| layers.10.2.layers.1.weight | (240,) | (240,) | 240 | Vector |
| layers.10.2.layers.1.bias | (240,) | (240,) | 240 | Vector |
| layers.10.2.layers.3.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| layers.10.2.layers.4.weight | (240,) | (240,) | 240 | Vector |
| layers.10.2.layers.4.bias | (240,) | (240,) | 240 | Vector |
| layers.10.2.layers.6.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| layers.10.2.layers.7.weight | (40,) | (40,) | 40 | Vector |
| layers.10.2.layers.7.bias | (40,) | (40,) | 40 | Vector |
| layers.11.0.layers.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| layers.11.0.layers.1.weight | (240,) | (240,) | 240 | Vector |
| layers.11.0.layers.1.bias | (240,) | (240,) | 240 | Vector |
| layers.11.0.layers.3.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| layers.11.0.layers.4.weight | (240,) | (240,) | 240 | Vector |
| layers.11.0.layers.4.bias | (240,) | (240,) | 240 | Vector |
| layers.11.0.layers.6.weight | (48, 240, 1, 1) | (48, 240) | 11520 | Matrix |
| layers.11.0.layers.7.weight | (48,) | (48,) | 48 | Vector |
| layers.11.0.layers.7.bias | (48,) | (48,) | 48 | Vector |
| layers.11.1.layers.0.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| layers.11.1.layers.1.weight | (288,) | (288,) | 288 | Vector |
| layers.11.1.layers.1.bias | (288,) | (288,) | 288 | Vector |
| layers.11.1.layers.3.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| layers.11.1.layers.4.weight | (288,) | (288,) | 288 | Vector |
| layers.11.1.layers.4.bias | (288,) | (288,) | 288 | Vector |
| layers.11.1.layers.6.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| layers.11.1.layers.7.weight | (48,) | (48,) | 48 | Vector |
| layers.11.1.layers.7.bias | (48,) | (48,) | 48 | Vector |
| layers.12.0.layers.0.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| layers.12.0.layers.1.weight | (288,) | (288,) | 288 | Vector |
| layers.12.0.layers.1.bias | (288,) | (288,) | 288 | Vector |
| layers.12.0.layers.3.weight | (288, 1, 5, 5) | (288, 5, 5) | 7200 | Tensor rank 3 |
| layers.12.0.layers.4.weight | (288,) | (288,) | 288 | Vector |
| layers.12.0.layers.4.bias | (288,) | (288,) | 288 | Vector |
| layers.12.0.layers.6.weight | (96, 288, 1, 1) | (96, 288) | 27648 | Matrix |
| layers.12.0.layers.7.weight | (96,) | (96,) | 96 | Vector |
| layers.12.0.layers.7.bias | (96,) | (96,) | 96 | Vector |
| layers.12.1.layers.0.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| layers.12.1.layers.1.weight | (576,) | (576,) | 576 | Vector |
| layers.12.1.layers.1.bias | (576,) | (576,) | 576 | Vector |
| layers.12.1.layers.3.weight | (576, 1, 5, 5) | (576, 5, 5) | 14400 | Tensor rank 3 |
| layers.12.1.layers.4.weight | (576,) | (576,) | 576 | Vector |
| layers.12.1.layers.4.bias | (576,) | (576,) | 576 | Vector |
| layers.12.1.layers.6.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| layers.12.1.layers.7.weight | (96,) | (96,) | 96 | Vector |
| layers.12.1.layers.7.bias | (96,) | (96,) | 96 | Vector |
| layers.12.2.layers.0.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| layers.12.2.layers.1.weight | (576,) | (576,) | 576 | Vector |
| layers.12.2.layers.1.bias | (576,) | (576,) | 576 | Vector |
| layers.12.2.layers.3.weight | (576, 1, 5, 5) | (576, 5, 5) | 14400 | Tensor rank 3 |
| layers.12.2.layers.4.weight | (576,) | (576,) | 576 | Vector |
| layers.12.2.layers.4.bias | (576,) | (576,) | 576 | Vector |
| layers.12.2.layers.6.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| layers.12.2.layers.7.weight | (96,) | (96,) | 96 | Vector |
| layers.12.2.layers.7.bias | (96,) | (96,) | 96 | Vector |
| layers.12.3.layers.0.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| layers.12.3.layers.1.weight | (576,) | (576,) | 576 | Vector |
| layers.12.3.layers.1.bias | (576,) | (576,) | 576 | Vector |
| layers.12.3.layers.3.weight | (576, 1, 5, 5) | (576, 5, 5) | 14400 | Tensor rank 3 |
| layers.12.3.layers.4.weight | (576,) | (576,) | 576 | Vector |
| layers.12.3.layers.4.bias | (576,) | (576,) | 576 | Vector |
| layers.12.3.layers.6.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| layers.12.3.layers.7.weight | (96,) | (96,) | 96 | Vector |
| layers.12.3.layers.7.bias | (96,) | (96,) | 96 | Vector |
| layers.13.0.layers.0.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| layers.13.0.layers.1.weight | (576,) | (576,) | 576 | Vector |
| layers.13.0.layers.1.bias | (576,) | (576,) | 576 | Vector |
| layers.13.0.layers.3.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| layers.13.0.layers.4.weight | (576,) | (576,) | 576 | Vector |
| layers.13.0.layers.4.bias | (576,) | (576,) | 576 | Vector |
| layers.13.0.layers.6.weight | (160, 576, 1, 1) | (160, 576) | 92160 | Matrix |
| layers.13.0.layers.7.weight | (160,) | (160,) | 160 | Vector |
| layers.13.0.layers.7.bias | (160,) | (160,) | 160 | Vector |
| layers.14.weight | (1280, 160, 1, 1) | (1280, 160) | 204800 | Matrix |
| layers.15.weight | (1280,) | (1280,) | 1280 | Vector |
| layers.15.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.1.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.1.bias | (1000,) | (1000,) | 1000 | Vector |

