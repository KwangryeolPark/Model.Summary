# mobilenetv2_120d parameter information

**Number of layers: [ 239 ]**

**Number of parameters: [ 22.244 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 22.244 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.53 | 22.18 | 10.88 | 0.42 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 1.11 | 96.72 | 2.15 | 0.01 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (32, 3, 3, 3) | (32, 3, 3, 3) | 864 | Tensor rank 4 |
| bn1.weight | (32,) | (32,) | 32 | Vector |
| bn1.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.conv_dw.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (32,) | (32,) | 32 | Vector |
| blocks.0.0.bn1.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.conv_pw.weight | (24, 32, 1, 1) | (24, 32) | 768 | Matrix |
| blocks.0.0.bn2.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.0.bn2.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.0.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.1.0.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.0.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.0.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.0.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.0.conv_pwl.weight | (32, 144, 1, 1) | (32, 144) | 4608 | Matrix |
| blocks.1.0.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.0.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.1.1.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.1.1.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.1.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.1.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.1.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.1.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.1.1.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.1.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.1.2.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.1.2.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.2.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.2.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.1.2.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.1.2.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.1.2.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.1.2.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.1.2.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.0.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.0.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.0.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.0.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.conv_pwl.weight | (40, 192, 1, 1) | (40, 192) | 7680 | Matrix |
| blocks.2.0.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.0.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.1.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.1.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.1.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.1.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.1.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.1.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.1.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.2.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.2.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.2.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.2.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.2.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.2.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.2.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.2.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.3.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.3.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.3.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.3.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.2.3.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.3.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.3.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.3.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.3.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.4.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.4.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.4.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.4.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.2.4.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.4.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.4.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.2.4.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.2.4.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.3.0.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.3.0.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.3.0.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.3.0.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.3.0.conv_pwl.weight | (80, 240, 1, 1) | (80, 240) | 19200 | Matrix |
| blocks.3.0.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.0.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.1.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.1.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.1.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.1.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.1.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.1.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.1.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.1.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.2.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.2.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.2.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.2.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.2.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.2.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.2.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.2.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.3.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.3.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.3.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.3.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.3.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.3.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.3.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.3.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.4.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.4.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.4.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.4.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.4.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.4.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.4.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.4.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.4.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.3.5.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.3.5.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.5.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.5.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.3.5.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.3.5.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.3.5.conv_pwl.weight | (80, 480, 1, 1) | (80, 480) | 38400 | Matrix |
| blocks.3.5.bn3.weight | (80,) | (80,) | 80 | Vector |
| blocks.3.5.bn3.bias | (80,) | (80,) | 80 | Vector |
| blocks.4.0.conv_pw.weight | (480, 80, 1, 1) | (480, 80) | 38400 | Matrix |
| blocks.4.0.bn1.weight | (480,) | (480,) | 480 | Vector |
| blocks.4.0.bn1.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.conv_dw.weight | (480, 1, 3, 3) | (480, 3, 3) | 4320 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (480,) | (480,) | 480 | Vector |
| blocks.4.0.bn2.bias | (480,) | (480,) | 480 | Vector |
| blocks.4.0.conv_pwl.weight | (112, 480, 1, 1) | (112, 480) | 53760 | Matrix |
| blocks.4.0.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.0.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.1.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.1.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.1.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.1.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.1.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.1.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.1.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.2.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.2.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.2.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.2.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.2.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.2.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.2.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.2.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.3.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.3.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.3.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.3.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.3.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.3.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.3.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.3.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.4.4.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.4.4.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.4.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.4.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.4.4.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.4.4.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.4.4.conv_pwl.weight | (112, 672, 1, 1) | (112, 672) | 75264 | Matrix |
| blocks.4.4.bn3.weight | (112,) | (112,) | 112 | Vector |
| blocks.4.4.bn3.bias | (112,) | (112,) | 112 | Vector |
| blocks.5.0.conv_pw.weight | (672, 112, 1, 1) | (672, 112) | 75264 | Matrix |
| blocks.5.0.bn1.weight | (672,) | (672,) | 672 | Vector |
| blocks.5.0.bn1.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.conv_dw.weight | (672, 1, 3, 3) | (672, 3, 3) | 6048 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (672,) | (672,) | 672 | Vector |
| blocks.5.0.bn2.bias | (672,) | (672,) | 672 | Vector |
| blocks.5.0.conv_pwl.weight | (192, 672, 1, 1) | (192, 672) | 129024 | Matrix |
| blocks.5.0.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.0.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.1.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.1.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.conv_dw.weight | (1152, 1, 3, 3) | (1152, 3, 3) | 10368 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.1.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.1.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.1.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.2.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.2.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.conv_dw.weight | (1152, 1, 3, 3) | (1152, 3, 3) | 10368 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.2.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.2.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.2.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.3.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.3.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.conv_dw.weight | (1152, 1, 3, 3) | (1152, 3, 3) | 10368 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.3.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.3.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.3.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.5.4.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.5.4.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.conv_dw.weight | (1152, 1, 3, 3) | (1152, 3, 3) | 10368 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.5.4.conv_pwl.weight | (192, 1152, 1, 1) | (192, 1152) | 221184 | Matrix |
| blocks.5.4.bn3.weight | (192,) | (192,) | 192 | Vector |
| blocks.5.4.bn3.bias | (192,) | (192,) | 192 | Vector |
| blocks.6.0.conv_pw.weight | (1152, 192, 1, 1) | (1152, 192) | 221184 | Matrix |
| blocks.6.0.bn1.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.bn1.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.conv_dw.weight | (1152, 1, 3, 3) | (1152, 3, 3) | 10368 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.bn2.bias | (1152,) | (1152,) | 1152 | Vector |
| blocks.6.0.conv_pwl.weight | (384, 1152, 1, 1) | (384, 1152) | 442368 | Matrix |
| blocks.6.0.bn3.weight | (384,) | (384,) | 384 | Vector |
| blocks.6.0.bn3.bias | (384,) | (384,) | 384 | Vector |
| conv_head.weight | (1280, 384, 1, 1) | (1280, 384) | 491520 | Matrix |
| bn2.weight | (1280,) | (1280,) | 1280 | Vector |
| bn2.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

