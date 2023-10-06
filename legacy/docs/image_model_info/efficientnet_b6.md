# efficientnet_b6 parameter information

**Number of layers: [ 584 ]**

**Number of parameters: [ 43.04M ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.47 | 30.65 | 7.71 | 0.17 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.65 | 97.05 | 2.30 | 0.00 | 

<img src="../figs/efficientnet_b6_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| features.0.0.weight | (56, 3, 3, 3) | (56, 3, 3, 3) | 1512 | Tensor rank 4 |
| features.0.1.weight | (56,) | (56,) | 56 | Vector |
| features.0.1.bias | (56,) | (56,) | 56 | Vector |
| features.1.0.block.0.0.weight | (56, 1, 3, 3) | (56, 3, 3) | 504 | Tensor rank 3 |
| features.1.0.block.0.1.weight | (56,) | (56,) | 56 | Vector |
| features.1.0.block.0.1.bias | (56,) | (56,) | 56 | Vector |
| features.1.0.block.1.fc1.weight | (14, 56, 1, 1) | (14, 56) | 784 | Matrix |
| features.1.0.block.1.fc1.bias | (14,) | (14,) | 14 | Vector |
| features.1.0.block.1.fc2.weight | (56, 14, 1, 1) | (56, 14) | 784 | Matrix |
| features.1.0.block.1.fc2.bias | (56,) | (56,) | 56 | Vector |
| features.1.0.block.2.0.weight | (32, 56, 1, 1) | (32, 56) | 1792 | Matrix |
| features.1.0.block.2.1.weight | (32,) | (32,) | 32 | Vector |
| features.1.0.block.2.1.bias | (32,) | (32,) | 32 | Vector |
| features.1.1.block.0.0.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| features.1.1.block.0.1.weight | (32,) | (32,) | 32 | Vector |
| features.1.1.block.0.1.bias | (32,) | (32,) | 32 | Vector |
| features.1.1.block.1.fc1.weight | (8, 32, 1, 1) | (8, 32) | 256 | Matrix |
| features.1.1.block.1.fc1.bias | (8,) | (8,) | 8 | Vector |
| features.1.1.block.1.fc2.weight | (32, 8, 1, 1) | (32, 8) | 256 | Matrix |
| features.1.1.block.1.fc2.bias | (32,) | (32,) | 32 | Vector |
| features.1.1.block.2.0.weight | (32, 32, 1, 1) | (32, 32) | 1024 | Matrix |
| features.1.1.block.2.1.weight | (32,) | (32,) | 32 | Vector |
| features.1.1.block.2.1.bias | (32,) | (32,) | 32 | Vector |
| features.1.2.block.0.0.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| features.1.2.block.0.1.weight | (32,) | (32,) | 32 | Vector |
| features.1.2.block.0.1.bias | (32,) | (32,) | 32 | Vector |
| features.1.2.block.1.fc1.weight | (8, 32, 1, 1) | (8, 32) | 256 | Matrix |
| features.1.2.block.1.fc1.bias | (8,) | (8,) | 8 | Vector |
| features.1.2.block.1.fc2.weight | (32, 8, 1, 1) | (32, 8) | 256 | Matrix |
| features.1.2.block.1.fc2.bias | (32,) | (32,) | 32 | Vector |
| features.1.2.block.2.0.weight | (32, 32, 1, 1) | (32, 32) | 1024 | Matrix |
| features.1.2.block.2.1.weight | (32,) | (32,) | 32 | Vector |
| features.1.2.block.2.1.bias | (32,) | (32,) | 32 | Vector |
| features.2.0.block.0.0.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| features.2.0.block.0.1.weight | (192,) | (192,) | 192 | Vector |
| features.2.0.block.0.1.bias | (192,) | (192,) | 192 | Vector |
| features.2.0.block.1.0.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| features.2.0.block.1.1.weight | (192,) | (192,) | 192 | Vector |
| features.2.0.block.1.1.bias | (192,) | (192,) | 192 | Vector |
| features.2.0.block.2.fc1.weight | (8, 192, 1, 1) | (8, 192) | 1536 | Matrix |
| features.2.0.block.2.fc1.bias | (8,) | (8,) | 8 | Vector |
| features.2.0.block.2.fc2.weight | (192, 8, 1, 1) | (192, 8) | 1536 | Matrix |
| features.2.0.block.2.fc2.bias | (192,) | (192,) | 192 | Vector |
| features.2.0.block.3.0.weight | (40, 192, 1, 1) | (40, 192) | 7680 | Matrix |
| features.2.0.block.3.1.weight | (40,) | (40,) | 40 | Vector |
| features.2.0.block.3.1.bias | (40,) | (40,) | 40 | Vector |
| features.2.1.block.0.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| features.2.1.block.0.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.1.block.0.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.1.block.1.0.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| features.2.1.block.1.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.1.block.1.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.1.block.2.fc1.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| features.2.1.block.2.fc1.bias | (10,) | (10,) | 10 | Vector |
| features.2.1.block.2.fc2.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| features.2.1.block.2.fc2.bias | (240,) | (240,) | 240 | Vector |
| features.2.1.block.3.0.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| features.2.1.block.3.1.weight | (40,) | (40,) | 40 | Vector |
| features.2.1.block.3.1.bias | (40,) | (40,) | 40 | Vector |
| features.2.2.block.0.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| features.2.2.block.0.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.2.block.0.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.2.block.1.0.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| features.2.2.block.1.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.2.block.1.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.2.block.2.fc1.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| features.2.2.block.2.fc1.bias | (10,) | (10,) | 10 | Vector |
| features.2.2.block.2.fc2.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| features.2.2.block.2.fc2.bias | (240,) | (240,) | 240 | Vector |
| features.2.2.block.3.0.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| features.2.2.block.3.1.weight | (40,) | (40,) | 40 | Vector |
| features.2.2.block.3.1.bias | (40,) | (40,) | 40 | Vector |
| features.2.3.block.0.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| features.2.3.block.0.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.3.block.0.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.3.block.1.0.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| features.2.3.block.1.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.3.block.1.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.3.block.2.fc1.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| features.2.3.block.2.fc1.bias | (10,) | (10,) | 10 | Vector |
| features.2.3.block.2.fc2.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| features.2.3.block.2.fc2.bias | (240,) | (240,) | 240 | Vector |
| features.2.3.block.3.0.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| features.2.3.block.3.1.weight | (40,) | (40,) | 40 | Vector |
| features.2.3.block.3.1.bias | (40,) | (40,) | 40 | Vector |
| features.2.4.block.0.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| features.2.4.block.0.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.4.block.0.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.4.block.1.0.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| features.2.4.block.1.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.4.block.1.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.4.block.2.fc1.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| features.2.4.block.2.fc1.bias | (10,) | (10,) | 10 | Vector |
| features.2.4.block.2.fc2.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| features.2.4.block.2.fc2.bias | (240,) | (240,) | 240 | Vector |
| features.2.4.block.3.0.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| features.2.4.block.3.1.weight | (40,) | (40,) | 40 | Vector |
| features.2.4.block.3.1.bias | (40,) | (40,) | 40 | Vector |
| features.2.5.block.0.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| features.2.5.block.0.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.5.block.0.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.5.block.1.0.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| features.2.5.block.1.1.weight | (240,) | (240,) | 240 | Vector |
| features.2.5.block.1.1.bias | (240,) | (240,) | 240 | Vector |
| features.2.5.block.2.fc1.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| features.2.5.block.2.fc1.bias | (10,) | (10,) | 10 | Vector |
| features.2.5.block.2.fc2.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| features.2.5.block.2.fc2.bias | (240,) | (240,) | 240 | Vector |
| features.2.5.block.3.0.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| features.2.5.block.3.1.weight | (40,) | (40,) | 40 | Vector |
| features.2.5.block.3.1.bias | (40,) | (40,) | 40 | Vector |
| features.3.0.block.0.0.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| features.3.0.block.0.1.weight | (240,) | (240,) | 240 | Vector |
| features.3.0.block.0.1.bias | (240,) | (240,) | 240 | Vector |
| features.3.0.block.1.0.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| features.3.0.block.1.1.weight | (240,) | (240,) | 240 | Vector |
| features.3.0.block.1.1.bias | (240,) | (240,) | 240 | Vector |
| features.3.0.block.2.fc1.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| features.3.0.block.2.fc1.bias | (10,) | (10,) | 10 | Vector |
| features.3.0.block.2.fc2.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| features.3.0.block.2.fc2.bias | (240,) | (240,) | 240 | Vector |
| features.3.0.block.3.0.weight | (72, 240, 1, 1) | (72, 240) | 17280 | Matrix |
| features.3.0.block.3.1.weight | (72,) | (72,) | 72 | Vector |
| features.3.0.block.3.1.bias | (72,) | (72,) | 72 | Vector |
| features.3.1.block.0.0.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| features.3.1.block.0.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.1.block.0.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.1.block.1.0.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| features.3.1.block.1.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.1.block.1.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.1.block.2.fc1.weight | (18, 432, 1, 1) | (18, 432) | 7776 | Matrix |
| features.3.1.block.2.fc1.bias | (18,) | (18,) | 18 | Vector |
| features.3.1.block.2.fc2.weight | (432, 18, 1, 1) | (432, 18) | 7776 | Matrix |
| features.3.1.block.2.fc2.bias | (432,) | (432,) | 432 | Vector |
| features.3.1.block.3.0.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| features.3.1.block.3.1.weight | (72,) | (72,) | 72 | Vector |
| features.3.1.block.3.1.bias | (72,) | (72,) | 72 | Vector |
| features.3.2.block.0.0.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| features.3.2.block.0.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.2.block.0.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.2.block.1.0.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| features.3.2.block.1.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.2.block.1.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.2.block.2.fc1.weight | (18, 432, 1, 1) | (18, 432) | 7776 | Matrix |
| features.3.2.block.2.fc1.bias | (18,) | (18,) | 18 | Vector |
| features.3.2.block.2.fc2.weight | (432, 18, 1, 1) | (432, 18) | 7776 | Matrix |
| features.3.2.block.2.fc2.bias | (432,) | (432,) | 432 | Vector |
| features.3.2.block.3.0.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| features.3.2.block.3.1.weight | (72,) | (72,) | 72 | Vector |
| features.3.2.block.3.1.bias | (72,) | (72,) | 72 | Vector |
| features.3.3.block.0.0.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| features.3.3.block.0.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.3.block.0.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.3.block.1.0.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| features.3.3.block.1.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.3.block.1.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.3.block.2.fc1.weight | (18, 432, 1, 1) | (18, 432) | 7776 | Matrix |
| features.3.3.block.2.fc1.bias | (18,) | (18,) | 18 | Vector |
| features.3.3.block.2.fc2.weight | (432, 18, 1, 1) | (432, 18) | 7776 | Matrix |
| features.3.3.block.2.fc2.bias | (432,) | (432,) | 432 | Vector |
| features.3.3.block.3.0.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| features.3.3.block.3.1.weight | (72,) | (72,) | 72 | Vector |
| features.3.3.block.3.1.bias | (72,) | (72,) | 72 | Vector |
| features.3.4.block.0.0.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| features.3.4.block.0.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.4.block.0.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.4.block.1.0.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| features.3.4.block.1.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.4.block.1.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.4.block.2.fc1.weight | (18, 432, 1, 1) | (18, 432) | 7776 | Matrix |
| features.3.4.block.2.fc1.bias | (18,) | (18,) | 18 | Vector |
| features.3.4.block.2.fc2.weight | (432, 18, 1, 1) | (432, 18) | 7776 | Matrix |
| features.3.4.block.2.fc2.bias | (432,) | (432,) | 432 | Vector |
| features.3.4.block.3.0.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| features.3.4.block.3.1.weight | (72,) | (72,) | 72 | Vector |
| features.3.4.block.3.1.bias | (72,) | (72,) | 72 | Vector |
| features.3.5.block.0.0.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| features.3.5.block.0.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.5.block.0.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.5.block.1.0.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| features.3.5.block.1.1.weight | (432,) | (432,) | 432 | Vector |
| features.3.5.block.1.1.bias | (432,) | (432,) | 432 | Vector |
| features.3.5.block.2.fc1.weight | (18, 432, 1, 1) | (18, 432) | 7776 | Matrix |
| features.3.5.block.2.fc1.bias | (18,) | (18,) | 18 | Vector |
| features.3.5.block.2.fc2.weight | (432, 18, 1, 1) | (432, 18) | 7776 | Matrix |
| features.3.5.block.2.fc2.bias | (432,) | (432,) | 432 | Vector |
| features.3.5.block.3.0.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| features.3.5.block.3.1.weight | (72,) | (72,) | 72 | Vector |
| features.3.5.block.3.1.bias | (72,) | (72,) | 72 | Vector |
| features.4.0.block.0.0.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| features.4.0.block.0.1.weight | (432,) | (432,) | 432 | Vector |
| features.4.0.block.0.1.bias | (432,) | (432,) | 432 | Vector |
| features.4.0.block.1.0.weight | (432, 1, 3, 3) | (432, 3, 3) | 3888 | Tensor rank 3 |
| features.4.0.block.1.1.weight | (432,) | (432,) | 432 | Vector |
| features.4.0.block.1.1.bias | (432,) | (432,) | 432 | Vector |
| features.4.0.block.2.fc1.weight | (18, 432, 1, 1) | (18, 432) | 7776 | Matrix |
| features.4.0.block.2.fc1.bias | (18,) | (18,) | 18 | Vector |
| features.4.0.block.2.fc2.weight | (432, 18, 1, 1) | (432, 18) | 7776 | Matrix |
| features.4.0.block.2.fc2.bias | (432,) | (432,) | 432 | Vector |
| features.4.0.block.3.0.weight | (144, 432, 1, 1) | (144, 432) | 62208 | Matrix |
| features.4.0.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.0.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.1.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.1.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.1.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.1.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.1.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.1.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.1.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.1.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.1.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.1.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.1.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.1.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.1.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.2.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.2.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.2.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.2.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.2.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.2.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.2.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.2.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.2.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.2.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.2.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.2.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.2.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.3.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.3.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.3.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.3.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.3.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.3.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.3.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.3.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.3.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.3.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.3.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.3.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.3.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.4.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.4.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.4.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.4.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.4.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.4.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.4.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.4.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.4.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.4.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.4.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.4.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.4.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.5.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.5.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.5.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.5.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.5.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.5.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.5.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.5.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.5.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.5.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.5.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.5.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.5.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.6.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.6.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.6.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.6.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.6.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.6.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.6.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.6.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.6.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.6.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.6.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.6.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.6.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.4.7.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.4.7.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.7.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.7.block.1.0.weight | (864, 1, 3, 3) | (864, 3, 3) | 7776 | Tensor rank 3 |
| features.4.7.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.4.7.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.4.7.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.4.7.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.4.7.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.4.7.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.4.7.block.3.0.weight | (144, 864, 1, 1) | (144, 864) | 124416 | Matrix |
| features.4.7.block.3.1.weight | (144,) | (144,) | 144 | Vector |
| features.4.7.block.3.1.bias | (144,) | (144,) | 144 | Vector |
| features.5.0.block.0.0.weight | (864, 144, 1, 1) | (864, 144) | 124416 | Matrix |
| features.5.0.block.0.1.weight | (864,) | (864,) | 864 | Vector |
| features.5.0.block.0.1.bias | (864,) | (864,) | 864 | Vector |
| features.5.0.block.1.0.weight | (864, 1, 5, 5) | (864, 5, 5) | 21600 | Tensor rank 3 |
| features.5.0.block.1.1.weight | (864,) | (864,) | 864 | Vector |
| features.5.0.block.1.1.bias | (864,) | (864,) | 864 | Vector |
| features.5.0.block.2.fc1.weight | (36, 864, 1, 1) | (36, 864) | 31104 | Matrix |
| features.5.0.block.2.fc1.bias | (36,) | (36,) | 36 | Vector |
| features.5.0.block.2.fc2.weight | (864, 36, 1, 1) | (864, 36) | 31104 | Matrix |
| features.5.0.block.2.fc2.bias | (864,) | (864,) | 864 | Vector |
| features.5.0.block.3.0.weight | (200, 864, 1, 1) | (200, 864) | 172800 | Matrix |
| features.5.0.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.0.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.1.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.1.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.1.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.1.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.1.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.1.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.1.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.1.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.1.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.1.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.1.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.1.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.1.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.2.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.2.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.2.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.2.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.2.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.2.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.2.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.2.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.2.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.2.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.2.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.2.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.2.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.3.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.3.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.3.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.3.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.3.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.3.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.3.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.3.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.3.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.3.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.3.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.3.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.3.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.4.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.4.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.4.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.4.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.4.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.4.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.4.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.4.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.4.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.4.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.4.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.4.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.4.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.5.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.5.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.5.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.5.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.5.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.5.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.5.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.5.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.5.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.5.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.5.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.5.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.5.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.6.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.6.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.6.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.6.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.6.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.6.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.6.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.6.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.6.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.6.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.6.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.6.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.6.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.5.7.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.5.7.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.7.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.7.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.5.7.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.5.7.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.7.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.5.7.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.5.7.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.5.7.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.5.7.block.3.0.weight | (200, 1200, 1, 1) | (200, 1200) | 240000 | Matrix |
| features.5.7.block.3.1.weight | (200,) | (200,) | 200 | Vector |
| features.5.7.block.3.1.bias | (200,) | (200,) | 200 | Vector |
| features.6.0.block.0.0.weight | (1200, 200, 1, 1) | (1200, 200) | 240000 | Matrix |
| features.6.0.block.0.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.6.0.block.0.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.6.0.block.1.0.weight | (1200, 1, 5, 5) | (1200, 5, 5) | 30000 | Tensor rank 3 |
| features.6.0.block.1.1.weight | (1200,) | (1200,) | 1200 | Vector |
| features.6.0.block.1.1.bias | (1200,) | (1200,) | 1200 | Vector |
| features.6.0.block.2.fc1.weight | (50, 1200, 1, 1) | (50, 1200) | 60000 | Matrix |
| features.6.0.block.2.fc1.bias | (50,) | (50,) | 50 | Vector |
| features.6.0.block.2.fc2.weight | (1200, 50, 1, 1) | (1200, 50) | 60000 | Matrix |
| features.6.0.block.2.fc2.bias | (1200,) | (1200,) | 1200 | Vector |
| features.6.0.block.3.0.weight | (344, 1200, 1, 1) | (344, 1200) | 412800 | Matrix |
| features.6.0.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.0.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.1.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.1.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.1.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.1.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.1.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.1.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.1.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.1.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.1.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.1.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.1.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.1.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.1.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.2.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.2.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.2.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.2.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.2.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.2.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.2.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.2.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.2.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.2.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.2.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.2.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.2.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.3.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.3.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.3.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.3.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.3.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.3.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.3.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.3.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.3.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.3.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.3.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.3.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.3.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.4.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.4.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.4.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.4.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.4.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.4.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.4.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.4.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.4.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.4.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.4.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.4.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.4.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.5.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.5.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.5.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.5.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.5.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.5.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.5.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.5.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.5.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.5.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.5.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.5.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.5.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.6.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.6.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.6.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.6.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.6.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.6.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.6.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.6.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.6.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.6.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.6.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.6.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.6.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.7.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.7.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.7.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.7.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.7.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.7.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.7.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.7.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.7.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.7.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.7.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.7.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.7.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.8.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.8.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.8.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.8.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.8.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.8.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.8.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.8.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.8.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.8.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.8.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.8.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.8.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.9.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.9.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.9.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.9.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.9.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.9.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.9.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.9.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.9.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.9.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.9.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.9.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.9.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.6.10.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.6.10.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.10.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.10.block.1.0.weight | (2064, 1, 5, 5) | (2064, 5, 5) | 51600 | Tensor rank 3 |
| features.6.10.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.6.10.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.10.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.6.10.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.6.10.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.6.10.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.6.10.block.3.0.weight | (344, 2064, 1, 1) | (344, 2064) | 710016 | Matrix |
| features.6.10.block.3.1.weight | (344,) | (344,) | 344 | Vector |
| features.6.10.block.3.1.bias | (344,) | (344,) | 344 | Vector |
| features.7.0.block.0.0.weight | (2064, 344, 1, 1) | (2064, 344) | 710016 | Matrix |
| features.7.0.block.0.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.7.0.block.0.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.7.0.block.1.0.weight | (2064, 1, 3, 3) | (2064, 3, 3) | 18576 | Tensor rank 3 |
| features.7.0.block.1.1.weight | (2064,) | (2064,) | 2064 | Vector |
| features.7.0.block.1.1.bias | (2064,) | (2064,) | 2064 | Vector |
| features.7.0.block.2.fc1.weight | (86, 2064, 1, 1) | (86, 2064) | 177504 | Matrix |
| features.7.0.block.2.fc1.bias | (86,) | (86,) | 86 | Vector |
| features.7.0.block.2.fc2.weight | (2064, 86, 1, 1) | (2064, 86) | 177504 | Matrix |
| features.7.0.block.2.fc2.bias | (2064,) | (2064,) | 2064 | Vector |
| features.7.0.block.3.0.weight | (576, 2064, 1, 1) | (576, 2064) | 1188864 | Matrix |
| features.7.0.block.3.1.weight | (576,) | (576,) | 576 | Vector |
| features.7.0.block.3.1.bias | (576,) | (576,) | 576 | Vector |
| features.7.1.block.0.0.weight | (3456, 576, 1, 1) | (3456, 576) | 1990656 | Matrix |
| features.7.1.block.0.1.weight | (3456,) | (3456,) | 3456 | Vector |
| features.7.1.block.0.1.bias | (3456,) | (3456,) | 3456 | Vector |
| features.7.1.block.1.0.weight | (3456, 1, 3, 3) | (3456, 3, 3) | 31104 | Tensor rank 3 |
| features.7.1.block.1.1.weight | (3456,) | (3456,) | 3456 | Vector |
| features.7.1.block.1.1.bias | (3456,) | (3456,) | 3456 | Vector |
| features.7.1.block.2.fc1.weight | (144, 3456, 1, 1) | (144, 3456) | 497664 | Matrix |
| features.7.1.block.2.fc1.bias | (144,) | (144,) | 144 | Vector |
| features.7.1.block.2.fc2.weight | (3456, 144, 1, 1) | (3456, 144) | 497664 | Matrix |
| features.7.1.block.2.fc2.bias | (3456,) | (3456,) | 3456 | Vector |
| features.7.1.block.3.0.weight | (576, 3456, 1, 1) | (576, 3456) | 1990656 | Matrix |
| features.7.1.block.3.1.weight | (576,) | (576,) | 576 | Vector |
| features.7.1.block.3.1.bias | (576,) | (576,) | 576 | Vector |
| features.7.2.block.0.0.weight | (3456, 576, 1, 1) | (3456, 576) | 1990656 | Matrix |
| features.7.2.block.0.1.weight | (3456,) | (3456,) | 3456 | Vector |
| features.7.2.block.0.1.bias | (3456,) | (3456,) | 3456 | Vector |
| features.7.2.block.1.0.weight | (3456, 1, 3, 3) | (3456, 3, 3) | 31104 | Tensor rank 3 |
| features.7.2.block.1.1.weight | (3456,) | (3456,) | 3456 | Vector |
| features.7.2.block.1.1.bias | (3456,) | (3456,) | 3456 | Vector |
| features.7.2.block.2.fc1.weight | (144, 3456, 1, 1) | (144, 3456) | 497664 | Matrix |
| features.7.2.block.2.fc1.bias | (144,) | (144,) | 144 | Vector |
| features.7.2.block.2.fc2.weight | (3456, 144, 1, 1) | (3456, 144) | 497664 | Matrix |
| features.7.2.block.2.fc2.bias | (3456,) | (3456,) | 3456 | Vector |
| features.7.2.block.3.0.weight | (576, 3456, 1, 1) | (576, 3456) | 1990656 | Matrix |
| features.7.2.block.3.1.weight | (576,) | (576,) | 576 | Vector |
| features.7.2.block.3.1.bias | (576,) | (576,) | 576 | Vector |
| features.8.0.weight | (2304, 576, 1, 1) | (2304, 576) | 1327104 | Matrix |
| features.8.1.weight | (2304,) | (2304,) | 2304 | Vector |
| features.8.1.bias | (2304,) | (2304,) | 2304 | Vector |
| classifier.1.weight | (1000, 2304) | (1000, 2304) | 2304000 | Matrix |
| classifier.1.bias | (1000,) | (1000,) | 1000 | Vector |

