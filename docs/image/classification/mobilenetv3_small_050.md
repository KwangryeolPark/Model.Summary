# mobilenetv3_small_050 parameter information

**Number of layers: [ 142 ]**

**Number of parameters: [ 6.078 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 6.078 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.97 | 29.58 | 7.75 | 0.70 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.63 | 97.37 | 1.97 | 0.03 | 

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
| blocks.0.0.conv_pw.weight | (8, 16, 1, 1) | (8, 16) | 128 | Matrix |
| blocks.0.0.bn2.weight | (8,) | (8,) | 8 | Vector |
| blocks.0.0.bn2.bias | (8,) | (8,) | 8 | Vector |
| blocks.1.0.conv_pw.weight | (40, 8, 1, 1) | (40, 8) | 320 | Matrix |
| blocks.1.0.bn1.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.0.bn1.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.0.conv_dw.weight | (40, 1, 3, 3) | (40, 3, 3) | 360 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.0.bn2.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.0.conv_pwl.weight | (16, 40, 1, 1) | (16, 40) | 640 | Matrix |
| blocks.1.0.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.1.0.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.1.1.conv_pw.weight | (56, 16, 1, 1) | (56, 16) | 896 | Matrix |
| blocks.1.1.bn1.weight | (56,) | (56,) | 56 | Vector |
| blocks.1.1.bn1.bias | (56,) | (56,) | 56 | Vector |
| blocks.1.1.conv_dw.weight | (56, 1, 3, 3) | (56, 3, 3) | 504 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (56,) | (56,) | 56 | Vector |
| blocks.1.1.bn2.bias | (56,) | (56,) | 56 | Vector |
| blocks.1.1.conv_pwl.weight | (16, 56, 1, 1) | (16, 56) | 896 | Matrix |
| blocks.1.1.bn3.weight | (16,) | (16,) | 16 | Vector |
| blocks.1.1.bn3.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.0.conv_pw.weight | (64, 16, 1, 1) | (64, 16) | 1024 | Matrix |
| blocks.2.0.bn1.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.0.bn1.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.0.conv_dw.weight | (64, 1, 5, 5) | (64, 5, 5) | 1600 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.0.bn2.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.0.se.conv_reduce.weight | (16, 64, 1, 1) | (16, 64) | 1024 | Matrix |
| blocks.2.0.se.conv_reduce.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.0.se.conv_expand.weight | (64, 16, 1, 1) | (64, 16) | 1024 | Matrix |
| blocks.2.0.se.conv_expand.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.0.conv_pwl.weight | (24, 64, 1, 1) | (24, 64) | 1536 | Matrix |
| blocks.2.0.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.2.0.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.1.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.2.1.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.1.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.1.conv_dw.weight | (144, 1, 5, 5) | (144, 5, 5) | 3600 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.1.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.1.se.conv_reduce.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.1.se.conv_expand.weight | (144, 40, 1, 1) | (144, 40) | 5760 | Matrix |
| blocks.2.1.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.1.conv_pwl.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| blocks.2.1.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.2.1.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.2.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.2.2.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.2.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.2.conv_dw.weight | (144, 1, 5, 5) | (144, 5, 5) | 3600 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.2.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.2.se.conv_reduce.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.2.se.conv_expand.weight | (144, 40, 1, 1) | (144, 40) | 5760 | Matrix |
| blocks.2.2.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.2.conv_pwl.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| blocks.2.2.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.2.2.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.0.conv_pw.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.3.0.bn1.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.0.bn1.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.0.conv_dw.weight | (72, 1, 5, 5) | (72, 5, 5) | 1800 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.0.bn2.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.0.se.conv_reduce.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.0.se.conv_expand.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.3.0.se.conv_expand.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.0.conv_pwl.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.3.0.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.3.0.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.1.conv_pw.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.3.1.bn1.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.1.bn1.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.1.conv_dw.weight | (72, 1, 5, 5) | (72, 5, 5) | 1800 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.1.bn2.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.1.se.conv_reduce.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.1.se.conv_expand.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.3.1.se.conv_expand.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.1.conv_pwl.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.3.1.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.3.1.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.4.0.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.4.0.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.4.0.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.4.0.conv_dw.weight | (144, 1, 5, 5) | (144, 5, 5) | 3600 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.4.0.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.4.0.se.conv_reduce.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.0.se.conv_expand.weight | (144, 40, 1, 1) | (144, 40) | 5760 | Matrix |
| blocks.4.0.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.4.0.conv_pwl.weight | (48, 144, 1, 1) | (48, 144) | 6912 | Matrix |
| blocks.4.0.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.4.0.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.4.1.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.4.1.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.1.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.1.conv_dw.weight | (288, 1, 5, 5) | (288, 5, 5) | 7200 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.1.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.1.se.conv_reduce.weight | (72, 288, 1, 1) | (72, 288) | 20736 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (72,) | (72,) | 72 | Vector |
| blocks.4.1.se.conv_expand.weight | (288, 72, 1, 1) | (288, 72) | 20736 | Matrix |
| blocks.4.1.se.conv_expand.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.1.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.4.1.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.4.1.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.4.2.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.4.2.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.2.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.2.conv_dw.weight | (288, 1, 5, 5) | (288, 5, 5) | 7200 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.4.2.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.2.se.conv_reduce.weight | (72, 288, 1, 1) | (72, 288) | 20736 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (72,) | (72,) | 72 | Vector |
| blocks.4.2.se.conv_expand.weight | (288, 72, 1, 1) | (288, 72) | 20736 | Matrix |
| blocks.4.2.se.conv_expand.bias | (288,) | (288,) | 288 | Vector |
| blocks.4.2.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.4.2.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.4.2.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.5.0.conv.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.5.0.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.5.0.bn1.bias | (288,) | (288,) | 288 | Vector |
| conv_head.weight | (1024, 288, 1, 1) | (1024, 288) | 294912 | Matrix |
| conv_head.bias | (1024,) | (1024,) | 1024 | Vector |
| classifier.weight | (1000, 1024) | (1000, 1024) | 1024000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

