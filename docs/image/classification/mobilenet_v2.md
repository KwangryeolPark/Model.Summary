# mobilenet_v2 parameter information

**Number of layers: [ 158 ]**

**Number of parameters: [ 8.493 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 8.493 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.46 | 22.15 | 10.76 | 0.63 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 1.53 | 95.54 | 2.88 | 0.04 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| mobilenet_v2.conv_stem.first_conv.convolution.weight | (32, 3, 3, 3) | (32, 3, 3, 3) | 864 | Tensor rank 4 |
| mobilenet_v2.conv_stem.first_conv.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.conv_stem.first_conv.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.conv_stem.conv_3x3.convolution.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| mobilenet_v2.conv_stem.conv_3x3.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.conv_stem.conv_3x3.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.conv_stem.reduce_1x1.convolution.weight | (16, 32, 1, 1) | (16, 32) | 512 | Matrix |
| mobilenet_v2.conv_stem.reduce_1x1.normalization.weight | (16,) | (16,) | 16 | Vector |
| mobilenet_v2.conv_stem.reduce_1x1.normalization.bias | (16,) | (16,) | 16 | Vector |
| mobilenet_v2.layer.0.expand_1x1.convolution.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| mobilenet_v2.layer.0.expand_1x1.normalization.weight | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.0.expand_1x1.normalization.bias | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.0.conv_3x3.convolution.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| mobilenet_v2.layer.0.conv_3x3.normalization.weight | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.0.conv_3x3.normalization.bias | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.0.reduce_1x1.convolution.weight | (24, 96, 1, 1) | (24, 96) | 2304 | Matrix |
| mobilenet_v2.layer.0.reduce_1x1.normalization.weight | (24,) | (24,) | 24 | Vector |
| mobilenet_v2.layer.0.reduce_1x1.normalization.bias | (24,) | (24,) | 24 | Vector |
| mobilenet_v2.layer.1.expand_1x1.convolution.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| mobilenet_v2.layer.1.expand_1x1.normalization.weight | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.1.expand_1x1.normalization.bias | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.1.conv_3x3.convolution.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| mobilenet_v2.layer.1.conv_3x3.normalization.weight | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.1.conv_3x3.normalization.bias | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.1.reduce_1x1.convolution.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| mobilenet_v2.layer.1.reduce_1x1.normalization.weight | (24,) | (24,) | 24 | Vector |
| mobilenet_v2.layer.1.reduce_1x1.normalization.bias | (24,) | (24,) | 24 | Vector |
| mobilenet_v2.layer.2.expand_1x1.convolution.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| mobilenet_v2.layer.2.expand_1x1.normalization.weight | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.2.expand_1x1.normalization.bias | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.2.conv_3x3.convolution.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| mobilenet_v2.layer.2.conv_3x3.normalization.weight | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.2.conv_3x3.normalization.bias | (144,) | (144,) | 144 | Vector |
| mobilenet_v2.layer.2.reduce_1x1.convolution.weight | (32, 144, 1, 1) | (32, 144) | 4608 | Matrix |
| mobilenet_v2.layer.2.reduce_1x1.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.layer.2.reduce_1x1.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.layer.3.expand_1x1.convolution.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| mobilenet_v2.layer.3.expand_1x1.normalization.weight | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.3.expand_1x1.normalization.bias | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.3.conv_3x3.convolution.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| mobilenet_v2.layer.3.conv_3x3.normalization.weight | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.3.conv_3x3.normalization.bias | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.3.reduce_1x1.convolution.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| mobilenet_v2.layer.3.reduce_1x1.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.layer.3.reduce_1x1.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.layer.4.expand_1x1.convolution.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| mobilenet_v2.layer.4.expand_1x1.normalization.weight | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.4.expand_1x1.normalization.bias | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.4.conv_3x3.convolution.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| mobilenet_v2.layer.4.conv_3x3.normalization.weight | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.4.conv_3x3.normalization.bias | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.4.reduce_1x1.convolution.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| mobilenet_v2.layer.4.reduce_1x1.normalization.weight | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.layer.4.reduce_1x1.normalization.bias | (32,) | (32,) | 32 | Vector |
| mobilenet_v2.layer.5.expand_1x1.convolution.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| mobilenet_v2.layer.5.expand_1x1.normalization.weight | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.5.expand_1x1.normalization.bias | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.5.conv_3x3.convolution.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| mobilenet_v2.layer.5.conv_3x3.normalization.weight | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.5.conv_3x3.normalization.bias | (192,) | (192,) | 192 | Vector |
| mobilenet_v2.layer.5.reduce_1x1.convolution.weight | (64, 192, 1, 1) | (64, 192) | 12288 | Matrix |
| mobilenet_v2.layer.5.reduce_1x1.normalization.weight | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.5.reduce_1x1.normalization.bias | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.6.expand_1x1.convolution.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| mobilenet_v2.layer.6.expand_1x1.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.6.expand_1x1.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.6.conv_3x3.convolution.weight | (384, 1, 3, 3) | (384, 3, 3) | 3456 | Tensor rank 3 |
| mobilenet_v2.layer.6.conv_3x3.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.6.conv_3x3.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.6.reduce_1x1.convolution.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| mobilenet_v2.layer.6.reduce_1x1.normalization.weight | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.6.reduce_1x1.normalization.bias | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.7.expand_1x1.convolution.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| mobilenet_v2.layer.7.expand_1x1.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.7.expand_1x1.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.7.conv_3x3.convolution.weight | (384, 1, 3, 3) | (384, 3, 3) | 3456 | Tensor rank 3 |
| mobilenet_v2.layer.7.conv_3x3.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.7.conv_3x3.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.7.reduce_1x1.convolution.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| mobilenet_v2.layer.7.reduce_1x1.normalization.weight | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.7.reduce_1x1.normalization.bias | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.8.expand_1x1.convolution.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| mobilenet_v2.layer.8.expand_1x1.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.8.expand_1x1.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.8.conv_3x3.convolution.weight | (384, 1, 3, 3) | (384, 3, 3) | 3456 | Tensor rank 3 |
| mobilenet_v2.layer.8.conv_3x3.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.8.conv_3x3.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.8.reduce_1x1.convolution.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| mobilenet_v2.layer.8.reduce_1x1.normalization.weight | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.8.reduce_1x1.normalization.bias | (64,) | (64,) | 64 | Vector |
| mobilenet_v2.layer.9.expand_1x1.convolution.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| mobilenet_v2.layer.9.expand_1x1.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.9.expand_1x1.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.9.conv_3x3.convolution.weight | (384, 1, 3, 3) | (384, 3, 3) | 3456 | Tensor rank 3 |
| mobilenet_v2.layer.9.conv_3x3.normalization.weight | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.9.conv_3x3.normalization.bias | (384,) | (384,) | 384 | Vector |
| mobilenet_v2.layer.9.reduce_1x1.convolution.weight | (96, 384, 1, 1) | (96, 384) | 36864 | Matrix |
| mobilenet_v2.layer.9.reduce_1x1.normalization.weight | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.9.reduce_1x1.normalization.bias | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.10.expand_1x1.convolution.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| mobilenet_v2.layer.10.expand_1x1.normalization.weight | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.10.expand_1x1.normalization.bias | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.10.conv_3x3.convolution.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| mobilenet_v2.layer.10.conv_3x3.normalization.weight | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.10.conv_3x3.normalization.bias | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.10.reduce_1x1.convolution.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| mobilenet_v2.layer.10.reduce_1x1.normalization.weight | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.10.reduce_1x1.normalization.bias | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.11.expand_1x1.convolution.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| mobilenet_v2.layer.11.expand_1x1.normalization.weight | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.11.expand_1x1.normalization.bias | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.11.conv_3x3.convolution.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| mobilenet_v2.layer.11.conv_3x3.normalization.weight | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.11.conv_3x3.normalization.bias | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.11.reduce_1x1.convolution.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| mobilenet_v2.layer.11.reduce_1x1.normalization.weight | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.11.reduce_1x1.normalization.bias | (96,) | (96,) | 96 | Vector |
| mobilenet_v2.layer.12.expand_1x1.convolution.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| mobilenet_v2.layer.12.expand_1x1.normalization.weight | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.12.expand_1x1.normalization.bias | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.12.conv_3x3.convolution.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| mobilenet_v2.layer.12.conv_3x3.normalization.weight | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.12.conv_3x3.normalization.bias | (576,) | (576,) | 576 | Vector |
| mobilenet_v2.layer.12.reduce_1x1.convolution.weight | (160, 576, 1, 1) | (160, 576) | 92160 | Matrix |
| mobilenet_v2.layer.12.reduce_1x1.normalization.weight | (160,) | (160,) | 160 | Vector |
| mobilenet_v2.layer.12.reduce_1x1.normalization.bias | (160,) | (160,) | 160 | Vector |
| mobilenet_v2.layer.13.expand_1x1.convolution.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| mobilenet_v2.layer.13.expand_1x1.normalization.weight | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.13.expand_1x1.normalization.bias | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.13.conv_3x3.convolution.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| mobilenet_v2.layer.13.conv_3x3.normalization.weight | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.13.conv_3x3.normalization.bias | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.13.reduce_1x1.convolution.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| mobilenet_v2.layer.13.reduce_1x1.normalization.weight | (160,) | (160,) | 160 | Vector |
| mobilenet_v2.layer.13.reduce_1x1.normalization.bias | (160,) | (160,) | 160 | Vector |
| mobilenet_v2.layer.14.expand_1x1.convolution.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| mobilenet_v2.layer.14.expand_1x1.normalization.weight | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.14.expand_1x1.normalization.bias | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.14.conv_3x3.convolution.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| mobilenet_v2.layer.14.conv_3x3.normalization.weight | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.14.conv_3x3.normalization.bias | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.14.reduce_1x1.convolution.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| mobilenet_v2.layer.14.reduce_1x1.normalization.weight | (160,) | (160,) | 160 | Vector |
| mobilenet_v2.layer.14.reduce_1x1.normalization.bias | (160,) | (160,) | 160 | Vector |
| mobilenet_v2.layer.15.expand_1x1.convolution.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| mobilenet_v2.layer.15.expand_1x1.normalization.weight | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.15.expand_1x1.normalization.bias | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.15.conv_3x3.convolution.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| mobilenet_v2.layer.15.conv_3x3.normalization.weight | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.15.conv_3x3.normalization.bias | (960,) | (960,) | 960 | Vector |
| mobilenet_v2.layer.15.reduce_1x1.convolution.weight | (320, 960, 1, 1) | (320, 960) | 307200 | Matrix |
| mobilenet_v2.layer.15.reduce_1x1.normalization.weight | (320,) | (320,) | 320 | Vector |
| mobilenet_v2.layer.15.reduce_1x1.normalization.bias | (320,) | (320,) | 320 | Vector |
| mobilenet_v2.conv_1x1.convolution.weight | (1280, 320, 1, 1) | (1280, 320) | 409600 | Matrix |
| mobilenet_v2.conv_1x1.normalization.weight | (1280,) | (1280,) | 1280 | Vector |
| mobilenet_v2.conv_1x1.normalization.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.weight | (2, 1280) | (2, 1280) | 2560 | Matrix |
| classifier.bias | (2,) | (2,) | 2 | Vector |

