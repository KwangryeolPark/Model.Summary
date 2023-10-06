# mobilenetv3_large_100 parameter information

**Number of layers: [ 174 ]**

**Number of parameters: [ 20.916 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 20.916 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 63.22 | 27.59 | 8.62 | 0.57 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.58 | 97.74 | 1.67 | 0.01 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (16, 3, 3, 3) | (16, 3, 3, 3) | 432 | Tensor rank 4 |
| bn1.weight | (16,) | (16,) | 16 | Vector |
| bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.conv_dw.weight | (16, 1, 3, 3) | (16, 3, 3) | 144 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn1.bias | (16,) | (16,) | 16 | Vector |
| blocks.0.0.conv_pw.weight | (16, 16, 1, 1) | (16, 16) | 256 | Matrix |
| blocks.0.0.bn2.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn2.bias | (16,) | (16,) | 16 | Vector |
| blocks.1.0.conv_pw.weight | (64, 16, 1, 1) | (64, 16) | 1024 | Matrix |
| blocks.1.0.bn1.weight | (64,) | (64,) | 64 | Vector |
| blocks.1.0.bn1.bias | (64,) | (64,) | 64 | Vector |
| blocks.1.0.conv_dw.weight | (64, 1, 3, 3) | (64, 3, 3) | 576 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (64,) | (64,) | 64 | Vector |
| blocks.1.0.bn2.bias | (64,) | (64,) | 64 | Vector |
| blocks.1.0.conv_pwl.weight | (24, 64, 1, 1) | (24, 64) | 1536 | Matrix |
| blocks.1.0.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.0.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.1.conv_pw.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.1.1.bn1.weight | (72,) | (72,) | 72 | Vector |
| blocks.1.1.bn1.bias | (72,) | (72,) | 72 | Vector |
| blocks.1.1.conv_dw.weight | (72, 1, 3, 3) | (72, 3, 3) | 648 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (72,) | (72,) | 72 | Vector |
| blocks.1.1.bn2.bias | (72,) | (72,) | 72 | Vector |
| blocks.1.1.conv_pwl.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.1.1.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.1.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.0.conv_pw.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.2.0.bn1.weight | (72,) | (72,) | 72 | Vector |
| blocks.2.0.bn1.bias | (72,) | (72,) | 72 | Vector |
| blocks.2.0.conv_dw.weight | (72, 1, 5, 5) | (72, 5, 5) | 1800 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (72,) | (72,) | 72 | Vector |
| blocks.2.0.bn2.bias | (72,) | (72,) | 72 | Vector |
| blocks.2.0.se.conv_reduce.weight | (24, 72, 1, 1) | (24, 72) | 1728 | Matrix |
| blocks.2.0.se.conv_reduce.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.0.se.conv_expand.weight | (72, 24, 1, 1) | (72, 24) | 1728 | Matrix |
| blocks.2.0.se.conv_expand.bias | (72,) | (72,) | 72 | Vector |
| blocks.2.0.conv_pwl.weight | (40, 72, 1, 1) | (40, 72) | 2880 | Matrix |
| blocks.2.0.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.0.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.1.conv_pw.weight | (120, 40, 1, 1) | (120, 40) | 4800 | Matrix |
| blocks.2.1.bn1.weight | (120,) | (120,) | 120 | Vector |
| blocks.2.1.bn1.bias | (120,) | (120,) | 120 | Vector |
| blocks.2.1.conv_dw.weight | (120, 1, 5, 5) | (120, 5, 5) | 3000 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (120,) | (120,) | 120 | Vector |
| blocks.2.1.bn2.bias | (120,) | (120,) | 120 | Vector |
| blocks.2.1.se.conv_reduce.weight | (32, 120, 1, 1) | (32, 120) | 3840 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.1.se.conv_expand.weight | (120, 32, 1, 1) | (120, 32) | 3840 | Matrix |
| blocks.2.1.se.conv_expand.bias | (120,) | (120,) | 120 | Vector |
| blocks.2.1.conv_pwl.weight | (40, 120, 1, 1) | (40, 120) | 4800 | Matrix |
| blocks.2.1.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.1.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.2.conv_pw.weight | (120, 40, 1, 1) | (120, 40) | 4800 | Matrix |
| blocks.2.2.bn1.weight | (120,) | (120,) | 120 | Vector |
| blocks.2.2.bn1.bias | (120,) | (120,) | 120 | Vector |
| blocks.2.2.conv_dw.weight | (120, 1, 5, 5) | (120, 5, 5) | 3000 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (120,) | (120,) | 120 | Vector |
| blocks.2.2.bn2.bias | (120,) | (120,) | 120 | Vector |
| blocks.2.2.se.conv_reduce.weight | (32, 120, 1, 1) | (32, 120) | 3840 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.2.se.conv_expand.weight | (120, 32, 1, 1) | (120, 32) | 3840 | Matrix |
| blocks.2.2.se.conv_expand.bias | (120,) | (120,) | 120 | Vector |
| blocks.2.2.conv_pwl.weight | (40, 120, 1, 1) | (40, 120) | 4800 | Matrix |
| blocks.2.2.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.2.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.3.0.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.3.0.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.3.0.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.3.0.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.conv_pwl.weight | (80, 240, 1, 1) | (80, 240) | 19200 | Matrix |
| blocks.3.0.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.0.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.1.conv_pw.weight | (200, 80, 1, 1) | (200, 80) | 16000 | Matrix |
| blocks.3.1.bn1.weight | (200,) | (200,) | 200 | Vector |
| blocks.3.1.bn1.bias | (200,) | (200,) | 200 | Vector |
| blocks.3.1.conv_dw.weight | (200, 1, 3, 3) | (200, 3, 3) | 1800 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (200,) | (200,) | 200 | Vector |
| blocks.3.1.bn2.bias | (200,) | (200,) | 200 | Vector |
| blocks.3.1.conv_pwl.weight | (80, 200, 1, 1) | (80, 200) | 16000 | Matrix |
| blocks.3.1.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.1.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.2.conv_pw.weight | (184, 80, 1, 1) | (184, 80) | 14720 | Matrix |
| blocks.3.2.bn1.weight | (184,) | (184,) | 184 | Vector |
| blocks.3.2.bn1.bias | (184,) | (184,) | 184 | Vector |
| blocks.3.2.conv_dw.weight | (184, 1, 3, 3) | (184, 3, 3) | 1656 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (184,) | (184,) | 184 | Vector |
| blocks.3.2.bn2.bias | (184,) | (184,) | 184 | Vector |
| blocks.3.2.conv_pwl.weight | (80, 184, 1, 1) | (80, 184) | 14720 | Matrix |
| blocks.3.2.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.2.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.3.conv_pw.weight | (184, 80, 1, 1) | (184, 80) | 14720 | Matrix |
| blocks.3.3.bn1.weight | (184,) | (184,) | 184 | Vector |
| blocks.3.3.bn1.bias | (184,) | (184,) | 184 | Vector |
| blocks.3.3.conv_dw.weight | (184, 1, 3, 3) | (184, 3, 3) | 1656 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (184,) | (184,) | 184 | Vector |
| blocks.3.3.bn2.bias | (184,) | (184,) | 184 | Vector |
| blocks.3.3.conv_pwl.weight | (80, 184, 1, 1) | (80, 184) | 14720 | Matrix |
| blocks.3.3.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.3.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.4.0.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.4.0.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.4.0.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.4.0.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.se.conv_reduce.weight | (120, 480, 1, 1) | (120, 480) | 57600 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (120,) | (120,) | 120 | Vector |
| blocks.4.0.se.conv_expand.weight | (480, 120, 1, 1) | (480, 120) | 57600 | Matrix |
| blocks.4.0.se.conv_expand.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.conv_pwl.weight | (112, 480, 1, 1) | (112, 480) | 53760 | Matrix |
| blocks.4.0.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.0.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.1.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.1.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.1.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.1.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.se.conv_reduce.weight | (168, 672, 1, 1) | (168, 672) | 112896 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (168,) | (168,) | 168 | Vector |
| blocks.4.1.se.conv_expand.weight | (672, 168, 1, 1) | (672, 168) | 112896 | Matrix |
| blocks.4.1.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.1.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.1.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.5.0.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.5.0.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.5.0.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.conv_dw.weight | (672, 1, 5, 5) | (672, 5, 5) | 16800 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.5.0.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.se.conv_reduce.weight | (168, 672, 1, 1) | (168, 672) | 112896 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (168,) | (168,) | 168 | Vector |
| blocks.5.0.se.conv_expand.weight | (672, 168, 1, 1) | (672, 168) | 112896 | Matrix |
| blocks.5.0.se.conv_expand.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.conv_pwl.weight | (160, 672, 1, 1) | (160, 672) | 107520 | Matrix |
| blocks.5.0.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.5.0.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.5.1.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.5.1.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.5.1.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.1.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.5.1.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.1.se.conv_reduce.weight | (240, 960, 1, 1) | (240, 960) | 230400 | Matrix |
| blocks.5.1.se.conv_reduce.bias | (240,) | (240,) | 240 | Vector |
| blocks.5.1.se.conv_expand.weight | (960, 240, 1, 1) | (960, 240) | 230400 | Matrix |
| blocks.5.1.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.1.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.5.1.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.5.1.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.5.2.conv_pw.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.5.2.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.5.2.bn1.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.2.conv_dw.weight | (960, 1, 5, 5) | (960, 5, 5) | 24000 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (960,) | (960,) | 960 | Vector |
| blocks.5.2.bn2.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.2.se.conv_reduce.weight | (240, 960, 1, 1) | (240, 960) | 230400 | Matrix |
| blocks.5.2.se.conv_reduce.bias | (240,) | (240,) | 240 | Vector |
| blocks.5.2.se.conv_expand.weight | (960, 240, 1, 1) | (960, 240) | 230400 | Matrix |
| blocks.5.2.se.conv_expand.bias | (960,) | (960,) | 960 | Vector |
| blocks.5.2.conv_pwl.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| blocks.5.2.bn3.weight | (160,) | (160,) | 160 | Vector |
| blocks.5.2.bn3.bias | (160,) | (160,) | 160 | Vector |
| blocks.6.0.conv.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| blocks.6.0.bn1.weight | (960,) | (960,) | 960 | Vector |
| blocks.6.0.bn1.bias | (960,) | (960,) | 960 | Vector |
| conv_head.weight | (1280, 960, 1, 1) | (1280, 960) | 1228800 | Matrix |
| conv_head.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

