# mobilenetv3_small_100 parameter information

**Number of layers: [ 142 ]**

**Number of parameters: [ 9.700 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 9.700 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.97 | 29.58 | 7.75 | 0.70 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.67 | 97.01 | 2.30 | 0.02 | 

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
| blocks.2.0.conv_pwl.weight | (40, 96, 1, 1) | (40, 96) | 3840 | Matrix |
| blocks.2.0.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.0.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.1.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.1.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.1.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.conv_dw.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.1.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.se.conv_reduce.weight | (64, 240, 1, 1) | (64, 240) | 15360 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.1.se.conv_expand.weight | (240, 64, 1, 1) | (240, 64) | 15360 | Matrix |
| blocks.2.1.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.1.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.1.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.2.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.2.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.2.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.2.conv_dw.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.2.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.2.se.conv_reduce.weight | (64, 240, 1, 1) | (64, 240) | 15360 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.2.se.conv_expand.weight | (240, 64, 1, 1) | (240, 64) | 15360 | Matrix |
| blocks.2.2.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.2.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.2.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.2.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.3.0.conv_pw.weight | (120, 40, 1, 1) | (120, 40) | 4800 | Matrix |
| blocks.3.0.bn1.weight | (120,) | (120,) | 120 | Vector |
| blocks.3.0.bn1.bias | (120,) | (120,) | 120 | Vector |
| blocks.3.0.conv_dw.weight | (120, 1, 5, 5) | (120, 5, 5) | 3000 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (120,) | (120,) | 120 | Vector |
| blocks.3.0.bn2.bias | (120,) | (120,) | 120 | Vector |
| blocks.3.0.se.conv_reduce.weight | (32, 120, 1, 1) | (32, 120) | 3840 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.0.se.conv_expand.weight | (120, 32, 1, 1) | (120, 32) | 3840 | Matrix |
| blocks.3.0.se.conv_expand.bias | (120,) | (120,) | 120 | Vector |
| blocks.3.0.conv_pwl.weight | (48, 120, 1, 1) | (48, 120) | 5760 | Matrix |
| blocks.3.0.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.3.0.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.3.1.conv_pw.weight | (144, 48, 1, 1) | (144, 48) | 6912 | Matrix |
| blocks.3.1.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.3.1.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.3.1.conv_dw.weight | (144, 1, 5, 5) | (144, 5, 5) | 3600 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.3.1.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.3.1.se.conv_reduce.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.3.1.se.conv_expand.weight | (144, 40, 1, 1) | (144, 40) | 5760 | Matrix |
| blocks.3.1.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.3.1.conv_pwl.weight | (48, 144, 1, 1) | (48, 144) | 6912 | Matrix |
| blocks.3.1.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.3.1.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.4.0.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.4.0.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.0.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.0.conv_dw.weight | (288, 1, 5, 5) | (288, 5, 5) | 7200 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.0.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.0.se.conv_reduce.weight | (72, 288, 1, 1) | (72, 288) | 20736 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (72,) | (72,) | 72 | Vector |
| blocks.4.0.se.conv_expand.weight | (288, 72, 1, 1) | (288, 72) | 20736 | Matrix |
| blocks.4.0.se.conv_expand.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.0.conv_pwl.weight | (96, 288, 1, 1) | (96, 288) | 27648 | Matrix |
| blocks.4.0.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.4.0.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.4.1.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.4.1.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.4.1.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.1.conv_dw.weight | (576, 1, 5, 5) | (576, 5, 5) | 14400 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.4.1.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.1.se.conv_reduce.weight | (144, 576, 1, 1) | (144, 576) | 82944 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (144,) | (144,) | 144 | Vector |
| blocks.4.1.se.conv_expand.weight | (576, 144, 1, 1) | (576, 144) | 82944 | Matrix |
| blocks.4.1.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.1.conv_pwl.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| blocks.4.1.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.4.1.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.4.2.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.4.2.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.4.2.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.2.conv_dw.weight | (576, 1, 5, 5) | (576, 5, 5) | 14400 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.4.2.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.2.se.conv_reduce.weight | (144, 576, 1, 1) | (144, 576) | 82944 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (144,) | (144,) | 144 | Vector |
| blocks.4.2.se.conv_expand.weight | (576, 144, 1, 1) | (576, 144) | 82944 | Matrix |
| blocks.4.2.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.2.conv_pwl.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| blocks.4.2.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.4.2.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.5.0.conv.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.5.0.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.5.0.bn1.bias | (576,) | (576,) | 576 | Vector |
| conv_head.weight | (1024, 576, 1, 1) | (1024, 576) | 589824 | Matrix |
| conv_head.bias | (1024,) | (1024,) | 1024 | Vector |
| classifier.weight | (1000, 1024) | (1000, 1024) | 1024000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

