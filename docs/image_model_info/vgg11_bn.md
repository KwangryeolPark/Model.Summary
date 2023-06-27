# vgg11_bn parameter information

**Number of layers: [ 38 ]**

**Number of parameters: [ 132.87M ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 71.05 | 7.89 | 21.05 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 0.01 | 93.05 | 6.94 | 

<img src="../figs/vgg11_bn_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| features.0.weight | (64, 3, 3, 3) | (64, 3, 3, 3) | 1728 | Tensor rank 4 |
| features.0.bias | (64,) | (64,) | 64 | Vector |
| features.1.weight | (64,) | (64,) | 64 | Vector |
| features.1.bias | (64,) | (64,) | 64 | Vector |
| features.4.weight | (128, 64, 3, 3) | (128, 64, 3, 3) | 73728 | Tensor rank 4 |
| features.4.bias | (128,) | (128,) | 128 | Vector |
| features.5.weight | (128,) | (128,) | 128 | Vector |
| features.5.bias | (128,) | (128,) | 128 | Vector |
| features.8.weight | (256, 128, 3, 3) | (256, 128, 3, 3) | 294912 | Tensor rank 4 |
| features.8.bias | (256,) | (256,) | 256 | Vector |
| features.9.weight | (256,) | (256,) | 256 | Vector |
| features.9.bias | (256,) | (256,) | 256 | Vector |
| features.11.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| features.11.bias | (256,) | (256,) | 256 | Vector |
| features.12.weight | (256,) | (256,) | 256 | Vector |
| features.12.bias | (256,) | (256,) | 256 | Vector |
| features.15.weight | (512, 256, 3, 3) | (512, 256, 3, 3) | 1179648 | Tensor rank 4 |
| features.15.bias | (512,) | (512,) | 512 | Vector |
| features.16.weight | (512,) | (512,) | 512 | Vector |
| features.16.bias | (512,) | (512,) | 512 | Vector |
| features.18.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| features.18.bias | (512,) | (512,) | 512 | Vector |
| features.19.weight | (512,) | (512,) | 512 | Vector |
| features.19.bias | (512,) | (512,) | 512 | Vector |
| features.22.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| features.22.bias | (512,) | (512,) | 512 | Vector |
| features.23.weight | (512,) | (512,) | 512 | Vector |
| features.23.bias | (512,) | (512,) | 512 | Vector |
| features.25.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| features.25.bias | (512,) | (512,) | 512 | Vector |
| features.26.weight | (512,) | (512,) | 512 | Vector |
| features.26.bias | (512,) | (512,) | 512 | Vector |
| classifier.0.weight | (4096, 25088) | (4096, 25088) | 102760448 | Matrix |
| classifier.0.bias | (4096,) | (4096,) | 4096 | Vector |
| classifier.3.weight | (4096, 4096) | (4096, 4096) | 16777216 | Matrix |
| classifier.3.bias | (4096,) | (4096,) | 4096 | Vector |
| classifier.6.weight | (1000, 4096) | (1000, 4096) | 4096000 | Matrix |
| classifier.6.bias | (1000,) | (1000,) | 1000 | Vector |

