# microsoft-resnet-26 parameter information

**Number of layers: [ 87 ]**

**Number of parameters: [ 53.200 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 53.200 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 66.67 | 22.99 | 10.34 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 0.22 | 54.78 | 45.00 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| embedder.embedder.convolution.weight | (64, 3, 7, 7) | (64, 3, 7, 7) | 9408 | Tensor rank 4 |
| embedder.embedder.normalization.weight | (64,) | (64,) | 64 | Vector |
| embedder.embedder.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.shortcut.convolution.weight | (256, 64, 1, 1) | (256, 64) | 16384 | Matrix |
| encoder.stages.0.layers.0.shortcut.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.0.layers.0.shortcut.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.0.layers.0.layer.0.convolution.weight | (64, 64, 1, 1) | (64, 64) | 4096 | Matrix |
| encoder.stages.0.layers.0.layer.0.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.0.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.1.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.0.layer.1.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.1.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.2.convolution.weight | (256, 64, 1, 1) | (256, 64) | 16384 | Matrix |
| encoder.stages.0.layers.0.layer.2.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.0.layers.0.layer.2.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.0.layers.1.layer.0.convolution.weight | (64, 256, 1, 1) | (64, 256) | 16384 | Matrix |
| encoder.stages.0.layers.1.layer.0.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.0.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.1.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.1.layer.1.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.1.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.2.convolution.weight | (256, 64, 1, 1) | (256, 64) | 16384 | Matrix |
| encoder.stages.0.layers.1.layer.2.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.0.layers.1.layer.2.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.1.layers.0.shortcut.convolution.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| encoder.stages.1.layers.0.shortcut.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.1.layers.0.shortcut.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.1.layers.0.layer.0.convolution.weight | (128, 256, 1, 1) | (128, 256) | 32768 | Matrix |
| encoder.stages.1.layers.0.layer.0.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.0.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.1.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.0.layer.1.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.1.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.2.convolution.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| encoder.stages.1.layers.0.layer.2.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.1.layers.0.layer.2.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.1.layers.1.layer.0.convolution.weight | (128, 512, 1, 1) | (128, 512) | 65536 | Matrix |
| encoder.stages.1.layers.1.layer.0.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.0.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.1.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.1.layer.1.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.1.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.2.convolution.weight | (512, 128, 1, 1) | (512, 128) | 65536 | Matrix |
| encoder.stages.1.layers.1.layer.2.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.1.layers.1.layer.2.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.2.layers.0.shortcut.convolution.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| encoder.stages.2.layers.0.shortcut.normalization.weight | (1024,) | (1024,) | 1024 | Vector |
| encoder.stages.2.layers.0.shortcut.normalization.bias | (1024,) | (1024,) | 1024 | Vector |
| encoder.stages.2.layers.0.layer.0.convolution.weight | (256, 512, 1, 1) | (256, 512) | 131072 | Matrix |
| encoder.stages.2.layers.0.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.0.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.2.convolution.weight | (1024, 256, 1, 1) | (1024, 256) | 262144 | Matrix |
| encoder.stages.2.layers.0.layer.2.normalization.weight | (1024,) | (1024,) | 1024 | Vector |
| encoder.stages.2.layers.0.layer.2.normalization.bias | (1024,) | (1024,) | 1024 | Vector |
| encoder.stages.2.layers.1.layer.0.convolution.weight | (256, 1024, 1, 1) | (256, 1024) | 262144 | Matrix |
| encoder.stages.2.layers.1.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.1.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.2.convolution.weight | (1024, 256, 1, 1) | (1024, 256) | 262144 | Matrix |
| encoder.stages.2.layers.1.layer.2.normalization.weight | (1024,) | (1024,) | 1024 | Vector |
| encoder.stages.2.layers.1.layer.2.normalization.bias | (1024,) | (1024,) | 1024 | Vector |
| encoder.stages.3.layers.0.shortcut.convolution.weight | (2048, 1024, 1, 1) | (2048, 1024) | 2097152 | Matrix |
| encoder.stages.3.layers.0.shortcut.normalization.weight | (2048,) | (2048,) | 2048 | Vector |
| encoder.stages.3.layers.0.shortcut.normalization.bias | (2048,) | (2048,) | 2048 | Vector |
| encoder.stages.3.layers.0.layer.0.convolution.weight | (512, 1024, 1, 1) | (512, 1024) | 524288 | Matrix |
| encoder.stages.3.layers.0.layer.0.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.0.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.1.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.0.layer.1.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.1.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.2.convolution.weight | (2048, 512, 1, 1) | (2048, 512) | 1048576 | Matrix |
| encoder.stages.3.layers.0.layer.2.normalization.weight | (2048,) | (2048,) | 2048 | Vector |
| encoder.stages.3.layers.0.layer.2.normalization.bias | (2048,) | (2048,) | 2048 | Vector |
| encoder.stages.3.layers.1.layer.0.convolution.weight | (512, 2048, 1, 1) | (512, 2048) | 1048576 | Matrix |
| encoder.stages.3.layers.1.layer.0.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.0.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.1.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.1.layer.1.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.1.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.2.convolution.weight | (2048, 512, 1, 1) | (2048, 512) | 1048576 | Matrix |
| encoder.stages.3.layers.1.layer.2.normalization.weight | (2048,) | (2048,) | 2048 | Vector |
| encoder.stages.3.layers.1.layer.2.normalization.bias | (2048,) | (2048,) | 2048 | Vector |

