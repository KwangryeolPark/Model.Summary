# shufflenet_v2_x1_0 parameter information

**Number of layers: [ 170 ]**

**Number of parameters: [ 2.28M ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.47 | 21.76 | 11.18 | 0.59 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.75 | 98.25 | 0.97 | 0.03 | 

<img src="../figs/shufflenet_v2_x1_0_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv1.0.weight | (24, 3, 3, 3) | (24, 3, 3, 3) | 648 | Tensor rank 4 |
| conv1.1.weight | (24,) | (24,) | 24 | Vector |
| conv1.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.0.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| stage2.0.branch1.1.weight | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.1.bias | (24,) | (24,) | 24 | Vector |
| stage2.0.branch1.2.weight | (58, 24, 1, 1) | (58, 24) | 1392 | Matrix |
| stage2.0.branch1.3.weight | (58,) | (58,) | 58 | Vector |
| stage2.0.branch1.3.bias | (58,) | (58,) | 58 | Vector |
| stage2.0.branch2.0.weight | (58, 24, 1, 1) | (58, 24) | 1392 | Matrix |
| stage2.0.branch2.1.weight | (58,) | (58,) | 58 | Vector |
| stage2.0.branch2.1.bias | (58,) | (58,) | 58 | Vector |
| stage2.0.branch2.3.weight | (58, 1, 3, 3) | (58, 3, 3) | 522 | Tensor rank 3 |
| stage2.0.branch2.4.weight | (58,) | (58,) | 58 | Vector |
| stage2.0.branch2.4.bias | (58,) | (58,) | 58 | Vector |
| stage2.0.branch2.5.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.0.branch2.6.weight | (58,) | (58,) | 58 | Vector |
| stage2.0.branch2.6.bias | (58,) | (58,) | 58 | Vector |
| stage2.1.branch2.0.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.1.branch2.1.weight | (58,) | (58,) | 58 | Vector |
| stage2.1.branch2.1.bias | (58,) | (58,) | 58 | Vector |
| stage2.1.branch2.3.weight | (58, 1, 3, 3) | (58, 3, 3) | 522 | Tensor rank 3 |
| stage2.1.branch2.4.weight | (58,) | (58,) | 58 | Vector |
| stage2.1.branch2.4.bias | (58,) | (58,) | 58 | Vector |
| stage2.1.branch2.5.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.1.branch2.6.weight | (58,) | (58,) | 58 | Vector |
| stage2.1.branch2.6.bias | (58,) | (58,) | 58 | Vector |
| stage2.2.branch2.0.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.2.branch2.1.weight | (58,) | (58,) | 58 | Vector |
| stage2.2.branch2.1.bias | (58,) | (58,) | 58 | Vector |
| stage2.2.branch2.3.weight | (58, 1, 3, 3) | (58, 3, 3) | 522 | Tensor rank 3 |
| stage2.2.branch2.4.weight | (58,) | (58,) | 58 | Vector |
| stage2.2.branch2.4.bias | (58,) | (58,) | 58 | Vector |
| stage2.2.branch2.5.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.2.branch2.6.weight | (58,) | (58,) | 58 | Vector |
| stage2.2.branch2.6.bias | (58,) | (58,) | 58 | Vector |
| stage2.3.branch2.0.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.3.branch2.1.weight | (58,) | (58,) | 58 | Vector |
| stage2.3.branch2.1.bias | (58,) | (58,) | 58 | Vector |
| stage2.3.branch2.3.weight | (58, 1, 3, 3) | (58, 3, 3) | 522 | Tensor rank 3 |
| stage2.3.branch2.4.weight | (58,) | (58,) | 58 | Vector |
| stage2.3.branch2.4.bias | (58,) | (58,) | 58 | Vector |
| stage2.3.branch2.5.weight | (58, 58, 1, 1) | (58, 58) | 3364 | Matrix |
| stage2.3.branch2.6.weight | (58,) | (58,) | 58 | Vector |
| stage2.3.branch2.6.bias | (58,) | (58,) | 58 | Vector |
| stage3.0.branch1.0.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.0.branch1.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.0.branch1.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.0.branch1.2.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.0.branch1.3.weight | (116,) | (116,) | 116 | Vector |
| stage3.0.branch1.3.bias | (116,) | (116,) | 116 | Vector |
| stage3.0.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.0.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.0.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.0.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.0.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.0.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.0.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.0.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.0.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.1.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.1.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.1.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.1.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.1.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.1.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.1.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.1.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.1.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.2.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.2.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.2.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.2.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.2.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.2.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.2.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.2.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.2.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.3.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.3.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.3.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.3.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.3.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.3.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.3.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.3.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.3.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.4.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.4.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.4.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.4.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.4.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.4.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.4.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.4.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.4.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.5.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.5.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.5.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.5.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.5.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.5.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.5.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.5.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.5.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.6.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.6.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.6.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.6.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.6.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.6.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.6.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.6.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.6.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage3.7.branch2.0.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.7.branch2.1.weight | (116,) | (116,) | 116 | Vector |
| stage3.7.branch2.1.bias | (116,) | (116,) | 116 | Vector |
| stage3.7.branch2.3.weight | (116, 1, 3, 3) | (116, 3, 3) | 1044 | Tensor rank 3 |
| stage3.7.branch2.4.weight | (116,) | (116,) | 116 | Vector |
| stage3.7.branch2.4.bias | (116,) | (116,) | 116 | Vector |
| stage3.7.branch2.5.weight | (116, 116, 1, 1) | (116, 116) | 13456 | Matrix |
| stage3.7.branch2.6.weight | (116,) | (116,) | 116 | Vector |
| stage3.7.branch2.6.bias | (116,) | (116,) | 116 | Vector |
| stage4.0.branch1.0.weight | (232, 1, 3, 3) | (232, 3, 3) | 2088 | Tensor rank 3 |
| stage4.0.branch1.1.weight | (232,) | (232,) | 232 | Vector |
| stage4.0.branch1.1.bias | (232,) | (232,) | 232 | Vector |
| stage4.0.branch1.2.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.0.branch1.3.weight | (232,) | (232,) | 232 | Vector |
| stage4.0.branch1.3.bias | (232,) | (232,) | 232 | Vector |
| stage4.0.branch2.0.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.0.branch2.1.weight | (232,) | (232,) | 232 | Vector |
| stage4.0.branch2.1.bias | (232,) | (232,) | 232 | Vector |
| stage4.0.branch2.3.weight | (232, 1, 3, 3) | (232, 3, 3) | 2088 | Tensor rank 3 |
| stage4.0.branch2.4.weight | (232,) | (232,) | 232 | Vector |
| stage4.0.branch2.4.bias | (232,) | (232,) | 232 | Vector |
| stage4.0.branch2.5.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.0.branch2.6.weight | (232,) | (232,) | 232 | Vector |
| stage4.0.branch2.6.bias | (232,) | (232,) | 232 | Vector |
| stage4.1.branch2.0.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.1.branch2.1.weight | (232,) | (232,) | 232 | Vector |
| stage4.1.branch2.1.bias | (232,) | (232,) | 232 | Vector |
| stage4.1.branch2.3.weight | (232, 1, 3, 3) | (232, 3, 3) | 2088 | Tensor rank 3 |
| stage4.1.branch2.4.weight | (232,) | (232,) | 232 | Vector |
| stage4.1.branch2.4.bias | (232,) | (232,) | 232 | Vector |
| stage4.1.branch2.5.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.1.branch2.6.weight | (232,) | (232,) | 232 | Vector |
| stage4.1.branch2.6.bias | (232,) | (232,) | 232 | Vector |
| stage4.2.branch2.0.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.2.branch2.1.weight | (232,) | (232,) | 232 | Vector |
| stage4.2.branch2.1.bias | (232,) | (232,) | 232 | Vector |
| stage4.2.branch2.3.weight | (232, 1, 3, 3) | (232, 3, 3) | 2088 | Tensor rank 3 |
| stage4.2.branch2.4.weight | (232,) | (232,) | 232 | Vector |
| stage4.2.branch2.4.bias | (232,) | (232,) | 232 | Vector |
| stage4.2.branch2.5.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.2.branch2.6.weight | (232,) | (232,) | 232 | Vector |
| stage4.2.branch2.6.bias | (232,) | (232,) | 232 | Vector |
| stage4.3.branch2.0.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.3.branch2.1.weight | (232,) | (232,) | 232 | Vector |
| stage4.3.branch2.1.bias | (232,) | (232,) | 232 | Vector |
| stage4.3.branch2.3.weight | (232, 1, 3, 3) | (232, 3, 3) | 2088 | Tensor rank 3 |
| stage4.3.branch2.4.weight | (232,) | (232,) | 232 | Vector |
| stage4.3.branch2.4.bias | (232,) | (232,) | 232 | Vector |
| stage4.3.branch2.5.weight | (232, 232, 1, 1) | (232, 232) | 53824 | Matrix |
| stage4.3.branch2.6.weight | (232,) | (232,) | 232 | Vector |
| stage4.3.branch2.6.bias | (232,) | (232,) | 232 | Vector |
| conv5.0.weight | (1024, 464, 1, 1) | (1024, 464) | 475136 | Matrix |
| conv5.1.weight | (1024,) | (1024,) | 1024 | Vector |
| conv5.1.bias | (1024,) | (1024,) | 1024 | Vector |
| fc.weight | (1000, 1024) | (1000, 1024) | 1024000 | Matrix |
| fc.bias | (1000,) | (1000,) | 1000 | Vector |

