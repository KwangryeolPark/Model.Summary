# mobilenetv2_050 parameter information

**Number of layers: [ 158 ]**

**Number of parameters: [ 7.510 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 7.510 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.46 | 22.15 | 10.76 | 0.63 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.99 | 97.33 | 1.65 | 0.02 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (16, 3, 3, 3) | (16, 3, 3, 3) | 432 | Tensor rank 4 |
| bn1.weight | (16,) | (16,) | 16 | Vector |
| bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.conv_dw.weight | (16, 1, 3, 3) | (16, 3, 3) | 144 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.conv_pw.weight | (8, 16, 1, 1) | (8, 16) | 128 | Matrix |
| blocks.0.0.bn2.weight | (8,) | (8,) | 8 | Vector |
| blocks.0.0.bn2.bias | (8,) | (8,) | 8 | Vector |
| blocks.1.0.conv_pw.weight | (48, 8, 1, 1) | (48, 8) | 384 | Matrix |
| blocks.1.0.bn1.weight | (48,) | (48,) | 48 | Vector |
| blocks.1.0.bn1.bias | (48,) | (48,) | 48 | Vector |
| blocks.1.0.conv_dw.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (48,) | (48,) | 48 | Vector |
| blocks.1.0.bn2.bias | (48,) | (48,) | 48 | Vector |
| blocks.1.0.conv_pwl.weight | (16, 48, 1, 1) | (16, 48) | 768 | Matrix |
| blocks.1.0.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.1.0.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.1.1.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.1.1.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.1.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.1.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.1.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.1.conv_pwl.weight | (16, 96, 1, 1) | (16, 96) | 1536 | Matrix |
| blocks.1.1.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.1.1.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.0.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.2.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.0.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.0.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.0.conv_pwl.weight | (16, 96, 1, 1) | (16, 96) | 1536 | Matrix |
| blocks.2.0.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.2.0.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.1.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.2.1.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.1.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.1.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.1.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.1.conv_pwl.weight | (16, 96, 1, 1) | (16, 96) | 1536 | Matrix |
| blocks.2.1.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.2.1.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.2.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.2.2.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.2.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.2.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.2.2.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.2.2.conv_pwl.weight | (16, 96, 1, 1) | (16, 96) | 1536 | Matrix |
| blocks.2.2.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.2.2.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.3.0.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.3.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.0.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.0.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.0.conv_pwl.weight | (32, 96, 1, 1) | (32, 96) | 3072 | Matrix |
| blocks.3.0.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.3.0.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.1.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.3.1.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.1.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.1.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.1.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.1.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.3.1.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.3.1.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.2.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.3.2.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.2.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.2.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.2.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.2.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.3.2.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.3.2.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.3.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.3.3.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.3.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.3.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.3.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.3.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.3.3.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.3.3.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.0.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.4.0.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.4.0.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.4.0.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.4.0.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.4.0.conv_pwl.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.4.0.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.4.0.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.4.1.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.4.1.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.1.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.1.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.1.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.1.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.4.1.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.4.1.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.4.2.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.4.2.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.2.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.2.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.2.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.2.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.4.2.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.4.2.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.5.0.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.5.0.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.5.0.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.5.0.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.5.0.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.5.0.conv_pwl.weight | (80, 288, 1, 1) | (80, 288) | 23040 | Matrix |
| blocks.5.0.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.5.0.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.5.1.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.5.1.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.5.1.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.5.1.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.5.1.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.5.1.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.5.1.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.5.1.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.5.2.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.5.2.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.5.2.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.5.2.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.5.2.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.5.2.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.5.2.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.5.2.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.6.0.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.6.0.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.6.0.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.6.0.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.6.0.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.6.0.conv_pwl.weight | (160, 480, 1, 1) | (160, 480) | 76800 | Matrix |
| blocks.6.0.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.6.0.bn3.bias | (160,) | (160,) | 160 | Vector |
| conv_head.weight | (1280, 160, 1, 1) | (1280, 160) | 204800 | Matrix |
| bn2.weight | (1280,) | (1280,) | 1280 | Vector |
| bn2.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

