# microsoft-resnet-34 parameter information

**Number of layers: [ 108 ]**

**Number of parameters: [ 81.195 MiB ] [ <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 81.195 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 66.67 | 2.78 | 30.56 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 0.08 | 0.81 | 99.11 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| embedder.embedder.convolution.weight | (64, 3, 7, 7) | (64, 3, 7, 7) | 9408 | Tensor rank 4 |
| embedder.embedder.normalization.weight | (64,) | (64,) | 64 | Vector |
| embedder.embedder.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.0.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.0.layer.0.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.0.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.1.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.0.layer.1.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.0.layer.1.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.0.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.1.layer.0.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.0.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.1.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.1.layer.1.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.1.layer.1.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.2.layer.0.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.2.layer.0.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.2.layer.0.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.2.layer.1.convolution.weight | (64, 64, 3, 3) | (64, 64, 3, 3) | 36864 | Tensor rank 4 |
| encoder.stages.0.layers.2.layer.1.normalization.weight | (64,) | (64,) | 64 | Vector |
| encoder.stages.0.layers.2.layer.1.normalization.bias | (64,) | (64,) | 64 | Vector |
| encoder.stages.1.layers.0.shortcut.convolution.weight | (128, 64, 1, 1) | (128, 64) | 8192 | Matrix |
| encoder.stages.1.layers.0.shortcut.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.shortcut.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.0.convolution.weight | (128, 64, 3, 3) | (128, 64, 3, 3) | 73728 | Tensor rank 4 |
| encoder.stages.1.layers.0.layer.0.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.0.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.1.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.0.layer.1.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.0.layer.1.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.0.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.1.layer.0.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.0.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.1.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.1.layer.1.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.1.layer.1.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.2.layer.0.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.2.layer.0.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.2.layer.0.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.2.layer.1.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.2.layer.1.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.2.layer.1.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.3.layer.0.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.3.layer.0.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.3.layer.0.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.3.layer.1.convolution.weight | (128, 128, 3, 3) | (128, 128, 3, 3) | 147456 | Tensor rank 4 |
| encoder.stages.1.layers.3.layer.1.normalization.weight | (128,) | (128,) | 128 | Vector |
| encoder.stages.1.layers.3.layer.1.normalization.bias | (128,) | (128,) | 128 | Vector |
| encoder.stages.2.layers.0.shortcut.convolution.weight | (256, 128, 1, 1) | (256, 128) | 32768 | Matrix |
| encoder.stages.2.layers.0.shortcut.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.shortcut.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.0.convolution.weight | (256, 128, 3, 3) | (256, 128, 3, 3) | 294912 | Tensor rank 4 |
| encoder.stages.2.layers.0.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.0.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.0.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.0.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.1.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.1.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.1.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.2.layer.0.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.2.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.2.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.2.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.2.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.2.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.3.layer.0.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.3.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.3.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.3.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.3.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.3.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.4.layer.0.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.4.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.4.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.4.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.4.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.4.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.5.layer.0.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.5.layer.0.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.5.layer.0.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.5.layer.1.convolution.weight | (256, 256, 3, 3) | (256, 256, 3, 3) | 589824 | Tensor rank 4 |
| encoder.stages.2.layers.5.layer.1.normalization.weight | (256,) | (256,) | 256 | Vector |
| encoder.stages.2.layers.5.layer.1.normalization.bias | (256,) | (256,) | 256 | Vector |
| encoder.stages.3.layers.0.shortcut.convolution.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| encoder.stages.3.layers.0.shortcut.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.shortcut.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.0.convolution.weight | (512, 256, 3, 3) | (512, 256, 3, 3) | 1179648 | Tensor rank 4 |
| encoder.stages.3.layers.0.layer.0.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.0.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.1.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.0.layer.1.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.0.layer.1.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.0.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.1.layer.0.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.0.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.1.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.1.layer.1.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.1.layer.1.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.2.layer.0.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.2.layer.0.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.2.layer.0.normalization.bias | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.2.layer.1.convolution.weight | (512, 512, 3, 3) | (512, 512, 3, 3) | 2359296 | Tensor rank 4 |
| encoder.stages.3.layers.2.layer.1.normalization.weight | (512,) | (512,) | 512 | Vector |
| encoder.stages.3.layers.2.layer.1.normalization.bias | (512,) | (512,) | 512 | Vector |

