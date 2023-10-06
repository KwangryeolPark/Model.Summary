# mobilenetv2_110d parameter information

**Number of layers: [ 203 ]**

**Number of parameters: [ 17.229 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 17.229 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.50 | 22.17 | 10.84 | 0.49 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 1.07 | 96.87 | 2.03 | 0.02 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (32, 3, 3, 3) | (32, 3, 3, 3) | 864 | Tensor rank 4 |
| bn1.weight | (32,) | (32,) | 32 | Vector |
| bn1.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.conv_dw.weight | (32, 1, 3, 3) | (32, 3, 3) | 288 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (32,) | (32,) | 32 | Vector |
| blocks.0.0.bn1.bias | (32,) | (32,) | 32 | Vector |
| blocks.0.0.conv_pw.weight | (16, 32, 1, 1) | (16, 32) | 512 | Matrix |
| blocks.0.0.bn2.weight | (16,) | (16,) | 16 | Vector |
| blocks.0.0.bn2.bias | (16,) | (16,) | 16 | Vector |
| blocks.1.0.conv_pw.weight | (96, 16, 1, 1) | (96, 16) | 1536 | Matrix |
| blocks.1.0.bn1.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.0.bn1.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.0.conv_dw.weight | (96, 1, 3, 3) | (96, 3, 3) | 864 | Tensor rank 3 |
| blocks.1.0.bn2.weight | (96,) | (96,) | 96 | Vector |
| blocks.1.0.bn2.bias | (96,) | (96,) | 96 | Vector |
| blocks.1.0.conv_pwl.weight | (24, 96, 1, 1) | (24, 96) | 2304 | Matrix |
| blocks.1.0.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.0.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.1.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.1.1.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.1.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.1.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.1.1.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.1.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.1.conv_pwl.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| blocks.1.1.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.1.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.1.2.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.1.2.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.2.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.2.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.1.2.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.1.2.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.1.2.conv_pwl.weight | (24, 144, 1, 1) | (24, 144) | 3456 | Matrix |
| blocks.1.2.bn3.weight | (24,) | (24,) | 24 | Vector |
| blocks.1.2.bn3.bias | (24,) | (24,) | 24 | Vector |
| blocks.2.0.conv_pw.weight | (144, 24, 1, 1) | (144, 24) | 3456 | Matrix |
| blocks.2.0.bn1.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.0.bn1.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.0.conv_dw.weight | (144, 1, 3, 3) | (144, 3, 3) | 1296 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (144,) | (144,) | 144 | Vector |
| blocks.2.0.bn2.bias | (144,) | (144,) | 144 | Vector |
| blocks.2.0.conv_pwl.weight | (32, 144, 1, 1) | (32, 144) | 4608 | Matrix |
| blocks.2.0.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.0.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.1.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.1.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.1.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.1.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.1.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.1.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.2.1.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.1.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.2.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.2.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.2.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.2.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.2.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.2.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.2.2.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.2.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.2.3.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.3.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.3.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.3.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.2.3.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.3.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.3.conv_pwl.weight | (32, 192, 1, 1) | (32, 192) | 6144 | Matrix |
| blocks.2.3.bn3.weight | (32,) | (32,) | 32 | Vector |
| blocks.2.3.bn3.bias | (32,) | (32,) | 32 | Vector |
| blocks.3.0.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.3.0.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.0.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.0.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.3.0.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.3.0.conv_pwl.weight | (72, 192, 1, 1) | (72, 192) | 13824 | Matrix |
| blocks.3.0.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.0.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.1.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.3.1.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.1.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.1.conv_dw.weight | (432, 1, 3, 3) | (432, 3, 3) | 3888 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.1.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.1.conv_pwl.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| blocks.3.1.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.1.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.2.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.3.2.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.2.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.2.conv_dw.weight | (432, 1, 3, 3) | (432, 3, 3) | 3888 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.2.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.2.conv_pwl.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| blocks.3.2.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.2.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.3.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.3.3.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.3.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.3.conv_dw.weight | (432, 1, 3, 3) | (432, 3, 3) | 3888 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.3.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.3.conv_pwl.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| blocks.3.3.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.3.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.3.4.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.3.4.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.4.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.4.conv_dw.weight | (432, 1, 3, 3) | (432, 3, 3) | 3888 | Tensor rank 3 |
| blocks.3.4.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.3.4.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.3.4.conv_pwl.weight | (72, 432, 1, 1) | (72, 432) | 31104 | Matrix |
| blocks.3.4.bn3.weight | (72,) | (72,) | 72 | Vector |
| blocks.3.4.bn3.bias | (72,) | (72,) | 72 | Vector |
| blocks.4.0.conv_pw.weight | (432, 72, 1, 1) | (432, 72) | 31104 | Matrix |
| blocks.4.0.bn1.weight | (432,) | (432,) | 432 | Vector |
| blocks.4.0.bn1.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.0.conv_dw.weight | (432, 1, 3, 3) | (432, 3, 3) | 3888 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (432,) | (432,) | 432 | Vector |
| blocks.4.0.bn2.bias | (432,) | (432,) | 432 | Vector |
| blocks.4.0.conv_pwl.weight | (104, 432, 1, 1) | (104, 432) | 44928 | Matrix |
| blocks.4.0.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.4.0.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.4.1.conv_pw.weight | (624, 104, 1, 1) | (624, 104) | 64896 | Matrix |
| blocks.4.1.bn1.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.1.bn1.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.1.conv_dw.weight | (624, 1, 3, 3) | (624, 3, 3) | 5616 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.1.bn2.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.1.conv_pwl.weight | (104, 624, 1, 1) | (104, 624) | 64896 | Matrix |
| blocks.4.1.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.4.1.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.4.2.conv_pw.weight | (624, 104, 1, 1) | (624, 104) | 64896 | Matrix |
| blocks.4.2.bn1.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.2.bn1.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.2.conv_dw.weight | (624, 1, 3, 3) | (624, 3, 3) | 5616 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.2.bn2.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.2.conv_pwl.weight | (104, 624, 1, 1) | (104, 624) | 64896 | Matrix |
| blocks.4.2.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.4.2.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.4.3.conv_pw.weight | (624, 104, 1, 1) | (624, 104) | 64896 | Matrix |
| blocks.4.3.bn1.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.3.bn1.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.3.conv_dw.weight | (624, 1, 3, 3) | (624, 3, 3) | 5616 | Tensor rank 3 |
| blocks.4.3.bn2.weight | (624,) | (624,) | 624 | Vector |
| blocks.4.3.bn2.bias | (624,) | (624,) | 624 | Vector |
| blocks.4.3.conv_pwl.weight | (104, 624, 1, 1) | (104, 624) | 64896 | Matrix |
| blocks.4.3.bn3.weight | (104,) | (104,) | 104 | Vector |
| blocks.4.3.bn3.bias | (104,) | (104,) | 104 | Vector |
| blocks.5.0.conv_pw.weight | (624, 104, 1, 1) | (624, 104) | 64896 | Matrix |
| blocks.5.0.bn1.weight | (624,) | (624,) | 624 | Vector |
| blocks.5.0.bn1.bias | (624,) | (624,) | 624 | Vector |
| blocks.5.0.conv_dw.weight | (624, 1, 3, 3) | (624, 3, 3) | 5616 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (624,) | (624,) | 624 | Vector |
| blocks.5.0.bn2.bias | (624,) | (624,) | 624 | Vector |
| blocks.5.0.conv_pwl.weight | (176, 624, 1, 1) | (176, 624) | 109824 | Matrix |
| blocks.5.0.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.5.0.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.5.1.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.5.1.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.1.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.1.conv_dw.weight | (1056, 1, 3, 3) | (1056, 3, 3) | 9504 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.1.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.1.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.5.1.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.5.1.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.5.2.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.5.2.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.2.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.2.conv_dw.weight | (1056, 1, 3, 3) | (1056, 3, 3) | 9504 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.2.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.2.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.5.2.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.5.2.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.5.3.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.5.3.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.3.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.3.conv_dw.weight | (1056, 1, 3, 3) | (1056, 3, 3) | 9504 | Tensor rank 3 |
| blocks.5.3.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.3.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.5.3.conv_pwl.weight | (176, 1056, 1, 1) | (176, 1056) | 185856 | Matrix |
| blocks.5.3.bn3.weight | (176,) | (176,) | 176 | Vector |
| blocks.5.3.bn3.bias | (176,) | (176,) | 176 | Vector |
| blocks.6.0.conv_pw.weight | (1056, 176, 1, 1) | (1056, 176) | 185856 | Matrix |
| blocks.6.0.bn1.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.6.0.bn1.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.6.0.conv_dw.weight | (1056, 1, 3, 3) | (1056, 3, 3) | 9504 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1056,) | (1056,) | 1056 | Vector |
| blocks.6.0.bn2.bias | (1056,) | (1056,) | 1056 | Vector |
| blocks.6.0.conv_pwl.weight | (352, 1056, 1, 1) | (352, 1056) | 371712 | Matrix |
| blocks.6.0.bn3.weight | (352,) | (352,) | 352 | Vector |
| blocks.6.0.bn3.bias | (352,) | (352,) | 352 | Vector |
| conv_head.weight | (1280, 352, 1, 1) | (1280, 352) | 450560 | Matrix |
| bn2.weight | (1280,) | (1280,) | 1280 | Vector |
| bn2.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

