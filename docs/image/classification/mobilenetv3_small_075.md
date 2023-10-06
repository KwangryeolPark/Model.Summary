# mobilenetv3_small_075 parameter information

**Number of layers: [ 142 ]**

**Number of parameters: [ 7.789 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 7.789 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.97 | 29.58 | 7.75 | 0.70 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.69 | 97.01 | 2.28 | 0.02 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (16, 3, 3, 3) | (16, 3, 3, 3) | 432 | Tensor rank 4 |
| bn1.weight | (16,) | (16,) | 16 | Vector |
| bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.conv_dw.weight | (16, 1, 3, 3) | (16, 3, 3) | 144 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.se.conv_reduce.weight | (8, 16, 1, 1) | (8, 16) | 128 | Matrix |
| blocks.0.0.se.conv_reduce.bias | (8,) | (8,) | 8 | Vector |
| blocks.0.0.se.conv_expand.weight | (16, 8, 1, 1) | (16, 8) | 128 | Matrix |
| blocks.0.0.se.conv_expand.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.conv_pw.weight | (16, 16, 1, 1) | (16, 16) | 256 | Matrix |
| blocks.0.0.bn2.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn2.bias | (16,) | (16,) | 16 | Vector |
| blocks.1.0.conv_pw.weight | (72, 16, 1, 1) | (72, 16) | 1152 | Matrix |
| blocks.1.0.bn1.weight | (72,) | (72,) | 72 | Vector |
| blocks.1.0.bn1.bias | (72,) | (72,) | 72 | Vector |
| blocks.1.0.conv_dw.weight | (72, 1, 3, 3) | (72, 3, 3) | 648 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (72,) | (72,) | 72 | Vector |
| blocks.1.0.bn2.bias | (72,) | (72,) | 72 | Vector |
| blocks.1.0.conv_pwl.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.1.0.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.0.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.1.conv_pw.weight | (88, 24, 1, 1) | (88, 24) | 2112 | Matrix |
| blocks.1.1.bn1.weight | (88,) | (88,) | 88 | Vector |
| blocks.1.1.bn1.bias | (88,) | (88,) | 88 | Vector |
| blocks.1.1.conv_dw.weight | (88, 1, 3, 3) | (88, 3, 3) | 792 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (88,) | (88,) | 88 | Vector |
| blocks.1.1.bn2.bias | (88,) | (88,) | 88 | Vector |
| blocks.1.1.conv_pwl.weight | (24, 88, 1, 1) | (24, 88) | 2112 | Matrix |
| blocks.1.1.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.1.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.0.conv_pw.weight | (96, 24, 1, 1) | (96, 24) | 2304 | Matrix |
| blocks.2.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.0.conv_dw.weight | (96, 1, 5, 5) | (96, 5, 5) | 2400 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.0.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.0.se.conv_reduce.weight | (24, 96, 1, 1) | (24, 96) | 2304 | Matrix |
| blocks.2.0.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.0.se.conv_expand.weight | (96, 24, 1, 1) | (96, 24) | 2304 | Matrix |
| blocks.2.0.se.conv_expand.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.0.conv_pwl.weight | (32, 96, 1, 1) | (32, 96) | 3072 | Matrix |
| blocks.2.0.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.0.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.1.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.1.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.1.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.1.conv_dw.weight | (192, 1, 5, 5) | (192, 5, 5) | 4800 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.1.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.1.se.conv_reduce.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.1.se.conv_expand.weight | (192, 48, 1, 1) | (192, 48) | 9216 | Matrix |
| blocks.2.1.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.1.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.2.1.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.1.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.2.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.2.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.2.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.2.conv_dw.weight | (192, 1, 5, 5) | (192, 5, 5) | 4800 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.2.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.2.se.conv_reduce.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.2.se.conv_expand.weight | (192, 48, 1, 1) | (192, 48) | 9216 | Matrix |
| blocks.2.2.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.2.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.2.2.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.2.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.0.conv_pw.weight | (96, 32, 1, 1) | (96, 32) | 3072 | Matrix |
| blocks.3.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.0.conv_dw.weight | (96, 1, 5, 5) | (96, 5, 5) | 2400 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.0.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.0.se.conv_reduce.weight | (24, 96, 1, 1) | (24, 96) | 2304 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.0.se.conv_expand.weight | (96, 24, 1, 1) | (96, 24) | 2304 | Matrix |
| blocks.3.0.se.conv_expand.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.0.conv_pwl.weight | (40, 96, 1, 1) | (40, 96) | 3840 | Matrix |
| blocks.3.0.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.3.0.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.3.1.conv_pw.weight | (120, 40, 1, 1) | (120, 40) | 4800 | Matrix |
| blocks.3.1.bn1.weight | (120,) | (120,) | 120 | Vector |
| blocks.3.1.bn1.bias | (120,) | (120,) | 120 | Vector |
| blocks.3.1.conv_dw.weight | (120, 1, 5, 5) | (120, 5, 5) | 3000 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (120,) | (120,) | 120 | Vector |
| blocks.3.1.bn2.bias | (120,) | (120,) | 120 | Vector |
| blocks.3.1.se.conv_reduce.weight | (32, 120, 1, 1) | (32, 120) | 3840 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.1.se.conv_expand.weight | (120, 32, 1, 1) | (120, 32) | 3840 | Matrix |
| blocks.3.1.se.conv_expand.bias | (120,) | (120,) | 120 | Vector |
| blocks.3.1.conv_pwl.weight | (40, 120, 1, 1) | (40, 120) | 4800 | Matrix |
| blocks.3.1.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.3.1.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.0.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.4.0.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.4.0.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.4.0.conv_dw.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.4.0.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.4.0.se.conv_reduce.weight | (64, 240, 1, 1) | (64, 240) | 15360 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (64,) | (64,) | 64 | Vector |
| blocks.4.0.se.conv_expand.weight | (240, 64, 1, 1) | (240, 64) | 15360 | Matrix |
| blocks.4.0.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.4.0.conv_pwl.weight | (72, 240, 1, 1) | (72, 240) | 17280 | Matrix |
| blocks.4.0.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.4.0.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.4.1.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.4.1.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.4.1.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.1.conv_dw.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.4.1.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.1.se.conv_reduce.weight | (112, 432, 1, 1) | (112, 432) | 48384 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.1.se.conv_expand.weight | (432, 112, 1, 1) | (432, 112) | 48384 | Matrix |
| blocks.4.1.se.conv_expand.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.1.conv_pwl.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| blocks.4.1.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.4.1.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.4.2.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.4.2.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.4.2.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.2.conv_dw.weight | (432, 1, 5, 5) | (432, 5, 5) | 10800 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.4.2.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.2.se.conv_reduce.weight | (112, 432, 1, 1) | (112, 432) | 48384 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.2.se.conv_expand.weight | (432, 112, 1, 1) | (432, 112) | 48384 | Matrix |
| blocks.4.2.se.conv_expand.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.2.conv_pwl.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| blocks.4.2.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.4.2.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.5.0.conv.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.5.0.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.5.0.bn1.bias | (432,) | (432,) | 432 | Vector |
| conv_head.weight | (1024, 432, 1, 1) | (1024, 432) | 442368 | Matrix |
| conv_head.bias | (1024,) | (1024,) | 1024 | Vector |
| classifier.weight | (1000, 1024) | (1000, 1024) | 1024000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

