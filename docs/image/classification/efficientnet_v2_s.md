# efficientnet_v2_s parameter information

**Number of layers: [ 452 ]**

**Number of parameters: [ 81.858 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 81.858 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 62.17 | 28.76 | 6.64 | 2.43 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | Tensor rank 4 | 
|  --- | --- | --- | --- |
| 0.89 | 93.94 | 1.41 | 3.76 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| features.0.0.weight | (24, 3, 3, 3) | (24, 3, 3, 3) | 648 | Tensor rank 4 |
| features.0.1.weight | (24,) | (24,) | 24 | Vector |
| features.0.1.bias | (24,) | (24,) | 24 | Vector |
| features.1.0.block.0.0.weight | (24, 24, 3, 3) | (24, 24, 3, 3) | 5184 | Tensor rank 4 |
| features.1.0.block.0.1.weight | (24,) | (24,) | 24 | Vector |
| features.1.0.block.0.1.bias | (24,) | (24,) | 24 | Vector |
| features.1.1.block.0.0.weight | (24, 24, 3, 3) | (24, 24, 3, 3) | 5184 | Tensor rank 4 |
| features.1.1.block.0.1.weight | (24,) | (24,) | 24 | Vector |
| features.1.1.block.0.1.bias | (24,) | (24,) | 24 | Vector |
| features.2.0.block.0.0.weight | (96, 24, 3, 3) | (96, 24, 3, 3) | 20736 | Tensor rank 4 |
| features.2.0.block.0.1.weight | (96,) | (96,) | 96 | Vector |
| features.2.0.block.0.1.bias | (96,) | (96,) | 96 | Vector |
| features.2.0.block.1.0.weight | (48, 96, 1, 1) | (48, 96) | 4608 | Matrix |
| features.2.0.block.1.1.weight | (48,) | (48,) | 48 | Vector |
| features.2.0.block.1.1.bias | (48,) | (48,) | 48 | Vector |
| features.2.1.block.0.0.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| features.2.1.block.0.1.weight | (192,) | (192,) | 192 | Vector |
| features.2.1.block.0.1.bias | (192,) | (192,) | 192 | Vector |
| features.2.1.block.1.0.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| features.2.1.block.1.1.weight | (48,) | (48,) | 48 | Vector |
| features.2.1.block.1.1.bias | (48,) | (48,) | 48 | Vector |
| features.2.2.block.0.0.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| features.2.2.block.0.1.weight | (192,) | (192,) | 192 | Vector |
| features.2.2.block.0.1.bias | (192,) | (192,) | 192 | Vector |
| features.2.2.block.1.0.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| features.2.2.block.1.1.weight | (48,) | (48,) | 48 | Vector |
| features.2.2.block.1.1.bias | (48,) | (48,) | 48 | Vector |
| features.2.3.block.0.0.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| features.2.3.block.0.1.weight | (192,) | (192,) | 192 | Vector |
| features.2.3.block.0.1.bias | (192,) | (192,) | 192 | Vector |
| features.2.3.block.1.0.weight | (48, 192, 1, 1) | (48, 192) | 9216 | Matrix |
| features.2.3.block.1.1.weight | (48,) | (48,) | 48 | Vector |
| features.2.3.block.1.1.bias | (48,) | (48,) | 48 | Vector |
| features.3.0.block.0.0.weight | (192, 48, 3, 3) | (192, 48, 3, 3) | 82944 | Tensor rank 4 |
| features.3.0.block.0.1.weight | (192,) | (192,) | 192 | Vector |
| features.3.0.block.0.1.bias | (192,) | (192,) | 192 | Vector |
| features.3.0.block.1.0.weight | (64, 192, 1, 1) | (64, 192) | 12288 | Matrix |
| features.3.0.block.1.1.weight | (64,) | (64,) | 64 | Vector |
| features.3.0.block.1.1.bias | (64,) | (64,) | 64 | Vector |
| features.3.1.block.0.0.weight | (256, 64, 3, 3) | (256, 64, 3, 3) | 147456 | Tensor rank 4 |
| features.3.1.block.0.1.weight | (256,) | (256,) | 256 | Vector |
| features.3.1.block.0.1.bias | (256,) | (256,) | 256 | Vector |
| features.3.1.block.1.0.weight | (64, 256, 1, 1) | (64, 256) | 16384 | Matrix |
| features.3.1.block.1.1.weight | (64,) | (64,) | 64 | Vector |
| features.3.1.block.1.1.bias | (64,) | (64,) | 64 | Vector |
| features.3.2.block.0.0.weight | (256, 64, 3, 3) | (256, 64, 3, 3) | 147456 | Tensor rank 4 |
| features.3.2.block.0.1.weight | (256,) | (256,) | 256 | Vector |
| features.3.2.block.0.1.bias | (256,) | (256,) | 256 | Vector |
| features.3.2.block.1.0.weight | (64, 256, 1, 1) | (64, 256) | 16384 | Matrix |
| features.3.2.block.1.1.weight | (64,) | (64,) | 64 | Vector |
| features.3.2.block.1.1.bias | (64,) | (64,) | 64 | Vector |
| features.3.3.block.0.0.weight | (256, 64, 3, 3) | (256, 64, 3, 3) | 147456 | Tensor rank 4 |
| features.3.3.block.0.1.weight | (256,) | (256,) | 256 | Vector |
| features.3.3.block.0.1.bias | (256,) | (256,) | 256 | Vector |
| features.3.3.block.1.0.weight | (64, 256, 1, 1) | (64, 256) | 16384 | Matrix |
| features.3.3.block.1.1.weight | (64,) | (64,) | 64 | Vector |
| features.3.3.block.1.1.bias | (64,) | (64,) | 64 | Vector |
| features.4.0.block.0.0.weight | (256, 64, 1, 1) | (256, 64) | 16384 | Matrix |
| features.4.0.block.0.1.weight | (256,) | (256,) | 256 | Vector |
| features.4.0.block.0.1.bias | (256,) | (256,) | 256 | Vector |
| features.4.0.block.1.0.weight | (256, 1, 3, 3) | (256, 3, 3) | 2304 | Tensor rank 3 |
| features.4.0.block.1.1.weight | (256,) | (256,) | 256 | Vector |
| features.4.0.block.1.1.bias | (256,) | (256,) | 256 | Vector |
| features.4.0.block.2.fc1.weight | (16, 256, 1, 1) | (16, 256) | 4096 | Matrix |
| features.4.0.block.2.fc1.bias | (16,) | (16,) | 16 | Vector |
| features.4.0.block.2.fc2.weight | (256, 16, 1, 1) | (256, 16) | 4096 | Matrix |
| features.4.0.block.2.fc2.bias | (256,) | (256,) | 256 | Vector |
| features.4.0.block.3.0.weight | (128, 256, 1, 1) | (128, 256) | 32768 | Matrix |
| features.4.0.block.3.1.weight | (128,) | (128,) | 128 | Vector |
| features.4.0.block.3.1.bias | (128,) | (128,) | 128 | Vector |
| features.4.1.block.0.0.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| features.4.1.block.0.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.1.block.0.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.1.block.1.0.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| features.4.1.block.1.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.1.block.1.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.1.block.2.fc1.weight | (32, 512, 1, 1) | (32, 512) | 16384 | Matrix |
| features.4.1.block.2.fc1.bias | (32,) | (32,) | 32 | Vector |
| features.4.1.block.2.fc2.weight | (512, 32, 1, 1) | (512, 32) | 16384 | Matrix |
| features.4.1.block.2.fc2.bias | (512,) | (512,) | 512 | Vector |
| features.4.1.block.3.0.weight | (128, 512, 1, 1) | (128, 512) | 65536 | Matrix |
| features.4.1.block.3.1.weight | (128,) | (128,) | 128 | Vector |
| features.4.1.block.3.1.bias | (128,) | (128,) | 128 | Vector |
| features.4.2.block.0.0.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| features.4.2.block.0.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.2.block.0.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.2.block.1.0.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| features.4.2.block.1.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.2.block.1.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.2.block.2.fc1.weight | (32, 512, 1, 1) | (32, 512) | 16384 | Matrix |
| features.4.2.block.2.fc1.bias | (32,) | (32,) | 32 | Vector |
| features.4.2.block.2.fc2.weight | (512, 32, 1, 1) | (512, 32) | 16384 | Matrix |
| features.4.2.block.2.fc2.bias | (512,) | (512,) | 512 | Vector |
| features.4.2.block.3.0.weight | (128, 512, 1, 1) | (128, 512) | 65536 | Matrix |
| features.4.2.block.3.1.weight | (128,) | (128,) | 128 | Vector |
| features.4.2.block.3.1.bias | (128,) | (128,) | 128 | Vector |
| features.4.3.block.0.0.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| features.4.3.block.0.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.3.block.0.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.3.block.1.0.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| features.4.3.block.1.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.3.block.1.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.3.block.2.fc1.weight | (32, 512, 1, 1) | (32, 512) | 16384 | Matrix |
| features.4.3.block.2.fc1.bias | (32,) | (32,) | 32 | Vector |
| features.4.3.block.2.fc2.weight | (512, 32, 1, 1) | (512, 32) | 16384 | Matrix |
| features.4.3.block.2.fc2.bias | (512,) | (512,) | 512 | Vector |
| features.4.3.block.3.0.weight | (128, 512, 1, 1) | (128, 512) | 65536 | Matrix |
| features.4.3.block.3.1.weight | (128,) | (128,) | 128 | Vector |
| features.4.3.block.3.1.bias | (128,) | (128,) | 128 | Vector |
| features.4.4.block.0.0.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| features.4.4.block.0.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.4.block.0.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.4.block.1.0.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| features.4.4.block.1.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.4.block.1.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.4.block.2.fc1.weight | (32, 512, 1, 1) | (32, 512) | 16384 | Matrix |
| features.4.4.block.2.fc1.bias | (32,) | (32,) | 32 | Vector |
| features.4.4.block.2.fc2.weight | (512, 32, 1, 1) | (512, 32) | 16384 | Matrix |
| features.4.4.block.2.fc2.bias | (512,) | (512,) | 512 | Vector |
| features.4.4.block.3.0.weight | (128, 512, 1, 1) | (128, 512) | 65536 | Matrix |
| features.4.4.block.3.1.weight | (128,) | (128,) | 128 | Vector |
| features.4.4.block.3.1.bias | (128,) | (128,) | 128 | Vector |
| features.4.5.block.0.0.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| features.4.5.block.0.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.5.block.0.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.5.block.1.0.weight | (512, 1, 3, 3) | (512, 3, 3) | 4608 | Tensor rank 3 |
| features.4.5.block.1.1.weight | (512,) | (512,) | 512 | Vector |
| features.4.5.block.1.1.bias | (512,) | (512,) | 512 | Vector |
| features.4.5.block.2.fc1.weight | (32, 512, 1, 1) | (32, 512) | 16384 | Matrix |
| features.4.5.block.2.fc1.bias | (32,) | (32,) | 32 | Vector |
| features.4.5.block.2.fc2.weight | (512, 32, 1, 1) | (512, 32) | 16384 | Matrix |
| features.4.5.block.2.fc2.bias | (512,) | (512,) | 512 | Vector |
| features.4.5.block.3.0.weight | (128, 512, 1, 1) | (128, 512) | 65536 | Matrix |
| features.4.5.block.3.1.weight | (128,) | (128,) | 128 | Vector |
| features.4.5.block.3.1.bias | (128,) | (128,) | 128 | Vector |
| features.5.0.block.0.0.weight | (768, 128, 1, 1) | (768, 128) | 98304 | Matrix |
| features.5.0.block.0.1.weight | (768,) | (768,) | 768 | Vector |
| features.5.0.block.0.1.bias | (768,) | (768,) | 768 | Vector |
| features.5.0.block.1.0.weight | (768, 1, 3, 3) | (768, 3, 3) | 6912 | Tensor rank 3 |
| features.5.0.block.1.1.weight | (768,) | (768,) | 768 | Vector |
| features.5.0.block.1.1.bias | (768,) | (768,) | 768 | Vector |
| features.5.0.block.2.fc1.weight | (32, 768, 1, 1) | (32, 768) | 24576 | Matrix |
| features.5.0.block.2.fc1.bias | (32,) | (32,) | 32 | Vector |
| features.5.0.block.2.fc2.weight | (768, 32, 1, 1) | (768, 32) | 24576 | Matrix |
| features.5.0.block.2.fc2.bias | (768,) | (768,) | 768 | Vector |
| features.5.0.block.3.0.weight | (160, 768, 1, 1) | (160, 768) | 122880 | Matrix |
| features.5.0.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.0.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.1.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.1.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.1.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.1.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.1.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.1.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.1.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.1.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.1.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.1.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.1.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.1.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.1.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.2.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.2.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.2.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.2.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.2.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.2.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.2.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.2.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.2.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.2.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.2.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.2.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.2.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.3.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.3.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.3.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.3.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.3.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.3.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.3.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.3.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.3.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.3.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.3.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.3.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.3.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.4.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.4.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.4.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.4.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.4.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.4.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.4.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.4.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.4.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.4.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.4.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.4.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.4.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.5.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.5.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.5.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.5.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.5.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.5.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.5.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.5.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.5.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.5.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.5.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.5.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.5.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.6.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.6.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.6.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.6.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.6.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.6.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.6.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.6.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.6.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.6.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.6.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.6.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.6.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.7.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.7.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.7.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.7.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.7.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.7.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.7.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.7.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.7.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.7.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.7.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.7.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.7.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.5.8.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.5.8.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.8.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.8.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.5.8.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.5.8.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.5.8.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.5.8.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.5.8.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.5.8.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.5.8.block.3.0.weight | (160, 960, 1, 1) | (160, 960) | 153600 | Matrix |
| features.5.8.block.3.1.weight | (160,) | (160,) | 160 | Vector |
| features.5.8.block.3.1.bias | (160,) | (160,) | 160 | Vector |
| features.6.0.block.0.0.weight | (960, 160, 1, 1) | (960, 160) | 153600 | Matrix |
| features.6.0.block.0.1.weight | (960,) | (960,) | 960 | Vector |
| features.6.0.block.0.1.bias | (960,) | (960,) | 960 | Vector |
| features.6.0.block.1.0.weight | (960, 1, 3, 3) | (960, 3, 3) | 8640 | Tensor rank 3 |
| features.6.0.block.1.1.weight | (960,) | (960,) | 960 | Vector |
| features.6.0.block.1.1.bias | (960,) | (960,) | 960 | Vector |
| features.6.0.block.2.fc1.weight | (40, 960, 1, 1) | (40, 960) | 38400 | Matrix |
| features.6.0.block.2.fc1.bias | (40,) | (40,) | 40 | Vector |
| features.6.0.block.2.fc2.weight | (960, 40, 1, 1) | (960, 40) | 38400 | Matrix |
| features.6.0.block.2.fc2.bias | (960,) | (960,) | 960 | Vector |
| features.6.0.block.3.0.weight | (256, 960, 1, 1) | (256, 960) | 245760 | Matrix |
| features.6.0.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.0.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.1.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.1.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.1.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.1.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.1.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.1.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.1.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.1.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.1.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.1.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.1.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.1.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.1.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.2.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.2.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.2.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.2.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.2.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.2.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.2.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.2.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.2.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.2.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.2.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.2.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.2.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.3.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.3.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.3.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.3.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.3.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.3.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.3.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.3.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.3.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.3.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.3.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.3.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.3.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.4.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.4.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.4.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.4.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.4.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.4.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.4.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.4.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.4.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.4.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.4.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.4.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.4.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.5.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.5.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.5.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.5.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.5.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.5.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.5.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.5.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.5.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.5.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.5.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.5.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.5.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.6.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.6.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.6.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.6.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.6.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.6.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.6.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.6.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.6.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.6.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.6.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.6.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.6.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.7.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.7.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.7.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.7.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.7.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.7.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.7.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.7.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.7.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.7.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.7.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.7.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.7.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.8.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.8.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.8.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.8.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.8.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.8.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.8.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.8.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.8.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.8.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.8.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.8.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.8.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.9.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.9.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.9.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.9.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.9.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.9.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.9.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.9.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.9.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.9.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.9.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.9.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.9.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.10.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.10.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.10.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.10.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.10.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.10.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.10.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.10.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.10.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.10.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.10.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.10.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.10.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.11.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.11.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.11.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.11.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.11.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.11.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.11.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.11.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.11.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.11.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.11.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.11.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.11.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.12.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.12.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.12.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.12.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.12.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.12.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.12.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.12.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.12.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.12.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.12.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.12.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.12.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.13.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.13.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.13.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.13.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.13.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.13.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.13.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.13.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.13.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.13.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.13.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.13.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.13.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.6.14.block.0.0.weight | (1536, 256, 1, 1) | (1536, 256) | 393216 | Matrix |
| features.6.14.block.0.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.14.block.0.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.14.block.1.0.weight | (1536, 1, 3, 3) | (1536, 3, 3) | 13824 | Tensor rank 3 |
| features.6.14.block.1.1.weight | (1536,) | (1536,) | 1536 | Vector |
| features.6.14.block.1.1.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.14.block.2.fc1.weight | (64, 1536, 1, 1) | (64, 1536) | 98304 | Matrix |
| features.6.14.block.2.fc1.bias | (64,) | (64,) | 64 | Vector |
| features.6.14.block.2.fc2.weight | (1536, 64, 1, 1) | (1536, 64) | 98304 | Matrix |
| features.6.14.block.2.fc2.bias | (1536,) | (1536,) | 1536 | Vector |
| features.6.14.block.3.0.weight | (256, 1536, 1, 1) | (256, 1536) | 393216 | Matrix |
| features.6.14.block.3.1.weight | (256,) | (256,) | 256 | Vector |
| features.6.14.block.3.1.bias | (256,) | (256,) | 256 | Vector |
| features.7.0.weight | (1280, 256, 1, 1) | (1280, 256) | 327680 | Matrix |
| features.7.1.weight | (1280,) | (1280,) | 1280 | Vector |
| features.7.1.bias | (1280,) | (1280,) | 1280 | Vector |
| classifier.1.weight | (1000, 1280) | (1000, 1280) | 1280000 | Matrix |
| classifier.1.bias | (1000,) | (1000,) | 1000 | Vector |

