# mobilenetv2_140 parameter information

**Number of layers: [ 158 ]**

**Number of parameters: [ 23.303 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 23.303 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 66.46 | 22.15 | 10.76 | 0.63 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.80 | 97.70 | 1.48 | 0.02 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv_stem.weight | (48, 3, 3, 3) | (48, 3, 3, 3) | 1296 | Tensor rank 4 |
| bn1.weight | (48,) | (48,) | 48 | Vector |
| bn1.bias | (48,) | (48,) | 48 | Vector |
| blocks.0.0.conv_dw.weight | (48, 1, 3, 3) | (48, 3, 3) | 432 | Tensor rank 3 |
| blocks.0.0.bn1.weight | (48,) | (48,) | 48 | Vector |
| blocks.0.0.bn1.bias | (48,) | (48,) | 48 | Vector |
| blocks.0.0.conv_pw.weight | (24, 48, 1, 1) | (24, 48) | 1152 | Matrix |
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
| blocks.2.0.conv_pw.weight | (192, 32, 1, 1) | (192, 32) | 6144 | Matrix |
| blocks.2.0.bn1.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.0.bn1.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.conv_dw.weight | (192, 1, 3, 3) | (192, 3, 3) | 1728 | Tensor rank 3 |
| blocks.2.0.bn2.weight | (192,) | (192,) | 192 | Vector |
| blocks.2.0.bn2.bias | (192,) | (192,) | 192 | Vector |
| blocks.2.0.conv_pwl.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| blocks.2.0.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.0.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.1.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.2.1.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.1.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.1.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.2.1.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.1.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.1.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.2.1.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.1.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.2.2.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.2.2.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.2.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.2.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.2.2.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.2.2.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.2.2.conv_pwl.weight | (48, 288, 1, 1) | (48, 288) | 13824 | Matrix |
| blocks.2.2.bn3.weight | (48,) | (48,) | 48 | Vector |
| blocks.2.2.bn3.bias | (48,) | (48,) | 48 | Vector |
| blocks.3.0.conv_pw.weight | (288, 48, 1, 1) | (288, 48) | 13824 | Matrix |
| blocks.3.0.bn1.weight | (288,) | (288,) | 288 | Vector |
| blocks.3.0.bn1.bias | (288,) | (288,) | 288 | Vector |
| blocks.3.0.conv_dw.weight | (288, 1, 3, 3) | (288, 3, 3) | 2592 | Tensor rank 3 |
| blocks.3.0.bn2.weight | (288,) | (288,) | 288 | Vector |
| blocks.3.0.bn2.bias | (288,) | (288,) | 288 | Vector |
| blocks.3.0.conv_pwl.weight | (88, 288, 1, 1) | (88, 288) | 25344 | Matrix |
| blocks.3.0.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.0.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.3.1.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.3.1.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.1.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.1.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.3.1.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.1.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.1.conv_pwl.weight | (88, 528, 1, 1) | (88, 528) | 46464 | Matrix |
| blocks.3.1.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.1.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.3.2.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.3.2.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.2.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.2.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.3.2.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.2.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.2.conv_pwl.weight | (88, 528, 1, 1) | (88, 528) | 46464 | Matrix |
| blocks.3.2.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.2.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.3.3.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.3.3.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.3.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.3.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.3.3.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.3.3.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.3.3.conv_pwl.weight | (88, 528, 1, 1) | (88, 528) | 46464 | Matrix |
| blocks.3.3.bn3.weight | (88,) | (88,) | 88 | Vector |
| blocks.3.3.bn3.bias | (88,) | (88,) | 88 | Vector |
| blocks.4.0.conv_pw.weight | (528, 88, 1, 1) | (528, 88) | 46464 | Matrix |
| blocks.4.0.bn1.weight | (528,) | (528,) | 528 | Vector |
| blocks.4.0.bn1.bias | (528,) | (528,) | 528 | Vector |
| blocks.4.0.conv_dw.weight | (528, 1, 3, 3) | (528, 3, 3) | 4752 | Tensor rank 3 |
| blocks.4.0.bn2.weight | (528,) | (528,) | 528 | Vector |
| blocks.4.0.bn2.bias | (528,) | (528,) | 528 | Vector |
| blocks.4.0.conv_pwl.weight | (136, 528, 1, 1) | (136, 528) | 71808 | Matrix |
| blocks.4.0.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.0.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.4.1.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.4.1.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.1.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.1.conv_dw.weight | (816, 1, 3, 3) | (816, 3, 3) | 7344 | Tensor rank 3 |
| blocks.4.1.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.1.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.1.conv_pwl.weight | (136, 816, 1, 1) | (136, 816) | 110976 | Matrix |
| blocks.4.1.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.1.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.4.2.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.4.2.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.2.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.2.conv_dw.weight | (816, 1, 3, 3) | (816, 3, 3) | 7344 | Tensor rank 3 |
| blocks.4.2.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.4.2.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.4.2.conv_pwl.weight | (136, 816, 1, 1) | (136, 816) | 110976 | Matrix |
| blocks.4.2.bn3.weight | (136,) | (136,) | 136 | Vector |
| blocks.4.2.bn3.bias | (136,) | (136,) | 136 | Vector |
| blocks.5.0.conv_pw.weight | (816, 136, 1, 1) | (816, 136) | 110976 | Matrix |
| blocks.5.0.bn1.weight | (816,) | (816,) | 816 | Vector |
| blocks.5.0.bn1.bias | (816,) | (816,) | 816 | Vector |
| blocks.5.0.conv_dw.weight | (816, 1, 3, 3) | (816, 3, 3) | 7344 | Tensor rank 3 |
| blocks.5.0.bn2.weight | (816,) | (816,) | 816 | Vector |
| blocks.5.0.bn2.bias | (816,) | (816,) | 816 | Vector |
| blocks.5.0.conv_pwl.weight | (224, 816, 1, 1) | (224, 816) | 182784 | Matrix |
| blocks.5.0.bn3.weight | (224,) | (224,) | 224 | Vector |
| blocks.5.0.bn3.bias | (224,) | (224,) | 224 | Vector |
| blocks.5.1.conv_pw.weight | (1344, 224, 1, 1) | (1344, 224) | 301056 | Matrix |
| blocks.5.1.bn1.weight | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.1.bn1.bias | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.1.conv_dw.weight | (1344, 1, 3, 3) | (1344, 3, 3) | 12096 | Tensor rank 3 |
| blocks.5.1.bn2.weight | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.1.bn2.bias | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.1.conv_pwl.weight | (224, 1344, 1, 1) | (224, 1344) | 301056 | Matrix |
| blocks.5.1.bn3.weight | (224,) | (224,) | 224 | Vector |
| blocks.5.1.bn3.bias | (224,) | (224,) | 224 | Vector |
| blocks.5.2.conv_pw.weight | (1344, 224, 1, 1) | (1344, 224) | 301056 | Matrix |
| blocks.5.2.bn1.weight | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.2.bn1.bias | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.2.conv_dw.weight | (1344, 1, 3, 3) | (1344, 3, 3) | 12096 | Tensor rank 3 |
| blocks.5.2.bn2.weight | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.2.bn2.bias | (1344,) | (1344,) | 1344 | Vector |
| blocks.5.2.conv_pwl.weight | (224, 1344, 1, 1) | (224, 1344) | 301056 | Matrix |
| blocks.5.2.bn3.weight | (224,) | (224,) | 224 | Vector |
| blocks.5.2.bn3.bias | (224,) | (224,) | 224 | Vector |
| blocks.6.0.conv_pw.weight | (1344, 224, 1, 1) | (1344, 224) | 301056 | Matrix |
| blocks.6.0.bn1.weight | (1344,) | (1344,) | 1344 | Vector |
| blocks.6.0.bn1.bias | (1344,) | (1344,) | 1344 | Vector |
| blocks.6.0.conv_dw.weight | (1344, 1, 3, 3) | (1344, 3, 3) | 12096 | Tensor rank 3 |
| blocks.6.0.bn2.weight | (1344,) | (1344,) | 1344 | Vector |
| blocks.6.0.bn2.bias | (1344,) | (1344,) | 1344 | Vector |
| blocks.6.0.conv_pwl.weight | (448, 1344, 1, 1) | (448, 1344) | 602112 | Matrix |
| blocks.6.0.bn3.weight | (448,) | (448,) | 448 | Vector |
| blocks.6.0.bn3.bias | (448,) | (448,) | 448 | Vector |
| conv_head.weight | (1792, 448, 1, 1) | (1792, 448) | 802816 | Matrix |
| bn2.weight | (1792,) | (1792,) | 1792 | Vector |
| bn2.bias | (1792,) | (1792,) | 1792 | Vector |
| classifier.weight | (1000, 1792) | (1000, 1792) | 1792000 | Matrix |
| classifier.bias | (1000,) | (1000,) | 1000 | Vector |

