# efficientnet_b3 parameter information

**Number of layers: [ 340 ]**

**Number of parameters: [ 46.666 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 46.666 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.47 | 30.59 | 7.65 | 0.29 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.89 | 96.07 | 3.04 | 0.01 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (40, 3, 3, 3) | (40, 3, 3, 3) | 1080 | Tensor rank 4 |
| bn1.weight | (40,) | (40,) | 40 | Vector |
| bn1.bias | (40,) | (40,) | 40 | Vector |
| blocks.0.0.conv_dw.weight | (40, 1, 3, 3) | (40, 3, 3) | 360 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (40,) | (40,) | 40 | Vector |
| blocks.0.0.bn1.bias | (40,) | (40,) | 40 | Vector |
| blocks.0.0.se.conv_reduce.weight | (10, 40, 1, 1) | (10, 40) | 400 | Matrix |
| blocks.0.0.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.0.0.se.conv_expand.weight | (40, 10, 1, 1) | (40, 10) | 400 | Matrix |
| blocks.0.0.se.conv_expand.bias | (40,) | (40,) | 40 | Vector |
| blocks.0.0.conv_pw.weight | (24, 40, 1, 1) | (24, 40) | 960 | Matrix |
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
| blocks.2.0.conv_pwl.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.0.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.0.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.1.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.2.1.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.1.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.1.conv_dw.weight | (288, 1, 5, 5) | (288, 5, 5) | 7200 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.1.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.1.se.conv_reduce.weight | (12, 288, 1, 1) | (12, 288) | 3456 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (12,) | (12,) | 12 | Vector |
| blocks.2.1.se.conv_expand.weight | (288, 12, 1, 1) | (288, 12) | 3456 | Matrix |
| blocks.2.1.se.conv_expand.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.1.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.2.1.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.1.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.2.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.2.2.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.2.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.2.conv_dw.weight | (288, 1, 5, 5) | (288, 5, 5) | 7200 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.2.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.2.se.conv_reduce.weight | (12, 288, 1, 1) | (12, 288) | 3456 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (12,) | (12,) | 12 | Vector |
| blocks.2.2.se.conv_expand.weight | (288, 12, 1, 1) | (288, 12) | 3456 | Matrix |
| blocks.2.2.se.conv_expand.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.2.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.2.2.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.2.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.3.0.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.3.0.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.3.0.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.3.0.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.3.0.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.3.0.se.conv_reduce.weight | (12, 288, 1, 1) | (12, 288) | 3456 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (12,) | (12,) | 12 | Vector |
| blocks.3.0.se.conv_expand.weight | (288, 12, 1, 1) | (288, 12) | 3456 | Matrix |
| blocks.3.0.se.conv_expand.bias | (288,) | (288,) | 288 | Vector |
| blocks.3.0.conv_pwl.weight | (96, 288, 1, 1) | (96, 288) | 27648 | Matrix |
| blocks.3.0.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.0.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.1.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.3.1.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.1.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.1.conv_dw.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.1.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.1.se.conv_reduce.weight | (24, 576, 1, 1) | (24, 576) | 13824 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.1.se.conv_expand.weight | (576, 24, 1, 1) | (576, 24) | 13824 | Matrix |
| blocks.3.1.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.1.conv_pwl.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| blocks.3.1.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.1.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.2.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.3.2.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.2.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.2.conv_dw.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.2.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.2.se.conv_reduce.weight | (24, 576, 1, 1) | (24, 576) | 13824 | Matrix |
| blocks.3.2.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.2.se.conv_expand.weight | (576, 24, 1, 1) | (576, 24) | 13824 | Matrix |
| blocks.3.2.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.2.conv_pwl.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| blocks.3.2.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.2.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.3.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.3.3.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.3.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.3.conv_dw.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.3.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.3.se.conv_reduce.weight | (24, 576, 1, 1) | (24, 576) | 13824 | Matrix |
| blocks.3.3.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.3.se.conv_expand.weight | (576, 24, 1, 1) | (576, 24) | 13824 | Matrix |
| blocks.3.3.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.3.conv_pwl.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| blocks.3.3.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.3.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.3.4.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.3.4.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.4.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.4.conv_dw.weight | (576, 1, 3, 3) | (576, 3, 3) | 5184 | Tensor rank 3 |
| blocks.3.4.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.3.4.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.4.se.conv_reduce.weight | (24, 576, 1, 1) | (24, 576) | 13824 | Matrix |
| blocks.3.4.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.3.4.se.conv_expand.weight | (576, 24, 1, 1) | (576, 24) | 13824 | Matrix |
| blocks.3.4.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.3.4.conv_pwl.weight | (96, 576, 1, 1) | (96, 576) | 55296 | Matrix |
| blocks.3.4.bn3.weight | (96,) | (96,) | 96 | Vector |
| blocks.3.4.bn3.bias | (96,) | (96,) | 96 | Vector |
| blocks.4.0.conv_pw.weight | (576, 96, 1, 1) | (576, 96) | 55296 | Matrix |
| blocks.4.0.bn1.weight | (576,) | (576,) | 576 | Vector |
| blocks.4.0.bn1.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.0.conv_dw.weight | (576, 1, 5, 5) | (576, 5, 5) | 14400 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (576,) | (576,) | 576 | Vector |
| blocks.4.0.bn2.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.0.se.conv_reduce.weight | (24, 576, 1, 1) | (24, 576) | 13824 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.4.0.se.conv_expand.weight | (576, 24, 1, 1) | (576, 24) | 13824 | Matrix |
| blocks.4.0.se.conv_expand.bias | (576,) | (576,) | 576 | Vector |
| blocks.4.0.conv_pwl.weight | (136, 576, 1, 1) | (136, 576) | 78336 | Matrix |
| blocks.4.0.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.0.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.4.1.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.4.1.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.1.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.1.conv_dw.weight | (816, 1, 5, 5) | (816, 5, 5) | 20400 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.1.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.1.se.conv_reduce.weight | (34, 816, 1, 1) | (34, 816) | 27744 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (34,) | (34,) | 34 | Vector |
| blocks.4.1.se.conv_expand.weight | (816, 34, 1, 1) | (816, 34) | 27744 | Matrix |
| blocks.4.1.se.conv_expand.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.1.conv_pwl.weight | (136, 816, 1, 1) | (136, 816) | 110976 | Matrix |
| blocks.4.1.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.1.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.4.2.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.4.2.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.2.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.2.conv_dw.weight | (816, 1, 5, 5) | (816, 5, 5) | 20400 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.2.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.2.se.conv_reduce.weight | (34, 816, 1, 1) | (34, 816) | 27744 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (34,) | (34,) | 34 | Vector |
| blocks.4.2.se.conv_expand.weight | (816, 34, 1, 1) | (816, 34) | 27744 | Matrix |
| blocks.4.2.se.conv_expand.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.2.conv_pwl.weight | (136, 816, 1, 1) | (136, 816) | 110976 | Matrix |
| blocks.4.2.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.2.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.4.3.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.4.3.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.3.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.3.conv_dw.weight | (816, 1, 5, 5) | (816, 5, 5) | 20400 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.3.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.3.se.conv_reduce.weight | (34, 816, 1, 1) | (34, 816) | 27744 | Matrix |
| blocks.4.3.se.conv_reduce.bias | (34,) | (34,) | 34 | Vector |
| blocks.4.3.se.conv_expand.weight | (816, 34, 1, 1) | (816, 34) | 27744 | Matrix |
| blocks.4.3.se.conv_expand.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.3.conv_pwl.weight | (136, 816, 1, 1) | (136, 816) | 110976 | Matrix |
| blocks.4.3.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.3.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.4.4.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.4.4.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.4.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.4.conv_dw.weight | (816, 1, 5, 5) | (816, 5, 5) | 20400 | Tensor rank 3 |
| blocks.4.4.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.4.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.4.se.conv_reduce.weight | (34, 816, 1, 1) | (34, 816) | 27744 | Matrix |
| blocks.4.4.se.conv_reduce.bias | (34,) | (34,) | 34 | Vector |
| blocks.4.4.se.conv_expand.weight | (816, 34, 1, 1) | (816, 34) | 27744 | Matrix |
| blocks.4.4.se.conv_expand.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.4.conv_pwl.weight | (136, 816, 1, 1) | (136, 816) | 110976 | Matrix |
| blocks.4.4.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.4.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.5.0.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.5.0.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.5.0.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.5.0.conv_dw.weight | (816, 1, 5, 5) | (816, 5, 5) | 20400 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.5.0.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.5.0.se.conv_reduce.weight | (34, 816, 1, 1) | (34, 816) | 27744 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (34,) | (34,) | 34 | Vector |
| blocks.5.0.se.conv_expand.weight | (816, 34, 1, 1) | (816, 34) | 27744 | Matrix |
| blocks.5.0.se.conv_expand.bias | (816,) | (816,) | 816 | Vector |
| blocks.5.0.conv_pwl.weight | (232, 816, 1, 1) | (232, 816) | 189312 | Matrix |
| blocks.5.0.bn3.weight | (232,) | (232,) | 232 | Vector |
| blocks.5.0.bn3.bias | (232,) | (232,) | 232 | Vector |
| blocks.5.1.conv_pw.weight | (1392, 232, 1, 1) | (1392, 232) | 322944 | Matrix |
| blocks.5.1.bn1.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.1.bn1.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.1.conv_dw.weight | (1392, 1, 5, 5) | (1392, 5, 5) | 34800 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.1.bn2.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.1.se.conv_reduce.weight | (58, 1392, 1, 1) | (58, 1392) | 80736 | Matrix |
| blocks.5.1.se.conv_reduce.bias | (58,) | (58,) | 58 | Vector |
| blocks.5.1.se.conv_expand.weight | (1392, 58, 1, 1) | (1392, 58) | 80736 | Matrix |
| blocks.5.1.se.conv_expand.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.1.conv_pwl.weight | (232, 1392, 1, 1) | (232, 1392) | 322944 | Matrix |
| blocks.5.1.bn3.weight | (232,) | (232,) | 232 | Vector |
| blocks.5.1.bn3.bias | (232,) | (232,) | 232 | Vector |
| blocks.5.2.conv_pw.weight | (1392, 232, 1, 1) | (1392, 232) | 322944 | Matrix |
| blocks.5.2.bn1.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.2.bn1.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.2.conv_dw.weight | (1392, 1, 5, 5) | (1392, 5, 5) | 34800 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.2.bn2.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.2.se.conv_reduce.weight | (58, 1392, 1, 1) | (58, 1392) | 80736 | Matrix |
| blocks.5.2.se.conv_reduce.bias | (58,) | (58,) | 58 | Vector |
| blocks.5.2.se.conv_expand.weight | (1392, 58, 1, 1) | (1392, 58) | 80736 | Matrix |
| blocks.5.2.se.conv_expand.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.2.conv_pwl.weight | (232, 1392, 1, 1) | (232, 1392) | 322944 | Matrix |
| blocks.5.2.bn3.weight | (232,) | (232,) | 232 | Vector |
| blocks.5.2.bn3.bias | (232,) | (232,) | 232 | Vector |
| blocks.5.3.conv_pw.weight | (1392, 232, 1, 1) | (1392, 232) | 322944 | Matrix |
| blocks.5.3.bn1.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.3.bn1.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.3.conv_dw.weight | (1392, 1, 5, 5) | (1392, 5, 5) | 34800 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.3.bn2.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.3.se.conv_reduce.weight | (58, 1392, 1, 1) | (58, 1392) | 80736 | Matrix |
| blocks.5.3.se.conv_reduce.bias | (58,) | (58,) | 58 | Vector |
| blocks.5.3.se.conv_expand.weight | (1392, 58, 1, 1) | (1392, 58) | 80736 | Matrix |
| blocks.5.3.se.conv_expand.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.3.conv_pwl.weight | (232, 1392, 1, 1) | (232, 1392) | 322944 | Matrix |
| blocks.5.3.bn3.weight | (232,) | (232,) | 232 | Vector |
| blocks.5.3.bn3.bias | (232,) | (232,) | 232 | Vector |
| blocks.5.4.conv_pw.weight | (1392, 232, 1, 1) | (1392, 232) | 322944 | Matrix |
| blocks.5.4.bn1.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.4.bn1.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.4.conv_dw.weight | (1392, 1, 5, 5) | (1392, 5, 5) | 34800 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.4.bn2.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.4.se.conv_reduce.weight | (58, 1392, 1, 1) | (58, 1392) | 80736 | Matrix |
| blocks.5.4.se.conv_reduce.bias | (58,) | (58,) | 58 | Vector |
| blocks.5.4.se.conv_expand.weight | (1392, 58, 1, 1) | (1392, 58) | 80736 | Matrix |
| blocks.5.4.se.conv_expand.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.4.conv_pwl.weight | (232, 1392, 1, 1) | (232, 1392) | 322944 | Matrix |
| blocks.5.4.bn3.weight | (232,) | (232,) | 232 | Vector |
| blocks.5.4.bn3.bias | (232,) | (232,) | 232 | Vector |
| blocks.5.5.conv_pw.weight | (1392, 232, 1, 1) | (1392, 232) | 322944 | Matrix |
| blocks.5.5.bn1.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.5.bn1.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.5.conv_dw.weight | (1392, 1, 5, 5) | (1392, 5, 5) | 34800 | Tensor rank 3 |
| blocks.5.5.bn2.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.5.bn2.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.5.se.conv_reduce.weight | (58, 1392, 1, 1) | (58, 1392) | 80736 | Matrix |
| blocks.5.5.se.conv_reduce.bias | (58,) | (58,) | 58 | Vector |
| blocks.5.5.se.conv_expand.weight | (1392, 58, 1, 1) | (1392, 58) | 80736 | Matrix |
| blocks.5.5.se.conv_expand.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.5.5.conv_pwl.weight | (232, 1392, 1, 1) | (232, 1392) | 322944 | Matrix |
| blocks.5.5.bn3.weight | (232,) | (232,) | 232 | Vector |
| blocks.5.5.bn3.bias | (232,) | (232,) | 232 | Vector |
| blocks.6.0.conv_pw.weight | (1392, 232, 1, 1) | (1392, 232) | 322944 | Matrix |
| blocks.6.0.bn1.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.6.0.bn1.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.6.0.conv_dw.weight | (1392, 1, 3, 3) | (1392, 3, 3) | 12528 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1392,) | (1392,) | 1392 | Vector |
| blocks.6.0.bn2.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.6.0.se.conv_reduce.weight | (58, 1392, 1, 1) | (58, 1392) | 80736 | Matrix |
| blocks.6.0.se.conv_reduce.bias | (58,) | (58,) | 58 | Vector |
| blocks.6.0.se.conv_expand.weight | (1392, 58, 1, 1) | (1392, 58) | 80736 | Matrix |
| blocks.6.0.se.conv_expand.bias | (1392,) | (1392,) | 1392 | Vector |
| blocks.6.0.conv_pwl.weight | (384, 1392, 1, 1) | (384, 1392) | 534528 | Matrix |
| blocks.6.0.bn3.weight | (384,) | (384,) | 384 | Vector |
| blocks.6.0.bn3.bias | (384,) | (384,) | 384 | Vector |
| blocks.6.1.conv_pw.weight | (2304, 384, 1, 1) | (2304, 384) | 884736 | Matrix |
| blocks.6.1.bn1.weight | (2304,) | (2304,) | 2304 | Vector |
| blocks.6.1.bn1.bias | (2304,) | (2304,) | 2304 | Vector |
| blocks.6.1.conv_dw.weight | (2304, 1, 3, 3) | (2304, 3, 3) | 20736 | Tensor rank 3 |
| blocks.6.1.bn2.weight | (2304,) | (2304,) | 2304 | Vector |
| blocks.6.1.bn2.bias | (2304,) | (2304,) | 2304 | Vector |
| blocks.6.1.se.conv_reduce.weight | (96, 2304, 1, 1) | (96, 2304) | 221184 | Matrix |
| blocks.6.1.se.conv_reduce.bias | (96,) | (96,) | 96 | Vector |
| blocks.6.1.se.conv_expand.weight | (2304, 96, 1, 1) | (2304, 96) | 221184 | Matrix |
| blocks.6.1.se.conv_expand.bias | (2304,) | (2304,) | 2304 | Vector |
| blocks.6.1.conv_pwl.weight | (384, 2304, 1, 1) | (384, 2304) | 884736 | Matrix |
| blocks.6.1.bn3.weight | (384,) | (384,) | 384 | Vector |
| blocks.6.1.bn3.bias | (384,) | (384,) | 384 | Vector |
| conv_head.weight | (1536, 384, 1, 1) | (1536, 384) | 589824 | Matrix |
| bn2.weight | (1536,) | (1536,) | 1536 | Vector |
| bn2.bias | (1536,) | (1536,) | 1536 | Vector |
| classifier.weight | (1000, 1536) | (1000, 1536) | 1536000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

