# shufflenet_v2_x0_5 parameter information

**Number of layers: [ 170 ]**

**Number of parameters: [ 1.37M ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.47 | 21.76 | 11.18 | 0.59 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.65 | 98.62 | 0.68 | 0.05 | 

<img src="../figs/shufflenet_v2_x0_5_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv1.0.weight | (24, 3, 3, 3) | (24, 3, 3, 3) | 648 | Tensor rank 4 |
| conv1.1.weight | (24,) | (24,) | 24 | Vector |
| conv1.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.0.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| stage2.0.branch1.1.weight | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.2.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.0.branch1.3.weight | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.3.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch2.0.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.0.branch2.1.weight | (24,) | (24,) | 24 | Vector |
| stage2.0.branch2.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch2.3.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| stage2.0.branch2.4.weight | (24,) | (24,) | 24 | Vector |
| stage2.0.branch2.4.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch2.5.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.0.branch2.6.weight | (24,) | (24,) | 24 | Vector |
| stage2.0.branch2.6.bias | (24,) | (24,) | 24 | Vector |
| stage2.1.branch2.0.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.1.branch2.1.weight | (24,) | (24,) | 24 | Vector |
| stage2.1.branch2.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.1.branch2.3.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| stage2.1.branch2.4.weight | (24,) | (24,) | 24 | Vector |
| stage2.1.branch2.4.bias | (24,) | (24,) | 24 | Vector |
| stage2.1.branch2.5.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.1.branch2.6.weight | (24,) | (24,) | 24 | Vector |
| stage2.1.branch2.6.bias | (24,) | (24,) | 24 | Vector |
| stage2.2.branch2.0.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.2.branch2.1.weight | (24,) | (24,) | 24 | Vector |
| stage2.2.branch2.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.2.branch2.3.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| stage2.2.branch2.4.weight | (24,) | (24,) | 24 | Vector |
| stage2.2.branch2.4.bias | (24,) | (24,) | 24 | Vector |
| stage2.2.branch2.5.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.2.branch2.6.weight | (24,) | (24,) | 24 | Vector |
| stage2.2.branch2.6.bias | (24,) | (24,) | 24 | Vector |
| stage2.3.branch2.0.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.3.branch2.1.weight | (24,) | (24,) | 24 | Vector |
| stage2.3.branch2.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.3.branch2.3.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| stage2.3.branch2.4.weight | (24,) | (24,) | 24 | Vector |
| stage2.3.branch2.4.bias | (24,) | (24,) | 24 | Vector |
| stage2.3.branch2.5.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| stage2.3.branch2.6.weight | (24,) | (24,) | 24 | Vector |
| stage2.3.branch2.6.bias | (24,) | (24,) | 24 | Vector |
| stage3.0.branch1.0.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.0.branch1.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.0.branch1.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.0.branch1.2.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.0.branch1.3.weight | (48,) | (48,) | 48 | Vector |
| stage3.0.branch1.3.bias | (48,) | (48,) | 48 | Vector |
| stage3.0.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.0.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.0.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.0.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.0.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.0.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.0.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.0.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.0.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.1.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.1.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.1.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.1.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.1.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.1.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.1.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.1.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.1.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.2.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.2.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.2.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.2.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.2.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.2.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.2.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.2.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.2.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.3.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.3.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.3.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.3.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.3.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.3.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.3.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.3.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.3.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.4.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.4.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.4.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.4.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.4.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.4.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.4.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.4.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.4.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.5.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.5.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.5.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.5.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.5.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.5.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.5.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.5.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.5.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.6.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.6.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.6.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.6.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.6.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.6.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.6.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.6.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.6.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage3.7.branch2.0.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.7.branch2.1.weight | (48,) | (48,) | 48 | Vector |
| stage3.7.branch2.1.bias | (48,) | (48,) | 48 | Vector |
| stage3.7.branch2.3.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| stage3.7.branch2.4.weight | (48,) | (48,) | 48 | Vector |
| stage3.7.branch2.4.bias | (48,) | (48,) | 48 | Vector |
| stage3.7.branch2.5.weight | (48, 48, 1, 1) | (48, 48) | 2304 | Matrix |
| stage3.7.branch2.6.weight | (48,) | (48,) | 48 | Vector |
| stage3.7.branch2.6.bias | (48,) | (48,) | 48 | Vector |
| stage4.0.branch1.0.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| stage4.0.branch1.1.weight | (96,) | (96,) | 96 | Vector |
| stage4.0.branch1.1.bias | (96,) | (96,) | 96 | Vector |
| stage4.0.branch1.2.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.0.branch1.3.weight | (96,) | (96,) | 96 | Vector |
| stage4.0.branch1.3.bias | (96,) | (96,) | 96 | Vector |
| stage4.0.branch2.0.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.0.branch2.1.weight | (96,) | (96,) | 96 | Vector |
| stage4.0.branch2.1.bias | (96,) | (96,) | 96 | Vector |
| stage4.0.branch2.3.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| stage4.0.branch2.4.weight | (96,) | (96,) | 96 | Vector |
| stage4.0.branch2.4.bias | (96,) | (96,) | 96 | Vector |
| stage4.0.branch2.5.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.0.branch2.6.weight | (96,) | (96,) | 96 | Vector |
| stage4.0.branch2.6.bias | (96,) | (96,) | 96 | Vector |
| stage4.1.branch2.0.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.1.branch2.1.weight | (96,) | (96,) | 96 | Vector |
| stage4.1.branch2.1.bias | (96,) | (96,) | 96 | Vector |
| stage4.1.branch2.3.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| stage4.1.branch2.4.weight | (96,) | (96,) | 96 | Vector |
| stage4.1.branch2.4.bias | (96,) | (96,) | 96 | Vector |
| stage4.1.branch2.5.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.1.branch2.6.weight | (96,) | (96,) | 96 | Vector |
| stage4.1.branch2.6.bias | (96,) | (96,) | 96 | Vector |
| stage4.2.branch2.0.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.2.branch2.1.weight | (96,) | (96,) | 96 | Vector |
| stage4.2.branch2.1.bias | (96,) | (96,) | 96 | Vector |
| stage4.2.branch2.3.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| stage4.2.branch2.4.weight | (96,) | (96,) | 96 | Vector |
| stage4.2.branch2.4.bias | (96,) | (96,) | 96 | Vector |
| stage4.2.branch2.5.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.2.branch2.6.weight | (96,) | (96,) | 96 | Vector |
| stage4.2.branch2.6.bias | (96,) | (96,) | 96 | Vector |
| stage4.3.branch2.0.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.3.branch2.1.weight | (96,) | (96,) | 96 | Vector |
| stage4.3.branch2.1.bias | (96,) | (96,) | 96 | Vector |
| stage4.3.branch2.3.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| stage4.3.branch2.4.weight | (96,) | (96,) | 96 | Vector |
| stage4.3.branch2.4.bias | (96,) | (96,) | 96 | Vector |
| stage4.3.branch2.5.weight | (96, 96, 1, 1) | (96, 96) | 9216 | Matrix |
| stage4.3.branch2.6.weight | (96,) | (96,) | 96 | Vector |
| stage4.3.branch2.6.bias | (96,) | (96,) | 96 | Vector |
| conv5.0.weight | (1024, 192, 1, 1) | (1024, 192) | 196608 | Matrix |
| conv5.1.weight | (1024,) | (1024,) | 1024 | Vector |
| conv5.1.bias | (1024,) | (1024,) | 1024 | Vector |
| fc.weight | (1000, 1024) | (1000, 1024) | 1024000 | Matrix |
| fc.bias | (1000,) | (1000,) | 1000 | Vector |

