# mobilenet_v1 parameter information

**Number of layers: [ 83 ]**

**Number of parameters: [ 12.241 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 12.241 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.27 | 16.87 | 15.66 | 1.20 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.68 | 97.90 | 1.39 | 0.03 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| mobilenet_v1.conv_stem.convolution.weight | (32, 3, 3, 3) | (32, 3, 3, 3) | 864 | Tensor rank 4 |
| mobilenet_v1.conv_stem.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v1.conv_stem.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v1.layer.0.convolution.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| mobilenet_v1.layer.0.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v1.layer.0.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v1.layer.1.convolution.weight | (64, 32, 1, 1) | (64, 32) | 2048 | Matrix |
| mobilenet_v1.layer.1.normalization.weight | (64,) | (64,) | 64 | Vector |
| mobilenet_v1.layer.1.normalization.bias | (64,) | (64,) | 64 | Vector |
| mobilenet_v1.layer.2.convolution.weight | (64, 1, 3, 3) | (64, 3, 3) | 576 | Tensor rank 3 |
| mobilenet_v1.layer.2.normalization.weight | (64,) | (64,) | 64 | Vector |
| mobilenet_v1.layer.2.normalization.bias | (64,) | (64,) | 64 | Vector |
| mobilenet_v1.layer.3.convolution.weight | (128, 64, 1, 1) | (128, 64) | 8192 | Matrix |
| mobilenet_v1.layer.3.normalization.weight | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.3.normalization.bias | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.4.convolution.weight | (128, 1, 3, 3) | (128, 3, 3) | 1152 | Tensor rank 3 |
| mobilenet_v1.layer.4.normalization.weight | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.4.normalization.bias | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.5.convolution.weight | (128, 128, 1, 1) | (128, 128) | 16384 | Matrix |
| mobilenet_v1.layer.5.normalization.weight | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.5.normalization.bias | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.6.convolution.weight | (128, 1, 3, 3) | (128, 3, 3) | 1152 | Tensor rank 3 |
| mobilenet_v1.layer.6.normalization.weight | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.6.normalization.bias | (128,) | (128,) | 128 | Vector |
| mobilenet_v1.layer.7.convolution.weight | (256, 128, 1, 1) | (256, 128) | 32768 | Matrix |
| mobilenet_v1.layer.7.normalization.weight | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.7.normalization.bias | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.8.convolution.weight | (256, 1, 3, 3) | (256, 3, 3) | 2304 | Tensor rank 3 |
| mobilenet_v1.layer.8.normalization.weight | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.8.normalization.bias | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.9.convolution.weight | (256, 256, 1, 1) | (256, 256) | 65536 | Matrix |
| mobilenet_v1.layer.9.normalization.weight | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.9.normalization.bias | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.10.convolution.weight | (256, 1, 3, 3) | (256, 3, 3) | 2304 | Tensor rank 3 |
| mobilenet_v1.layer.10.normalization.weight | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.10.normalization.bias | (256,) | (256,) | 256 | Vector |
| mobilenet_v1.layer.11.convolution.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| mobilenet_v1.layer.11.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.11.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.12.convolution.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| mobilenet_v1.layer.12.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.12.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.13.convolution.weight | (512, 512, 1, 1) | (512, 512) | 262144 | Matrix |
| mobilenet_v1.layer.13.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.13.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.14.convolution.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| mobilenet_v1.layer.14.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.14.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.15.convolution.weight | (512, 512, 1, 1) | (512, 512) | 262144 | Matrix |
| mobilenet_v1.layer.15.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.15.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.16.convolution.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| mobilenet_v1.layer.16.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.16.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.17.convolution.weight | (512, 512, 1, 1) | (512, 512) | 262144 | Matrix |
| mobilenet_v1.layer.17.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.17.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.18.convolution.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| mobilenet_v1.layer.18.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.18.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.19.convolution.weight | (512, 512, 1, 1) | (512, 512) | 262144 | Matrix |
| mobilenet_v1.layer.19.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.19.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.20.convolution.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| mobilenet_v1.layer.20.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.20.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.21.convolution.weight | (512, 512, 1, 1) | (512, 512) | 262144 | Matrix |
| mobilenet_v1.layer.21.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.21.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.22.convolution.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| mobilenet_v1.layer.22.normalization.weight | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.22.normalization.bias | (512,) | (512,) | 512 | Vector |
| mobilenet_v1.layer.23.convolution.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| mobilenet_v1.layer.23.normalization.weight | (1024,) | (1024,) | 1024 | Vector |
| mobilenet_v1.layer.23.normalization.bias | (1024,) | (1024,) | 1024 | Vector |
| mobilenet_v1.layer.24.convolution.weight | (1024, 1, 3, 3) | (1024, 3, 3) | 9216 | Tensor rank 3 |
| mobilenet_v1.layer.24.normalization.weight | (1024,) | (1024,) | 1024 | Vector |
| mobilenet_v1.layer.24.normalization.bias | (1024,) | (1024,) | 1024 | Vector |
| mobilenet_v1.layer.25.convolution.weight | (1024, 1024, 1, 1) | (1024, 1024) | 1048576 | Matrix |
| mobilenet_v1.layer.25.normalization.weight | (1024,) | (1024,) | 1024 | Vector |
| mobilenet_v1.layer.25.normalization.bias | (1024,) | (1024,) | 1024 | Vector |
| classifier.weight | (2, 1024) | (2, 1024) | 2048 | Matrix |
| classifier.bias | (2,) | (2,) | 2 | Vector |

