# efficientnet_b2 parameter information

**Number of layers: [ 301 ]**

**Number of parameters: [ 34.752 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 34.752 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 61.46 | 30.56 | 7.64 | 0.33 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.92 | 96.01 | 3.06 | 0.01 | 

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
| blocks.2.0.conv_pwl.weight | (48, 144, 1, 1) | (48, 144) | 6912 | Matrix |
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
| blocks.3.0.conv_pwl.weight | (88, 288, 1, 1) | (88, 288) | 25344 | Matrix |
| blocks.3.0.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.0.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.3.1.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.3.1.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.1.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.1.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.1.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.1.se.conv_reduce.weight | (22, 528, 1, 1) | (22, 528) | 11616 | Matrix |
| blocks.3.1.se.conv_reduce.bias | (22,) | (22,) | 22 | Vector |
| blocks.3.1.se.conv_expand.weight | (528, 22, 1, 1) | (528, 22) | 11616 | Matrix |
| blocks.3.1.se.conv_expand.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.1.conv_pwl.weight | (88, 528, 1, 1) | (88, 528) | 46464 | Matrix |
| blocks.3.1.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.1.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.3.2.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.3.2.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.2.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.2.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.2.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.2.se.conv_reduce.weight | (22, 528, 1, 1) | (22, 528) | 11616 | Matrix |
| blocks.3.2.se.conv_reduce.bias | (22,) | (22,) | 22 | Vector |
| blocks.3.2.se.conv_expand.weight | (528, 22, 1, 1) | (528, 22) | 11616 | Matrix |
| blocks.3.2.se.conv_expand.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.2.conv_pwl.weight | (88, 528, 1, 1) | (88, 528) | 46464 | Matrix |
| blocks.3.2.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.2.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.3.3.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.3.3.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.3.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.3.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.3.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.3.se.conv_reduce.weight | (22, 528, 1, 1) | (22, 528) | 11616 | Matrix |
| blocks.3.3.se.conv_reduce.bias | (22,) | (22,) | 22 | Vector |
| blocks.3.3.se.conv_expand.weight | (528, 22, 1, 1) | (528, 22) | 11616 | Matrix |
| blocks.3.3.se.conv_expand.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.3.conv_pwl.weight | (88, 528, 1, 1) | (88, 528) | 46464 | Matrix |
| blocks.3.3.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.3.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.4.0.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.4.0.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.4.0.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.4.0.conv_dw.weight | (528, 1, 5, 5) | (528, 5, 5) | 13200 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.4.0.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.4.0.se.conv_reduce.weight | (22, 528, 1, 1) | (22, 528) | 11616 | Matrix |
| blocks.4.0.se.conv_reduce.bias | (22,) | (22,) | 22 | Vector |
| blocks.4.0.se.conv_expand.weight | (528, 22, 1, 1) | (528, 22) | 11616 | Matrix |
| blocks.4.0.se.conv_expand.bias | (528,) | (528,) | 528 | Vector |
| blocks.4.0.conv_pwl.weight | (120, 528, 1, 1) | (120, 528) | 63360 | Matrix |
| blocks.4.0.bn3.weight | (120,) | (120,) | 120 | Vector |
| blocks.4.0.bn3.bias | (120,) | (120,) | 120 | Vector |
| blocks.4.1.conv_pw.weight | (720, 120, 1, 1) | (720, 120) | 86400 | Matrix |
| blocks.4.1.bn1.weight | (720,) | (720,) | 720 | Vector |
| blocks.4.1.bn1.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.1.conv_dw.weight | (720, 1, 5, 5) | (720, 5, 5) | 18000 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (720,) | (720,) | 720 | Vector |
| blocks.4.1.bn2.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.1.se.conv_reduce.weight | (30, 720, 1, 1) | (30, 720) | 21600 | Matrix |
| blocks.4.1.se.conv_reduce.bias | (30,) | (30,) | 30 | Vector |
| blocks.4.1.se.conv_expand.weight | (720, 30, 1, 1) | (720, 30) | 21600 | Matrix |
| blocks.4.1.se.conv_expand.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.1.conv_pwl.weight | (120, 720, 1, 1) | (120, 720) | 86400 | Matrix |
| blocks.4.1.bn3.weight | (120,) | (120,) | 120 | Vector |
| blocks.4.1.bn3.bias | (120,) | (120,) | 120 | Vector |
| blocks.4.2.conv_pw.weight | (720, 120, 1, 1) | (720, 120) | 86400 | Matrix |
| blocks.4.2.bn1.weight | (720,) | (720,) | 720 | Vector |
| blocks.4.2.bn1.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.2.conv_dw.weight | (720, 1, 5, 5) | (720, 5, 5) | 18000 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (720,) | (720,) | 720 | Vector |
| blocks.4.2.bn2.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.2.se.conv_reduce.weight | (30, 720, 1, 1) | (30, 720) | 21600 | Matrix |
| blocks.4.2.se.conv_reduce.bias | (30,) | (30,) | 30 | Vector |
| blocks.4.2.se.conv_expand.weight | (720, 30, 1, 1) | (720, 30) | 21600 | Matrix |
| blocks.4.2.se.conv_expand.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.2.conv_pwl.weight | (120, 720, 1, 1) | (120, 720) | 86400 | Matrix |
| blocks.4.2.bn3.weight | (120,) | (120,) | 120 | Vector |
| blocks.4.2.bn3.bias | (120,) | (120,) | 120 | Vector |
| blocks.4.3.conv_pw.weight | (720, 120, 1, 1) | (720, 120) | 86400 | Matrix |
| blocks.4.3.bn1.weight | (720,) | (720,) | 720 | Vector |
| blocks.4.3.bn1.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.3.conv_dw.weight | (720, 1, 5, 5) | (720, 5, 5) | 18000 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (720,) | (720,) | 720 | Vector |
| blocks.4.3.bn2.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.3.se.conv_reduce.weight | (30, 720, 1, 1) | (30, 720) | 21600 | Matrix |
| blocks.4.3.se.conv_reduce.bias | (30,) | (30,) | 30 | Vector |
| blocks.4.3.se.conv_expand.weight | (720, 30, 1, 1) | (720, 30) | 21600 | Matrix |
| blocks.4.3.se.conv_expand.bias | (720,) | (720,) | 720 | Vector |
| blocks.4.3.conv_pwl.weight | (120, 720, 1, 1) | (120, 720) | 86400 | Matrix |
| blocks.4.3.bn3.weight | (120,) | (120,) | 120 | Vector |
| blocks.4.3.bn3.bias | (120,) | (120,) | 120 | Vector |
| blocks.5.0.conv_pw.weight | (720, 120, 1, 1) | (720, 120) | 86400 | Matrix |
| blocks.5.0.bn1.weight | (720,) | (720,) | 720 | Vector |
| blocks.5.0.bn1.bias | (720,) | (720,) | 720 | Vector |
| blocks.5.0.conv_dw.weight | (720, 1, 5, 5) | (720, 5, 5) | 18000 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (720,) | (720,) | 720 | Vector |
| blocks.5.0.bn2.bias | (720,) | (720,) | 720 | Vector |
| blocks.5.0.se.conv_reduce.weight | (30, 720, 1, 1) | (30, 720) | 21600 | Matrix |
| blocks.5.0.se.conv_reduce.bias | (30,) | (30,) | 30 | Vector |
| blocks.5.0.se.conv_expand.weight | (720, 30, 1, 1) | (720, 30) | 21600 | Matrix |
| blocks.5.0.se.conv_expand.bias | (720,) | (720,) | 720 | Vector |
| blocks.5.0.conv_pwl.weight | (208, 720, 1, 1) | (208, 720) | 149760 | Matrix |
| blocks.5.0.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.0.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.5.1.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.5.1.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.1.conv_dw.weight | (1248, 1, 5, 5) | (1248, 5, 5) | 31200 | Tensor rank 3 |
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
| blocks.5.2.conv_dw.weight | (1248, 1, 5, 5) | (1248, 5, 5) | 31200 | Tensor rank 3 |
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
| blocks.5.3.conv_dw.weight | (1248, 1, 5, 5) | (1248, 5, 5) | 31200 | Tensor rank 3 |
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
| blocks.5.4.conv_dw.weight | (1248, 1, 5, 5) | (1248, 5, 5) | 31200 | Tensor rank 3 |
| blocks.5.4.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.5.4.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.5.4.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.5.4.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.5.4.conv_pwl.weight | (208, 1248, 1, 1) | (208, 1248) | 259584 | Matrix |
| blocks.5.4.bn3.weight | (208,) | (208,) | 208 | Vector |
| blocks.5.4.bn3.bias | (208,) | (208,) | 208 | Vector |
| blocks.6.0.conv_pw.weight | (1248, 208, 1, 1) | (1248, 208) | 259584 | Matrix |
| blocks.6.0.bn1.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.6.0.bn1.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.6.0.conv_dw.weight | (1248, 1, 3, 3) | (1248, 3, 3) | 11232 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1248,) | (1248,) | 1248 | Vector |
| blocks.6.0.bn2.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.6.0.se.conv_reduce.weight | (52, 1248, 1, 1) | (52, 1248) | 64896 | Matrix |
| blocks.6.0.se.conv_reduce.bias | (52,) | (52,) | 52 | Vector |
| blocks.6.0.se.conv_expand.weight | (1248, 52, 1, 1) | (1248, 52) | 64896 | Matrix |
| blocks.6.0.se.conv_expand.bias | (1248,) | (1248,) | 1248 | Vector |
| blocks.6.0.conv_pwl.weight | (352, 1248, 1, 1) | (352, 1248) | 439296 | Matrix |
| blocks.6.0.bn3.weight | (352,) | (352,) | 352 | Vector |
| blocks.6.0.bn3.bias | (352,) | (352,) | 352 | Vector |
| blocks.6.1.conv_pw.weight | (2112, 352, 1, 1) | (2112, 352) | 743424 | Matrix |
| blocks.6.1.bn1.weight | (2112,) | (2112,) | 2112 | Vector |
| blocks.6.1.bn1.bias | (2112,) | (2112,) | 2112 | Vector |
| blocks.6.1.conv_dw.weight | (2112, 1, 3, 3) | (2112, 3, 3) | 19008 | Tensor rank 3 |
| blocks.6.1.bn2.weight | (2112,) | (2112,) | 2112 | Vector |
| blocks.6.1.bn2.bias | (2112,) | (2112,) | 2112 | Vector |
| blocks.6.1.se.conv_reduce.weight | (88, 2112, 1, 1) | (88, 2112) | 185856 | Matrix |
| blocks.6.1.se.conv_reduce.bias | (88,) | (88,) | 88 | Vector |
| blocks.6.1.se.conv_expand.weight | (2112, 88, 1, 1) | (2112, 88) | 185856 | Matrix |
| blocks.6.1.se.conv_expand.bias | (2112,) | (2112,) | 2112 | Vector |
| blocks.6.1.conv_pwl.weight | (352, 2112, 1, 1) | (352, 2112) | 743424 | Matrix |
| blocks.6.1.bn3.weight | (352,) | (352,) | 352 | Vector |
| blocks.6.1.bn3.bias | (352,) | (352,) | 352 | Vector |
| conv_head.weight | (1408, 352, 1, 1) | (1408, 352) | 495616 | Matrix |
| bn2.weight | (1408,) | (1408,) | 1408 | Vector |
| bn2.bias | (1408,) | (1408,) | 1408 | Vector |
| classifier.weight | (1000, 1408) | (1000, 1408) | 1408000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

