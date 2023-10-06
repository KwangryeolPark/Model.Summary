# efficientnetv2_rw_t parameter information

**Number of layers: [ 439 ]**

**Number of parameters: [ 52.068 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 52.068 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 62.19 | 28.70 | 6.61 | 2.51 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 1.08 | 93.46 | 1.72 | 3.74 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (24, 3, 3, 3) | (24, 3, 3, 3) | 648 | Tensor rank 4 |
| bn1.weight | (24,) | (24,) | 24 | Vector |
| bn1.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.0.conv.weight | (24, 24, 3, 3) | (24, 24, 3, 3) | 5184 | Tensor rank 4 |
| blocks.0.0.bn1.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.0.bn1.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.1.conv.weight | (24, 24, 3, 3) | (24, 24, 3, 3) | 5184 | Tensor rank 4 |
| blocks.0.1.bn1.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.1.bn1.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.0.conv_exp.weight | (96, 24, 3, 3) | (96, 24, 3, 3) | 20736 | Tensor rank 4 |
| blocks.1.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.0.conv_pwl.weight | (40, 96, 1, 1) | (40, 96) | 3840 | Matrix |
| blocks.1.0.bn2.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.0.bn2.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.1.conv_exp.weight | (160, 40, 3, 3) | (160, 40, 3, 3) | 57600 | Tensor rank 4 |
| blocks.1.1.bn1.weight | (160,) | (160,) | 160 | Vector |
| blocks.1.1.bn1.bias | (160,) | (160,) | 160 | Vector |
| blocks.1.1.conv_pwl.weight | (40, 160, 1, 1) | (40, 160) | 6400 | Matrix |
| blocks.1.1.bn2.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.1.bn2.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.2.conv_exp.weight | (160, 40, 3, 3) | (160, 40, 3, 3) | 57600 | Tensor rank 4 |
| blocks.1.2.bn1.weight | (160,) | (160,) | 160 | Vector |
| blocks.1.2.bn1.bias | (160,) | (160,) | 160 | Vector |
| blocks.1.2.conv_pwl.weight | (40, 160, 1, 1) | (40, 160) | 6400 | Matrix |
| blocks.1.2.bn2.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.2.bn2.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.3.conv_exp.weight | (160, 40, 3, 3) | (160, 40, 3, 3) | 57600 | Tensor rank 4 |
| blocks.1.3.bn1.weight | (160,) | (160,) | 160 | Vector |
| blocks.1.3.bn1.bias | (160,) | (160,) | 160 | Vector |
| blocks.1.3.conv_pwl.weight | (40, 160, 1, 1) | (40, 160) | 6400 | Matrix |
| blocks.1.3.bn2.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.3.bn2.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.0.conv_exp.weight | (160, 40, 3, 3) | (160, 40, 3, 3) | 57600 | Tensor rank 4 |
| blocks.2.0.bn1.weight | (160,) | (160,) | 160 | Vector |
| blocks.2.0.bn1.bias | (160,) | (160,) | 160 | Vector |
| blocks.2.0.conv_pwl.weight | (48, 160, 1, 1) | (48, 160) | 7680 | Matrix |
| blocks.2.0.bn2.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.0.bn2.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.1.conv_exp.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| blocks.2.1.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.1.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.1.conv_pwl.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.1.bn2.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.1.bn2.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.2.conv_exp.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| blocks.2.2.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.2.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.2.conv_pwl.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.2.bn2.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.2.bn2.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.3.conv_exp.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| blocks.2.3.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.3.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.3.conv_pwl.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.3.bn2.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.3.bn2.bias | (48,) | (48,) | 48 | Vector |
| blocks.3.0.conv_pw.weight | (192, 48, 1, 1) | (192, 48) | 9216 | Matrix |
| blocks.3.0.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.0.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.0.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.0.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.0.se.conv_reduce.weight | (12, 192, 1, 1) | (12, 192) | 2304 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (12,) | (12,) | 12 | Vector |
| blocks.3.0.se.conv_expand.weight | (192, 12, 1, 1) | (192, 12) | 2304 | Matrix |
| blocks.3.0.se.conv_expand.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.0.conv_pwl.weight | (104, 192, 1, 1) | (104, 192) | 19968 | Matrix |
| blocks.3.0.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.3.0.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.3.1.conv_pw.weight | (416, 104, 1, 1) | (416, 104) | 43264 | Matrix |
| blocks.3.1.bn1.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.1.bn1.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.1.conv_dw.weight | (416, 1, 3, 3) | (416, 3, 3) | 3744 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.1.bn2.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.1.se.conv_reduce.weight | (26, 416, 1, 1) | (26, 416) | 10816 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (26,) | (26,) | 26 | Vector |
| blocks.3.1.se.conv_expand.weight | (416, 26, 1, 1) | (416, 26) | 10816 | Matrix |
| blocks.3.1.se.conv_expand.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.1.conv_pwl.weight | (104, 416, 1, 1) | (104, 416) | 43264 | Matrix |
| blocks.3.1.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.3.1.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.3.2.conv_pw.weight | (416, 104, 1, 1) | (416, 104) | 43264 | Matrix |
| blocks.3.2.bn1.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.2.bn1.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.2.conv_dw.weight | (416, 1, 3, 3) | (416, 3, 3) | 3744 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.2.bn2.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.2.se.conv_reduce.weight | (26, 416, 1, 1) | (26, 416) | 10816 | Matrix |
| blocks.3.2.se.conv_reduce.bias | (26,) | (26,) | 26 | Vector |
| blocks.3.2.se.conv_expand.weight | (416, 26, 1, 1) | (416, 26) | 10816 | Matrix |
| blocks.3.2.se.conv_expand.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.2.conv_pwl.weight | (104, 416, 1, 1) | (104, 416) | 43264 | Matrix |
| blocks.3.2.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.3.2.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.3.3.conv_pw.weight | (416, 104, 1, 1) | (416, 104) | 43264 | Matrix |
| blocks.3.3.bn1.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.3.bn1.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.3.conv_dw.weight | (416, 1, 3, 3) | (416, 3, 3) | 3744 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.3.bn2.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.3.se.conv_reduce.weight | (26, 416, 1, 1) | (26, 416) | 10816 | Matrix |
| blocks.3.3.se.conv_reduce.bias | (26,) | (26,) | 26 | Vector |
| blocks.3.3.se.conv_expand.weight | (416, 26, 1, 1) | (416, 26) | 10816 | Matrix |
| blocks.3.3.se.conv_expand.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.3.conv_pwl.weight | (104, 416, 1, 1) | (104, 416) | 43264 | Matrix |
| blocks.3.3.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.3.3.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.3.4.conv_pw.weight | (416, 104, 1, 1) | (416, 104) | 43264 | Matrix |
| blocks.3.4.bn1.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.4.bn1.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.4.conv_dw.weight | (416, 1, 3, 3) | (416, 3, 3) | 3744 | Tensor rank 3 |
| blocks.3.4.bn2.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.4.bn2.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.4.se.conv_reduce.weight | (26, 416, 1, 1) | (26, 416) | 10816 | Matrix |
| blocks.3.4.se.conv_reduce.bias | (26,) | (26,) | 26 | Vector |
| blocks.3.4.se.conv_expand.weight | (416, 26, 1, 1) | (416, 26) | 10816 | Matrix |
| blocks.3.4.se.conv_expand.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.4.conv_pwl.weight | (104, 416, 1, 1) | (104, 416) | 43264 | Matrix |
| blocks.3.4.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.3.4.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.3.5.conv_pw.weight | (416, 104, 1, 1) | (416, 104) | 43264 | Matrix |
| blocks.3.5.bn1.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.5.bn1.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.5.conv_dw.weight | (416, 1, 3, 3) | (416, 3, 3) | 3744 | Tensor rank 3 |
| blocks.3.5.bn2.weight | (416,) | (416,) | 416 | Vector |
| blocks.3.5.bn2.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.5.se.conv_reduce.weight | (26, 416, 1, 1) | (26, 416) | 10816 | Matrix |
| blocks.3.5.se.conv_reduce.bias | (26,) | (26,) | 26 | Vector |
| blocks.3.5.se.conv_expand.weight | (416, 26, 1, 1) | (416, 26) | 10816 | Matrix |
| blocks.3.5.se.conv_expand.bias | (416,) | (416,) | 416 | Vector |
| blocks.3.5.conv_pwl.weight | (104, 416, 1, 1) | (104, 416) | 43264 | Matrix |
| blocks.3.5.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.3.5.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.4.0.conv_pw.weight | (624, 104, 1, 1) | (624, 104) | 64896 | Matrix |
| blocks.4.0.bn1.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.0.bn1.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.0.conv_dw.weight | (624, 1, 3, 3) | (624, 3, 3) | 5616 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.0.bn2.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.0.se.conv_reduce.weight | (26, 624, 1, 1) | (26, 624) | 16224 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (26,) | (26,) | 26 | Vector |
| blocks.4.0.se.conv_expand.weight | (624, 26, 1, 1) | (624, 26) | 16224 | Matrix |
| blocks.4.0.se.conv_expand.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.0.conv_pwl.weight | (128, 624, 1, 1) | (128, 624) | 79872 | Matrix |
| blocks.4.0.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.0.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.1.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.1.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.1.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.1.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.1.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.1.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.1.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.1.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.1.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.1.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.1.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.2.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.2.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.2.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.2.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.2.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.2.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.2.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.2.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.2.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.2.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.2.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.3.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.3.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.3.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.3.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.3.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.3.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.3.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.3.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.3.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.3.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.3.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.3.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.4.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.4.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.4.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.4.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.4.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.4.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.4.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.4.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.4.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.4.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.4.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.4.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.4.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.5.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.5.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.5.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.5.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.5.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.5.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.5.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.5.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.5.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.5.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.5.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.5.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.5.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.6.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.6.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.6.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.6.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.6.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.6.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.6.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.6.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.6.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.6.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.6.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.6.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.6.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.7.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.7.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.7.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.7.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.7.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.7.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.7.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.7.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.7.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.7.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.7.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.7.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.7.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.8.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.8.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.8.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.8.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.4.8.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.8.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.8.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.8.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.8.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.8.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.8.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.4.8.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.4.8.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.5.0.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.5.0.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.5.0.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.5.0.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.5.0.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.5.0.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.5.0.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.5.0.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.5.0.conv_pwl.weight | (208, 768, 1, 1) | (208, 768) | 159744 | Matrix |
| blocks.5.0.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.0.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.1.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.1.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.1.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.1.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.1.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.1.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.1.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.2.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.2.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.2.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.2.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.2.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.2.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.2.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.2.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.2.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.2.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.2.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.2.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.3.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.3.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.3.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.3.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.3.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.3.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.3.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.3.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.3.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.3.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.3.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.3.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.4.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.4.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.4.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.4.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.4.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.4.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.4.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.5.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.5.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.5.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.5.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.5.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.5.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.5.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.5.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.5.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.5.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.5.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.5.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.5.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.6.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.6.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.6.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.6.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.6.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.6.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.6.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.6.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.6.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.6.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.6.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.6.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.6.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.7.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.7.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.7.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.7.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.7.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.7.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.7.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.7.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.7.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.7.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.7.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.7.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.7.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.8.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.8.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.8.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.8.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.8.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.8.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.8.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.8.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.8.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.8.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.8.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.8.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.8.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.9.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.9.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.9.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.9.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.9.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.9.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.9.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.9.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.9.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.9.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.9.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.9.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.9.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.10.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.10.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.10.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.10.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.10.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.10.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.10.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.10.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.10.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.10.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.10.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.10.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.10.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.11.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.11.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.11.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.11.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.11.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.11.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.11.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.11.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.11.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.11.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.11.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.11.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.11.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.12.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.12.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.12.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.12.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.12.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.12.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.12.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.12.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.12.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.12.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.12.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.12.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.12.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.13.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.13.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.13.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.13.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.5.13.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.13.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.13.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.13.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.13.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.13.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.13.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.13.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.13.bn3.bias | (208,) | (208,) | 208 | Vector |
| conv_head.weight | (1024, 208, 1, 1) | (1024, 208) | 212992 | Matrix |
| bn2.weight | (1024,) | (1024,) | 1024 | Vector |
| bn2.bias | (1024,) | (1024,) | 1024 | Vector |
| classifier.weight | (1000, 1024) | (1000, 1024) | 1024000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

