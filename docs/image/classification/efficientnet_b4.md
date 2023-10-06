# efficientnet_b4 parameter information

**Number of layers: [ 418 ]**

**Number of parameters: [ 73.782 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 73.782 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.48 | 30.62 | 7.66 | 0.24 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.80 | 96.32 | 2.87 | 0.01 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (48, 3, 3, 3) | (48, 3, 3, 3) | 1296 | Tensor rank 4 |
| bn1.weight | (48,) | (48,) | 48 | Vector |
| bn1.bias | (48,) | (48,) | 48 | Vector |
| blocks.0.0.conv_dw.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (48,) | (48,) | 48 | Vector |
| blocks.0.0.bn1.bias | (48,) | (48,) | 48 | Vector |
| blocks.0.0.se.conv_reduce.weight | (12, 48, 1, 1) | (12, 48) | 576 | Matrix |
| blocks.0.0.se.conv_reduce.bias | (12,) | (12,) | 12 | Vector |
| blocks.0.0.se.conv_expand.weight | (48, 12, 1, 1) | (48, 12) | 576 | Matrix |
| blocks.0.0.se.conv_expand.bias | (48,) | (48,) | 48 | Vector |
| blocks.0.0.conv_pw.weight | (24, 48, 1, 1) | (24, 48) | 1152 | Matrix |
| blocks.0.0.bn2.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.0.bn2.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.1.conv_dw.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| blocks.0.1.bn1.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.1.bn1.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.1.se.conv_reduce.weight | (6, 24, 1, 1) | (6, 24) | 144 | Matrix |
| blocks.0.1.se.conv_reduce.bias | (6,) | (6,) | 6 | Vector |
| blocks.0.1.se.conv_expand.weight | (24, 6, 1, 1) | (24, 6) | 144 | Matrix |
| blocks.0.1.se.conv_expand.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.1.conv_pw.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| blocks.0.1.bn2.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.1.bn2.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.0.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.1.0.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.0.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.0.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.0.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.0.se.conv_reduce.weight | (6, 144, 1, 1) | (6, 144) | 864 | Matrix |
| blocks.1.0.se.conv_reduce.bias | (6,) | (6,) | 6 | Vector |
| blocks.1.0.se.conv_expand.weight | (144, 6, 1, 1) | (144, 6) | 864 | Matrix |
| blocks.1.0.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.0.conv_pwl.weight | (32, 144, 1, 1) | (32, 144) | 4608 | Matrix |
| blocks.1.0.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.0.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.1.1.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.1.1.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.1.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.1.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.1.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.1.se.conv_reduce.weight | (8, 192, 1, 1) | (8, 192) | 1536 | Matrix |
| blocks.1.1.se.conv_reduce.bias | (8,) | (8,) | 8 | Vector |
| blocks.1.1.se.conv_expand.weight | (192, 8, 1, 1) | (192, 8) | 1536 | Matrix |
| blocks.1.1.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.1.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.1.1.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.1.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.1.2.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.1.2.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.2.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.2.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.1.2.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.2.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.2.se.conv_reduce.weight | (8, 192, 1, 1) | (8, 192) | 1536 | Matrix |
| blocks.1.2.se.conv_reduce.bias | (8,) | (8,) | 8 | Vector |
| blocks.1.2.se.conv_expand.weight | (192, 8, 1, 1) | (192, 8) | 1536 | Matrix |
| blocks.1.2.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.2.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.1.2.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.2.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.1.3.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.1.3.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.3.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.3.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.1.3.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.3.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.3.se.conv_reduce.weight | (8, 192, 1, 1) | (8, 192) | 1536 | Matrix |
| blocks.1.3.se.conv_reduce.bias | (8,) | (8,) | 8 | Vector |
| blocks.1.3.se.conv_expand.weight | (192, 8, 1, 1) | (192, 8) | 1536 | Matrix |
| blocks.1.3.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.3.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.1.3.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.3.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.0.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.0.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.0.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.conv_dw.weight | (192, 1, 5, 5) | (192, 5, 5) | 4800 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.0.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.se.conv_reduce.weight | (8, 192, 1, 1) | (8, 192) | 1536 | Matrix |
| blocks.2.0.se.conv_reduce.bias | (8,) | (8,) | 8 | Vector |
| blocks.2.0.se.conv_expand.weight | (192, 8, 1, 1) | (192, 8) | 1536 | Matrix |
| blocks.2.0.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.conv_pwl.weight | (56, 192, 1, 1) | (56, 192) | 10752 | Matrix |
| blocks.2.0.bn3.weight | (56,) | (56,) | 56 | Vector |
| blocks.2.0.bn3.bias | (56,) | (56,) | 56 | Vector |
| blocks.2.1.conv_pw.weight | (336, 56, 1, 1) | (336, 56) | 18816 | Matrix |
| blocks.2.1.bn1.weight | (336,) | (336,) | 336 | Vector |
| blocks.2.1.bn1.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.1.conv_dw.weight | (336, 1, 5, 5) | (336, 5, 5) | 8400 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (336,) | (336,) | 336 | Vector |
| blocks.2.1.bn2.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.1.se.conv_reduce.weight | (14, 336, 1, 1) | (14, 336) | 4704 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (14,) | (14,) | 14 | Vector |
| blocks.2.1.se.conv_expand.weight | (336, 14, 1, 1) | (336, 14) | 4704 | Matrix |
| blocks.2.1.se.conv_expand.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.1.conv_pwl.weight | (56, 336, 1, 1) | (56, 336) | 18816 | Matrix |
| blocks.2.1.bn3.weight | (56,) | (56,) | 56 | Vector |
| blocks.2.1.bn3.bias | (56,) | (56,) | 56 | Vector |
| blocks.2.2.conv_pw.weight | (336, 56, 1, 1) | (336, 56) | 18816 | Matrix |
| blocks.2.2.bn1.weight | (336,) | (336,) | 336 | Vector |
| blocks.2.2.bn1.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.2.conv_dw.weight | (336, 1, 5, 5) | (336, 5, 5) | 8400 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (336,) | (336,) | 336 | Vector |
| blocks.2.2.bn2.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.2.se.conv_reduce.weight | (14, 336, 1, 1) | (14, 336) | 4704 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (14,) | (14,) | 14 | Vector |
| blocks.2.2.se.conv_expand.weight | (336, 14, 1, 1) | (336, 14) | 4704 | Matrix |
| blocks.2.2.se.conv_expand.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.2.conv_pwl.weight | (56, 336, 1, 1) | (56, 336) | 18816 | Matrix |
| blocks.2.2.bn3.weight | (56,) | (56,) | 56 | Vector |
| blocks.2.2.bn3.bias | (56,) | (56,) | 56 | Vector |
| blocks.2.3.conv_pw.weight | (336, 56, 1, 1) | (336, 56) | 18816 | Matrix |
| blocks.2.3.bn1.weight | (336,) | (336,) | 336 | Vector |
| blocks.2.3.bn1.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.3.conv_dw.weight | (336, 1, 5, 5) | (336, 5, 5) | 8400 | Tensor rank 3 |
| blocks.2.3.bn2.weight | (336,) | (336,) | 336 | Vector |
| blocks.2.3.bn2.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.3.se.conv_reduce.weight | (14, 336, 1, 1) | (14, 336) | 4704 | Matrix |
| blocks.2.3.se.conv_reduce.bias | (14,) | (14,) | 14 | Vector |
| blocks.2.3.se.conv_expand.weight | (336, 14, 1, 1) | (336, 14) | 4704 | Matrix |
| blocks.2.3.se.conv_expand.bias | (336,) | (336,) | 336 | Vector |
| blocks.2.3.conv_pwl.weight | (56, 336, 1, 1) | (56, 336) | 18816 | Matrix |
| blocks.2.3.bn3.weight | (56,) | (56,) | 56 | Vector |
| blocks.2.3.bn3.bias | (56,) | (56,) | 56 | Vector |
| blocks.3.0.conv_pw.weight | (336, 56, 1, 1) | (336, 56) | 18816 | Matrix |
| blocks.3.0.bn1.weight | (336,) | (336,) | 336 | Vector |
| blocks.3.0.bn1.bias | (336,) | (336,) | 336 | Vector |
| blocks.3.0.conv_dw.weight | (336, 1, 3, 3) | (336, 3, 3) | 3024 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (336,) | (336,) | 336 | Vector |
| blocks.3.0.bn2.bias | (336,) | (336,) | 336 | Vector |
| blocks.3.0.se.conv_reduce.weight | (14, 336, 1, 1) | (14, 336) | 4704 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (14,) | (14,) | 14 | Vector |
| blocks.3.0.se.conv_expand.weight | (336, 14, 1, 1) | (336, 14) | 4704 | Matrix |
| blocks.3.0.se.conv_expand.bias | (336,) | (336,) | 336 | Vector |
| blocks.3.0.conv_pwl.weight | (112, 336, 1, 1) | (112, 336) | 37632 | Matrix |
| blocks.3.0.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.3.0.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.3.1.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.3.1.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.1.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.1.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.1.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.1.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.3.1.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.3.1.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.1.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.3.1.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.3.1.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.3.2.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.3.2.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.2.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.2.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.2.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.2.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.3.2.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.3.2.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.3.2.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.2.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.3.2.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.3.2.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.3.3.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.3.3.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.3.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.3.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.3.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.3.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.3.3.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.3.3.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.3.3.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.3.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.3.3.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.3.3.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.3.4.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.3.4.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.4.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.4.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.3.4.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.4.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.4.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.3.4.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.3.4.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.3.4.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.4.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.3.4.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.3.4.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.3.5.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.3.5.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.5.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.5.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.3.5.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.3.5.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.5.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.3.5.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.3.5.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.3.5.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.3.5.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.3.5.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.3.5.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.0.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.0.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.0.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.0.conv_dw.weight | (672, 1, 5, 5) | (672, 5, 5) | 16800 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.0.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.0.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.4.0.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.4.0.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.0.conv_pwl.weight | (160, 672, 1, 1) | (160, 672) | 107520 | Matrix |
| blocks.4.0.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.4.0.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.4.1.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.4.1.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.1.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.1.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.1.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.1.se.conv_reduce.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.1.se.conv_expand.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| blocks.4.1.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.1.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.4.1.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.4.1.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.4.2.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.4.2.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.2.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.2.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.2.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.2.se.conv_reduce.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.2.se.conv_expand.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| blocks.4.2.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.2.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.4.2.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.4.2.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.4.3.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.4.3.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.3.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.3.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.3.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.3.se.conv_reduce.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| blocks.4.3.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.3.se.conv_expand.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| blocks.4.3.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.3.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.4.3.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.4.3.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.4.4.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.4.4.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.4.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.4.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.4.4.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.4.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.4.se.conv_reduce.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| blocks.4.4.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.4.se.conv_expand.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| blocks.4.4.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.4.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.4.4.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.4.4.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.4.5.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.4.5.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.5.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.5.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.4.5.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.4.5.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.5.se.conv_reduce.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| blocks.4.5.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.4.5.se.conv_expand.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| blocks.4.5.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.4.5.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.4.5.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.4.5.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.5.0.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.5.0.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.5.0.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.0.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.5.0.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.0.se.conv_reduce.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (40,) | (40,) | 40 | Vector |
| blocks.5.0.se.conv_expand.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| blocks.5.0.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.0.conv_pwl.weight | (272, 960, 1, 1) | (272, 960) | 261120 | Matrix |
| blocks.5.0.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.0.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.1.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.1.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.1.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.1.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.1.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.1.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.1.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.1.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.1.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.1.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.1.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.1.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.2.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.2.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.2.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.2.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.2.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.2.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.2.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.2.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.2.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.2.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.2.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.2.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.3.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.3.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.3.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.3.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.3.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.3.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.3.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.3.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.3.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.3.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.3.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.3.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.4.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.4.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.4.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.4.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.4.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.4.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.4.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.4.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.4.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.4.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.4.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.4.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.5.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.5.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.5.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.5.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.5.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.5.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.5.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.5.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.5.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.5.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.5.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.5.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.5.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.6.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.6.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.6.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.6.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.6.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.6.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.6.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.6.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.6.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.6.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.6.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.6.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.6.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.5.7.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.5.7.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.7.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.7.conv_dw.weight | (1632, 1, 5, 5) | (1632, 5, 5) | 40800 | Tensor rank 3 |
| blocks.5.7.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.7.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.7.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.5.7.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.5.7.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.5.7.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.5.7.conv_pwl.weight | (272, 1632, 1, 1) | (272, 1632) | 443904 | Matrix |
| blocks.5.7.bn3.weight | (272,) | (272,) | 272 | Vector |
| blocks.5.7.bn3.bias | (272,) | (272,) | 272 | Vector |
| blocks.6.0.conv_pw.weight | (1632, 272, 1, 1) | (1632, 272) | 443904 | Matrix |
| blocks.6.0.bn1.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.6.0.bn1.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.6.0.conv_dw.weight | (1632, 1, 3, 3) | (1632, 3, 3) | 14688 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1632,) | (1632,) | 1632 | Vector |
| blocks.6.0.bn2.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.6.0.se.conv_reduce.weight | (68, 1632, 1, 1) | (68, 1632) | 110976 | Matrix |
| blocks.6.0.se.conv_reduce.bias | (68,) | (68,) | 68 | Vector |
| blocks.6.0.se.conv_expand.weight | (1632, 68, 1, 1) | (1632, 68) | 110976 | Matrix |
| blocks.6.0.se.conv_expand.bias | (1632,) | (1632,) | 1632 | Vector |
| blocks.6.0.conv_pwl.weight | (448, 1632, 1, 1) | (448, 1632) | 731136 | Matrix |
| blocks.6.0.bn3.weight | (448,) | (448,) | 448 | Vector |
| blocks.6.0.bn3.bias | (448,) | (448,) | 448 | Vector |
| blocks.6.1.conv_pw.weight | (2688, 448, 1, 1) | (2688, 448) | 1204224 | Matrix |
| blocks.6.1.bn1.weight | (2688,) | (2688,) | 2688 | Vector |
| blocks.6.1.bn1.bias | (2688,) | (2688,) | 2688 | Vector |
| blocks.6.1.conv_dw.weight | (2688, 1, 3, 3) | (2688, 3, 3) | 24192 | Tensor rank 3 |
| blocks.6.1.bn2.weight | (2688,) | (2688,) | 2688 | Vector |
| blocks.6.1.bn2.bias | (2688,) | (2688,) | 2688 | Vector |
| blocks.6.1.se.conv_reduce.weight | (112, 2688, 1, 1) | (112, 2688) | 301056 | Matrix |
| blocks.6.1.se.conv_reduce.bias | (112,) | (112,) | 112 | Vector |
| blocks.6.1.se.conv_expand.weight | (2688, 112, 1, 1) | (2688, 112) | 301056 | Matrix |
| blocks.6.1.se.conv_expand.bias | (2688,) | (2688,) | 2688 | Vector |
| blocks.6.1.conv_pwl.weight | (448, 2688, 1, 1) | (448, 2688) | 1204224 | Matrix |
| blocks.6.1.bn3.weight | (448,) | (448,) | 448 | Vector |
| blocks.6.1.bn3.bias | (448,) | (448,) | 448 | Vector |
| conv_head.weight | (1792, 448, 1, 1) | (1792, 448) | 802816 | Matrix |
| bn2.weight | (1792,) | (1792,) | 1792 | Vector |
| bn2.bias | (1792,) | (1792,) | 1792 | Vector |
| classifier.weight | (1000, 1792) | (1000, 1792) | 1792000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

