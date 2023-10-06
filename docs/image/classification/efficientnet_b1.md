# efficientnet_b1 parameter information

**Number of layers: [ 301 ]**

**Number of parameters: [ 29.732 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 29.732 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.46 | 30.56 | 7.64 | 0.33 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.99 | 95.71 | 3.29 | 0.01 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (32, 3, 3, 3) | (32, 3, 3, 3) | 864 | Tensor rank 4 |
| bn1.weight | (32,) | (32,) | 32 | Vector |
| bn1.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.conv_dw.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (32,) | (32,) | 32 | Vector |
| blocks.0.0.bn1.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.se.conv_reduce.weight | (8, 32, 1, 1) | (8, 32) | 256 | Matrix |
| blocks.0.0.se.conv_reduce.bias | (8,) | (8,) | 8 | Vector |
| blocks.0.0.se.conv_expand.weight | (32, 8, 1, 1) | (32, 8) | 256 | Matrix |
| blocks.0.0.se.conv_expand.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.conv_pw.weight | (16, 32, 1, 1) | (16, 32) | 512 | Matrix |
| blocks.0.0.bn2.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn2.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.1.conv_dw.weight | (16, 1, 3, 3) | (16, 3, 3) | 144 | Tensor rank 3 |
| blocks.0.1.bn1.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.1.bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.1.se.conv_reduce.weight | (4, 16, 1, 1) | (4, 16) | 64 | Matrix |
| blocks.0.1.se.conv_reduce.bias | (4,) | (4,) | 4 | Vector |
| blocks.0.1.se.conv_expand.weight | (16, 4, 1, 1) | (16, 4) | 64 | Matrix |
| blocks.0.1.se.conv_expand.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.1.conv_pw.weight | (16, 16, 1, 1) | (16, 16) | 256 | Matrix |
| blocks.0.1.bn2.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.1.bn2.bias | (16,) | (16,) | 16 | Vector |
| blocks.1.0.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.1.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.0.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.0.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.0.se.conv_reduce.weight | (4, 96, 1, 1) | (4, 96) | 384 | Matrix |
| blocks.1.0.se.conv_reduce.bias | (4,) | (4,) | 4 | Vector |
| blocks.1.0.se.conv_expand.weight | (96, 4, 1, 1) | (96, 4) | 384 | Matrix |
| blocks.1.0.se.conv_expand.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.0.conv_pwl.weight | (24, 96, 1, 1) | (24, 96) | 2304 | Matrix |
| blocks.1.0.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.0.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.1.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.1.1.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.1.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.1.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.1.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.1.se.conv_reduce.weight | (6, 144, 1, 1) | (6, 144) | 864 | Matrix |
| blocks.1.1.se.conv_reduce.bias | (6,) | (6,) | 6 | Vector |
| blocks.1.1.se.conv_expand.weight | (144, 6, 1, 1) | (144, 6) | 864 | Matrix |
| blocks.1.1.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.1.conv_pwl.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| blocks.1.1.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.1.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.2.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.1.2.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.2.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.2.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.1.2.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.2.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.2.se.conv_reduce.weight | (6, 144, 1, 1) | (6, 144) | 864 | Matrix |
| blocks.1.2.se.conv_reduce.bias | (6,) | (6,) | 6 | Vector |
| blocks.1.2.se.conv_expand.weight | (144, 6, 1, 1) | (144, 6) | 864 | Matrix |
| blocks.1.2.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.2.conv_pwl.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| blocks.1.2.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.2.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.0.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.2.0.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.0.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.0.conv_dw.weight | (144, 1, 5, 5) | (144, 5, 5) | 3600 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.0.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.0.se.conv_reduce.weight | (6, 144, 1, 1) | (6, 144) | 864 | Matrix |
| blocks.2.0.se.conv_reduce.bias | (6,) | (6,) | 6 | Vector |
| blocks.2.0.se.conv_expand.weight | (144, 6, 1, 1) | (144, 6) | 864 | Matrix |
| blocks.2.0.se.conv_expand.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.0.conv_pwl.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| blocks.2.0.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.0.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.1.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.1.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.1.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.conv_dw.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.1.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.2.1.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
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
| blocks.2.2.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.2.2.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.2.2.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.2.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.2.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.2.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.3.0.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.3.0.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.3.0.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.3.0.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.3.0.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.3.0.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.conv_pwl.weight | (80, 240, 1, 1) | (80, 240) | 19200 | Matrix |
| blocks.3.0.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.0.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.1.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.1.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.1.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.1.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.1.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.1.se.conv_reduce.weight | (20, 480, 1, 1) | (20, 480) | 9600 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (20,) | (20,) | 20 | Vector |
| blocks.3.1.se.conv_expand.weight | (480, 20, 1, 1) | (480, 20) | 9600 | Matrix |
| blocks.3.1.se.conv_expand.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.1.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.1.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.1.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.2.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.2.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.2.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.2.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.2.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.2.se.conv_reduce.weight | (20, 480, 1, 1) | (20, 480) | 9600 | Matrix |
| blocks.3.2.se.conv_reduce.bias | (20,) | (20,) | 20 | Vector |
| blocks.3.2.se.conv_expand.weight | (480, 20, 1, 1) | (480, 20) | 9600 | Matrix |
| blocks.3.2.se.conv_expand.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.2.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.2.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.2.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.3.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.3.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.3.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.3.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.3.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.3.se.conv_reduce.weight | (20, 480, 1, 1) | (20, 480) | 9600 | Matrix |
| blocks.3.3.se.conv_reduce.bias | (20,) | (20,) | 20 | Vector |
| blocks.3.3.se.conv_expand.weight | (480, 20, 1, 1) | (480, 20) | 9600 | Matrix |
| blocks.3.3.se.conv_expand.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.3.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.3.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.3.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.4.0.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.4.0.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.4.0.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.conv_dw.weight | (480, 1, 5, 5) | (480, 5, 5) | 12000 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.4.0.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.se.conv_reduce.weight | (20, 480, 1, 1) | (20, 480) | 9600 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (20,) | (20,) | 20 | Vector |
| blocks.4.0.se.conv_expand.weight | (480, 20, 1, 1) | (480, 20) | 9600 | Matrix |
| blocks.4.0.se.conv_expand.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.conv_pwl.weight | (112, 480, 1, 1) | (112, 480) | 53760 | Matrix |
| blocks.4.0.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.0.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.1.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.1.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.1.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.conv_dw.weight | (672, 1, 5, 5) | (672, 5, 5) | 16800 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.1.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.4.1.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.4.1.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.1.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.1.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.2.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.2.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.2.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.2.conv_dw.weight | (672, 1, 5, 5) | (672, 5, 5) | 16800 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.2.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.2.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.4.2.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.4.2.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.2.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.2.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.2.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.3.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.3.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.3.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.3.conv_dw.weight | (672, 1, 5, 5) | (672, 5, 5) | 16800 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.3.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.3.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.4.3.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.4.3.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.4.3.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.3.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.3.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.3.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.5.0.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.5.0.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.5.0.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.conv_dw.weight | (672, 1, 5, 5) | (672, 5, 5) | 16800 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.5.0.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.se.conv_reduce.weight | (28, 672, 1, 1) | (28, 672) | 18816 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (28,) | (28,) | 28 | Vector |
| blocks.5.0.se.conv_expand.weight | (672, 28, 1, 1) | (672, 28) | 18816 | Matrix |
| blocks.5.0.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.conv_pwl.weight | (192, 672, 1, 1) | (192, 672) | 129024 | Matrix |
| blocks.5.0.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.0.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.1.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.1.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.conv_dw.weight | (1152, 1, 5, 5) | (1152, 5, 5) | 28800 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.se.conv_reduce.weight | (48, 1152, 1, 1) | (48, 1152) | 55296 | Matrix |
| blocks.5.1.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.5.1.se.conv_expand.weight | (1152, 48, 1, 1) | (1152, 48) | 55296 | Matrix |
| blocks.5.1.se.conv_expand.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.1.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.1.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.2.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.2.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.conv_dw.weight | (1152, 1, 5, 5) | (1152, 5, 5) | 28800 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.se.conv_reduce.weight | (48, 1152, 1, 1) | (48, 1152) | 55296 | Matrix |
| blocks.5.2.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.5.2.se.conv_expand.weight | (1152, 48, 1, 1) | (1152, 48) | 55296 | Matrix |
| blocks.5.2.se.conv_expand.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.2.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.2.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.3.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.3.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.conv_dw.weight | (1152, 1, 5, 5) | (1152, 5, 5) | 28800 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.se.conv_reduce.weight | (48, 1152, 1, 1) | (48, 1152) | 55296 | Matrix |
| blocks.5.3.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.5.3.se.conv_expand.weight | (1152, 48, 1, 1) | (1152, 48) | 55296 | Matrix |
| blocks.5.3.se.conv_expand.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.3.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.3.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.4.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.4.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.conv_dw.weight | (1152, 1, 5, 5) | (1152, 5, 5) | 28800 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.se.conv_reduce.weight | (48, 1152, 1, 1) | (48, 1152) | 55296 | Matrix |
| blocks.5.4.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.5.4.se.conv_expand.weight | (1152, 48, 1, 1) | (1152, 48) | 55296 | Matrix |
| blocks.5.4.se.conv_expand.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.4.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.4.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.6.0.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.6.0.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.conv_dw.weight | (1152, 1, 3, 3) | (1152, 3, 3) | 10368 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.se.conv_reduce.weight | (48, 1152, 1, 1) | (48, 1152) | 55296 | Matrix |
| blocks.6.0.se.conv_reduce.bias | (48,) | (48,) | 48 | Vector |
| blocks.6.0.se.conv_expand.weight | (1152, 48, 1, 1) | (1152, 48) | 55296 | Matrix |
| blocks.6.0.se.conv_expand.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.conv_pwl.weight | (320, 1152, 1, 1) | (320, 1152) | 368640 | Matrix |
| blocks.6.0.bn3.weight | (320,) | (320,) | 320 | Vector |
| blocks.6.0.bn3.bias | (320,) | (320,) | 320 | Vector |
| blocks.6.1.conv_pw.weight | (1920, 320, 1, 1) | (1920, 320) | 614400 | Matrix |
| blocks.6.1.bn1.weight | (1920,) | (1920,) | 1920 | Vector |
| blocks.6.1.bn1.bias | (1920,) | (1920,) | 1920 | Vector |
| blocks.6.1.conv_dw.weight | (1920, 1, 3, 3) | (1920, 3, 3) | 17280 | Tensor rank 3 |
| blocks.6.1.bn2.weight | (1920,) | (1920,) | 1920 | Vector |
| blocks.6.1.bn2.bias | (1920,) | (1920,) | 1920 | Vector |
| blocks.6.1.se.conv_reduce.weight | (80, 1920, 1, 1) | (80, 1920) | 153600 | Matrix |
| blocks.6.1.se.conv_reduce.bias | (80,) | (80,) | 80 | Vector |
| blocks.6.1.se.conv_expand.weight | (1920, 80, 1, 1) | (1920, 80) | 153600 | Matrix |
| blocks.6.1.se.conv_expand.bias | (1920,) | (1920,) | 1920 | Vector |
| blocks.6.1.conv_pwl.weight | (320, 1920, 1, 1) | (320, 1920) | 614400 | Matrix |
| blocks.6.1.bn3.weight | (320,) | (320,) | 320 | Vector |
| blocks.6.1.bn3.bias | (320,) | (320,) | 320 | Vector |
| conv_head.weight | (1280, 320, 1, 1) | (1280, 320) | 409600 | Matrix |
| bn2.weight | (1280,) | (1280,) | 1280 | Vector |
| bn2.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

