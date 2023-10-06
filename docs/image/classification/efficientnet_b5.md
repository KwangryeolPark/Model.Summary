# efficientnet_b5 parameter information

**Number of layers: [ 506 ]**

**Number of parameters: [ 115.928 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 115.928 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.46 | 30.63 | 7.71 | 0.20 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.70 | 96.85 | 2.44 | 0.00 | 

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
| blocks.0.2.conv_dw.weight | (24, 1, 3, 3) | (24, 3, 3) | 216 | Tensor rank 3 |
| blocks.0.2.bn1.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.2.bn1.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.2.se.conv_reduce.weight | (6, 24, 1, 1) | (6, 24) | 144 | Matrix |
| blocks.0.2.se.conv_reduce.bias | (6,) | (6,) | 6 | Vector |
| blocks.0.2.se.conv_expand.weight | (24, 6, 1, 1) | (24, 6) | 144 | Matrix |
| blocks.0.2.se.conv_expand.bias | (24,) | (24,) | 24 | Vector |
| blocks.0.2.conv_pw.weight | (24, 24, 1, 1) | (24, 24) | 576 | Matrix |
| blocks.0.2.bn2.weight | (24,) | (24,) | 24 | Vector |
| blocks.0.2.bn2.bias | (24,) | (24,) | 24 | Vector |
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
| blocks.1.0.conv_pwl.weight | (40, 144, 1, 1) | (40, 144) | 5760 | Matrix |
| blocks.1.0.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.0.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.1.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.1.1.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.1.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.1.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.1.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.1.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.1.1.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.1.1.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.1.1.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.1.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.1.1.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.1.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.2.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.1.2.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.2.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.2.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.1.2.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.2.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.2.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.1.2.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.1.2.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.1.2.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.2.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.1.2.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.2.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.3.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.1.3.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.3.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.3.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.1.3.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.3.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.3.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.1.3.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.1.3.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.1.3.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.3.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.1.3.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.3.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.1.4.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.1.4.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.4.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.4.conv_dw.weight | (240, 1, 3, 3) | (240, 3, 3) | 2160 | Tensor rank 3 |
| blocks.1.4.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.1.4.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.4.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.1.4.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.1.4.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.1.4.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.1.4.conv_pwl.weight | (40, 240, 1, 1) | (40, 240) | 9600 | Matrix |
| blocks.1.4.bn3.weight | (40,) | (40,) | 40 | Vector |
| blocks.1.4.bn3.bias | (40,) | (40,) | 40 | Vector |
| blocks.2.0.conv_pw.weight | (240, 40, 1, 1) | (240, 40) | 9600 | Matrix |
| blocks.2.0.bn1.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.0.bn1.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.0.conv_dw.weight | (240, 1, 5, 5) | (240, 5, 5) | 6000 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (240,) | (240,) | 240 | Vector |
| blocks.2.0.bn2.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.0.se.conv_reduce.weight | (10, 240, 1, 1) | (10, 240) | 2400 | Matrix |
| blocks.2.0.se.conv_reduce.bias | (10,) | (10,) | 10 | Vector |
| blocks.2.0.se.conv_expand.weight | (240, 10, 1, 1) | (240, 10) | 2400 | Matrix |
| blocks.2.0.se.conv_expand.bias | (240,) | (240,) | 240 | Vector |
| blocks.2.0.conv_pwl.weight | (64, 240, 1, 1) | (64, 240) | 15360 | Matrix |
| blocks.2.0.bn3.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.0.bn3.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.1.conv_pw.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| blocks.2.1.bn1.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.1.bn1.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.1.conv_dw.weight | (384, 1, 5, 5) | (384, 5, 5) | 9600 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.1.bn2.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.1.se.conv_reduce.weight | (16, 384, 1, 1) | (16, 384) | 6144 | Matrix |
| blocks.2.1.se.conv_reduce.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.1.se.conv_expand.weight | (384, 16, 1, 1) | (384, 16) | 6144 | Matrix |
| blocks.2.1.se.conv_expand.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.1.conv_pwl.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| blocks.2.1.bn3.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.1.bn3.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.2.conv_pw.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| blocks.2.2.bn1.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.2.bn1.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.2.conv_dw.weight | (384, 1, 5, 5) | (384, 5, 5) | 9600 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.2.bn2.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.2.se.conv_reduce.weight | (16, 384, 1, 1) | (16, 384) | 6144 | Matrix |
| blocks.2.2.se.conv_reduce.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.2.se.conv_expand.weight | (384, 16, 1, 1) | (384, 16) | 6144 | Matrix |
| blocks.2.2.se.conv_expand.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.2.conv_pwl.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| blocks.2.2.bn3.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.2.bn3.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.3.conv_pw.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| blocks.2.3.bn1.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.3.bn1.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.3.conv_dw.weight | (384, 1, 5, 5) | (384, 5, 5) | 9600 | Tensor rank 3 |
| blocks.2.3.bn2.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.3.bn2.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.3.se.conv_reduce.weight | (16, 384, 1, 1) | (16, 384) | 6144 | Matrix |
| blocks.2.3.se.conv_reduce.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.3.se.conv_expand.weight | (384, 16, 1, 1) | (384, 16) | 6144 | Matrix |
| blocks.2.3.se.conv_expand.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.3.conv_pwl.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| blocks.2.3.bn3.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.3.bn3.bias | (64,) | (64,) | 64 | Vector |
| blocks.2.4.conv_pw.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| blocks.2.4.bn1.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.4.bn1.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.4.conv_dw.weight | (384, 1, 5, 5) | (384, 5, 5) | 9600 | Tensor rank 3 |
| blocks.2.4.bn2.weight | (384,) | (384,) | 384 | Vector |
| blocks.2.4.bn2.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.4.se.conv_reduce.weight | (16, 384, 1, 1) | (16, 384) | 6144 | Matrix |
| blocks.2.4.se.conv_reduce.bias | (16,) | (16,) | 16 | Vector |
| blocks.2.4.se.conv_expand.weight | (384, 16, 1, 1) | (384, 16) | 6144 | Matrix |
| blocks.2.4.se.conv_expand.bias | (384,) | (384,) | 384 | Vector |
| blocks.2.4.conv_pwl.weight | (64, 384, 1, 1) | (64, 384) | 24576 | Matrix |
| blocks.2.4.bn3.weight | (64,) | (64,) | 64 | Vector |
| blocks.2.4.bn3.bias | (64,) | (64,) | 64 | Vector |
| blocks.3.0.conv_pw.weight | (384, 64, 1, 1) | (384, 64) | 24576 | Matrix |
| blocks.3.0.bn1.weight | (384,) | (384,) | 384 | Vector |
| blocks.3.0.bn1.bias | (384,) | (384,) | 384 | Vector |
| blocks.3.0.conv_dw.weight | (384, 1, 3, 3) | (384, 3, 3) | 3456 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (384,) | (384,) | 384 | Vector |
| blocks.3.0.bn2.bias | (384,) | (384,) | 384 | Vector |
| blocks.3.0.se.conv_reduce.weight | (16, 384, 1, 1) | (16, 384) | 6144 | Matrix |
| blocks.3.0.se.conv_reduce.bias | (16,) | (16,) | 16 | Vector |
| blocks.3.0.se.conv_expand.weight | (384, 16, 1, 1) | (384, 16) | 6144 | Matrix |
| blocks.3.0.se.conv_expand.bias | (384,) | (384,) | 384 | Vector |
| blocks.3.0.conv_pwl.weight | (128, 384, 1, 1) | (128, 384) | 49152 | Matrix |
| blocks.3.0.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.0.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.3.1.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.3.1.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.1.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.1.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.1.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.1.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.1.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.3.1.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.1.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.3.1.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.1.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.3.2.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.3.2.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.2.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.2.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.2.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.2.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.3.2.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.2.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.3.2.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.2.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.3.2.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.2.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.3.3.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.3.3.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.3.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.3.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.3.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.3.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.3.3.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.3.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.3.3.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.3.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.3.3.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.3.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.3.4.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.3.4.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.4.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.4.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.3.4.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.4.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.4.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.3.4.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.4.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.3.4.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.4.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.3.4.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.4.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.3.5.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.3.5.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.5.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.5.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.3.5.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.5.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.5.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.3.5.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.5.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.3.5.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.5.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.3.5.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.5.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.3.6.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.3.6.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.6.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.6.conv_dw.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| blocks.3.6.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.3.6.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.6.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.3.6.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.6.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.3.6.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.3.6.conv_pwl.weight | (128, 768, 1, 1) | (128, 768) | 98304 | Matrix |
| blocks.3.6.bn3.weight | (128,) | (128,) | 128 | Vector |
| blocks.3.6.bn3.bias | (128,) | (128,) | 128 | Vector |
| blocks.4.0.conv_pw.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| blocks.4.0.bn1.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.0.bn1.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.0.conv_dw.weight | (768, 1, 5, 5) | (768, 5, 5) | 19200 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (768,) | (768,) | 768 | Vector |
| blocks.4.0.bn2.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.0.se.conv_reduce.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (32,) | (32,) | 32 | Vector |
| blocks.4.0.se.conv_expand.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| blocks.4.0.se.conv_expand.bias | (768,) | (768,) | 768 | Vector |
| blocks.4.0.conv_pwl.weight | (176, 768, 1, 1) | (176, 768) | 135168 | Matrix |
| blocks.4.0.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.0.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.4.1.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.4.1.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.1.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.1.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.1.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.1.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.4.1.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.4.1.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.1.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.4.1.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.1.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.4.2.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.4.2.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.2.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.2.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.2.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.2.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.4.2.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.4.2.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.2.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.4.2.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.2.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.4.3.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.4.3.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.3.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.3.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.3.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.3.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.4.3.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.4.3.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.4.3.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.3.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.4.3.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.3.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.4.4.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.4.4.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.4.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.4.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.4.4.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.4.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.4.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.4.4.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.4.4.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.4.4.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.4.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.4.4.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.4.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.4.5.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.4.5.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.5.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.5.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.4.5.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.5.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.5.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.4.5.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.4.5.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.4.5.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.5.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.4.5.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.5.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.4.6.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.4.6.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.6.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.6.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.4.6.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.6.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.6.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.4.6.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.4.6.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.4.6.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.4.6.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.4.6.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.4.6.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.5.0.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.5.0.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.0.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.0.conv_dw.weight | (1056, 1, 5, 5) | (1056, 5, 5) | 26400 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.0.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.0.se.conv_reduce.weight | (44, 1056, 1, 1) | (44, 1056) | 46464 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (44,) | (44,) | 44 | Vector |
| blocks.5.0.se.conv_expand.weight | (1056, 44, 1, 1) | (1056, 44) | 46464 | Matrix |
| blocks.5.0.se.conv_expand.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.0.conv_pwl.weight | (304, 1056, 1, 1) | (304, 1056) | 321024 | Matrix |
| blocks.5.0.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.0.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.1.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.1.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.1.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.1.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.1.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.1.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.1.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.1.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.1.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.1.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.1.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.1.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.2.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.2.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.2.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.2.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.2.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.2.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.2.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.2.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.2.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.2.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.2.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.2.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.3.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.3.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.3.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.3.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.3.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.3.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.3.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.3.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.3.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.3.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.3.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.3.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.4.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.4.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.4.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.4.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.4.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.4.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.4.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.4.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.4.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.4.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.4.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.4.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.5.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.5.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.5.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.5.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.5.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.5.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.5.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.5.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.5.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.5.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.5.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.5.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.5.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.6.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.6.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.6.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.6.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.6.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.6.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.6.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.6.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.6.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.6.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.6.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.6.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.6.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.7.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.7.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.7.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.7.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.7.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.7.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.7.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.7.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.7.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.7.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.7.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.7.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.7.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.5.8.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.5.8.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.8.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.8.conv_dw.weight | (1824, 1, 5, 5) | (1824, 5, 5) | 45600 | Tensor rank 3 |
| blocks.5.8.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.8.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.8.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.5.8.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.5.8.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.5.8.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.5.8.conv_pwl.weight | (304, 1824, 1, 1) | (304, 1824) | 554496 | Matrix |
| blocks.5.8.bn3.weight | (304,) | (304,) | 304 | Vector |
| blocks.5.8.bn3.bias | (304,) | (304,) | 304 | Vector |
| blocks.6.0.conv_pw.weight | (1824, 304, 1, 1) | (1824, 304) | 554496 | Matrix |
| blocks.6.0.bn1.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.6.0.bn1.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.6.0.conv_dw.weight | (1824, 1, 3, 3) | (1824, 3, 3) | 16416 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1824,) | (1824,) | 1824 | Vector |
| blocks.6.0.bn2.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.6.0.se.conv_reduce.weight | (76, 1824, 1, 1) | (76, 1824) | 138624 | Matrix |
| blocks.6.0.se.conv_reduce.bias | (76,) | (76,) | 76 | Vector |
| blocks.6.0.se.conv_expand.weight | (1824, 76, 1, 1) | (1824, 76) | 138624 | Matrix |
| blocks.6.0.se.conv_expand.bias | (1824,) | (1824,) | 1824 | Vector |
| blocks.6.0.conv_pwl.weight | (512, 1824, 1, 1) | (512, 1824) | 933888 | Matrix |
| blocks.6.0.bn3.weight | (512,) | (512,) | 512 | Vector |
| blocks.6.0.bn3.bias | (512,) | (512,) | 512 | Vector |
| blocks.6.1.conv_pw.weight | (3072, 512, 1, 1) | (3072, 512) | 1572864 | Matrix |
| blocks.6.1.bn1.weight | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.1.bn1.bias | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.1.conv_dw.weight | (3072, 1, 3, 3) | (3072, 3, 3) | 27648 | Tensor rank 3 |
| blocks.6.1.bn2.weight | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.1.bn2.bias | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.1.se.conv_reduce.weight | (128, 3072, 1, 1) | (128, 3072) | 393216 | Matrix |
| blocks.6.1.se.conv_reduce.bias | (128,) | (128,) | 128 | Vector |
| blocks.6.1.se.conv_expand.weight | (3072, 128, 1, 1) | (3072, 128) | 393216 | Matrix |
| blocks.6.1.se.conv_expand.bias | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.1.conv_pwl.weight | (512, 3072, 1, 1) | (512, 3072) | 1572864 | Matrix |
| blocks.6.1.bn3.weight | (512,) | (512,) | 512 | Vector |
| blocks.6.1.bn3.bias | (512,) | (512,) | 512 | Vector |
| blocks.6.2.conv_pw.weight | (3072, 512, 1, 1) | (3072, 512) | 1572864 | Matrix |
| blocks.6.2.bn1.weight | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.2.bn1.bias | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.2.conv_dw.weight | (3072, 1, 3, 3) | (3072, 3, 3) | 27648 | Tensor rank 3 |
| blocks.6.2.bn2.weight | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.2.bn2.bias | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.2.se.conv_reduce.weight | (128, 3072, 1, 1) | (128, 3072) | 393216 | Matrix |
| blocks.6.2.se.conv_reduce.bias | (128,) | (128,) | 128 | Vector |
| blocks.6.2.se.conv_expand.weight | (3072, 128, 1, 1) | (3072, 128) | 393216 | Matrix |
| blocks.6.2.se.conv_expand.bias | (3072,) | (3072,) | 3072 | Vector |
| blocks.6.2.conv_pwl.weight | (512, 3072, 1, 1) | (512, 3072) | 1572864 | Matrix |
| blocks.6.2.bn3.weight | (512,) | (512,) | 512 | Vector |
| blocks.6.2.bn3.bias | (512,) | (512,) | 512 | Vector |
| conv_head.weight | (2048, 512, 1, 1) | (2048, 512) | 1048576 | Matrix |
| bn2.weight | (2048,) | (2048,) | 2048 | Vector |
| bn2.bias | (2048,) | (2048,) | 2048 | Vector |
| classifier.weight | (1000, 2048) | (1000, 2048) | 2048000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

