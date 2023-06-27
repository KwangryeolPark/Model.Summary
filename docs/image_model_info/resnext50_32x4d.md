# resnext50_32x4d parameter information

**Number of layers: [ 161 ]**

**Number of parameters: [ 25.03M ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 66.46 | 22.98 | 10.56 | 
**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 4 | 
|  --- | --- | --- |
| 0.28 | 94.03 | 5.69 | 

<img src="../figs/resnext50_32x4d_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| conv1.weight | (64, 3, 7, 7) | (64, 3, 7, 7) | 9408 | Tensor rank 4 |
| bn1.weight | (64,) | (64,) | 64 | Vector |
| bn1.bias | (64,) | (64,) | 64 | Vector |
| layer1.0.conv1.weight | (128, 64, 1, 1) | (128, 64) | 8192 | Matrix |
| layer1.0.bn1.weight | (128,) | (128,) | 128 | Vector |
| layer1.0.bn1.bias | (128,) | (128,) | 128 | Vector |
| layer1.0.conv2.weight | (128, 4, 3, 3) | (128, 4, 3, 3) | 4608 | Tensor rank 4 |
| layer1.0.bn2.weight | (128,) | (128,) | 128 | Vector |
| layer1.0.bn2.bias | (128,) | (128,) | 128 | Vector |
| layer1.0.conv3.weight | (256, 128, 1, 1) | (256, 128) | 32768 | Matrix |
| layer1.0.bn3.weight | (256,) | (256,) | 256 | Vector |
| layer1.0.bn3.bias | (256,) | (256,) | 256 | Vector |
| layer1.0.downsample.0.weight | (256, 64, 1, 1) | (256, 64) | 16384 | Matrix |
| layer1.0.downsample.1.weight | (256,) | (256,) | 256 | Vector |
| layer1.0.downsample.1.bias | (256,) | (256,) | 256 | Vector |
| layer1.1.conv1.weight | (128, 256, 1, 1) | (128, 256) | 32768 | Matrix |
| layer1.1.bn1.weight | (128,) | (128,) | 128 | Vector |
| layer1.1.bn1.bias | (128,) | (128,) | 128 | Vector |
| layer1.1.conv2.weight | (128, 4, 3, 3) | (128, 4, 3, 3) | 4608 | Tensor rank 4 |
| layer1.1.bn2.weight | (128,) | (128,) | 128 | Vector |
| layer1.1.bn2.bias | (128,) | (128,) | 128 | Vector |
| layer1.1.conv3.weight | (256, 128, 1, 1) | (256, 128) | 32768 | Matrix |
| layer1.1.bn3.weight | (256,) | (256,) | 256 | Vector |
| layer1.1.bn3.bias | (256,) | (256,) | 256 | Vector |
| layer1.2.conv1.weight | (128, 256, 1, 1) | (128, 256) | 32768 | Matrix |
| layer1.2.bn1.weight | (128,) | (128,) | 128 | Vector |
| layer1.2.bn1.bias | (128,) | (128,) | 128 | Vector |
| layer1.2.conv2.weight | (128, 4, 3, 3) | (128, 4, 3, 3) | 4608 | Tensor rank 4 |
| layer1.2.bn2.weight | (128,) | (128,) | 128 | Vector |
| layer1.2.bn2.bias | (128,) | (128,) | 128 | Vector |
| layer1.2.conv3.weight | (256, 128, 1, 1) | (256, 128) | 32768 | Matrix |
| layer1.2.bn3.weight | (256,) | (256,) | 256 | Vector |
| layer1.2.bn3.bias | (256,) | (256,) | 256 | Vector |
| layer2.0.conv1.weight | (256, 256, 1, 1) | (256, 256) | 65536 | Matrix |
| layer2.0.bn1.weight | (256,) | (256,) | 256 | Vector |
| layer2.0.bn1.bias | (256,) | (256,) | 256 | Vector |
| layer2.0.conv2.weight | (256, 8, 3, 3) | (256, 8, 3, 3) | 18432 | Tensor rank 4 |
| layer2.0.bn2.weight | (256,) | (256,) | 256 | Vector |
| layer2.0.bn2.bias | (256,) | (256,) | 256 | Vector |
| layer2.0.conv3.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| layer2.0.bn3.weight | (512,) | (512,) | 512 | Vector |
| layer2.0.bn3.bias | (512,) | (512,) | 512 | Vector |
| layer2.0.downsample.0.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| layer2.0.downsample.1.weight | (512,) | (512,) | 512 | Vector |
| layer2.0.downsample.1.bias | (512,) | (512,) | 512 | Vector |
| layer2.1.conv1.weight | (256, 512, 1, 1) | (256, 512) | 131072 | Matrix |
| layer2.1.bn1.weight | (256,) | (256,) | 256 | Vector |
| layer2.1.bn1.bias | (256,) | (256,) | 256 | Vector |
| layer2.1.conv2.weight | (256, 8, 3, 3) | (256, 8, 3, 3) | 18432 | Tensor rank 4 |
| layer2.1.bn2.weight | (256,) | (256,) | 256 | Vector |
| layer2.1.bn2.bias | (256,) | (256,) | 256 | Vector |
| layer2.1.conv3.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| layer2.1.bn3.weight | (512,) | (512,) | 512 | Vector |
| layer2.1.bn3.bias | (512,) | (512,) | 512 | Vector |
| layer2.2.conv1.weight | (256, 512, 1, 1) | (256, 512) | 131072 | Matrix |
| layer2.2.bn1.weight | (256,) | (256,) | 256 | Vector |
| layer2.2.bn1.bias | (256,) | (256,) | 256 | Vector |
| layer2.2.conv2.weight | (256, 8, 3, 3) | (256, 8, 3, 3) | 18432 | Tensor rank 4 |
| layer2.2.bn2.weight | (256,) | (256,) | 256 | Vector |
| layer2.2.bn2.bias | (256,) | (256,) | 256 | Vector |
| layer2.2.conv3.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| layer2.2.bn3.weight | (512,) | (512,) | 512 | Vector |
| layer2.2.bn3.bias | (512,) | (512,) | 512 | Vector |
| layer2.3.conv1.weight | (256, 512, 1, 1) | (256, 512) | 131072 | Matrix |
| layer2.3.bn1.weight | (256,) | (256,) | 256 | Vector |
| layer2.3.bn1.bias | (256,) | (256,) | 256 | Vector |
| layer2.3.conv2.weight | (256, 8, 3, 3) | (256, 8, 3, 3) | 18432 | Tensor rank 4 |
| layer2.3.bn2.weight | (256,) | (256,) | 256 | Vector |
| layer2.3.bn2.bias | (256,) | (256,) | 256 | Vector |
| layer2.3.conv3.weight | (512, 256, 1, 1) | (512, 256) | 131072 | Matrix |
| layer2.3.bn3.weight | (512,) | (512,) | 512 | Vector |
| layer2.3.bn3.bias | (512,) | (512,) | 512 | Vector |
| layer3.0.conv1.weight | (512, 512, 1, 1) | (512, 512) | 262144 | Matrix |
| layer3.0.bn1.weight | (512,) | (512,) | 512 | Vector |
| layer3.0.bn1.bias | (512,) | (512,) | 512 | Vector |
| layer3.0.conv2.weight | (512, 16, 3, 3) | (512, 16, 3, 3) | 73728 | Tensor rank 4 |
| layer3.0.bn2.weight | (512,) | (512,) | 512 | Vector |
| layer3.0.bn2.bias | (512,) | (512,) | 512 | Vector |
| layer3.0.conv3.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.0.bn3.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.0.bn3.bias | (1024,) | (1024,) | 1024 | Vector |
| layer3.0.downsample.0.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.0.downsample.1.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.0.downsample.1.bias | (1024,) | (1024,) | 1024 | Vector |
| layer3.1.conv1.weight | (512, 1024, 1, 1) | (512, 1024) | 524288 | Matrix |
| layer3.1.bn1.weight | (512,) | (512,) | 512 | Vector |
| layer3.1.bn1.bias | (512,) | (512,) | 512 | Vector |
| layer3.1.conv2.weight | (512, 16, 3, 3) | (512, 16, 3, 3) | 73728 | Tensor rank 4 |
| layer3.1.bn2.weight | (512,) | (512,) | 512 | Vector |
| layer3.1.bn2.bias | (512,) | (512,) | 512 | Vector |
| layer3.1.conv3.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.1.bn3.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.1.bn3.bias | (1024,) | (1024,) | 1024 | Vector |
| layer3.2.conv1.weight | (512, 1024, 1, 1) | (512, 1024) | 524288 | Matrix |
| layer3.2.bn1.weight | (512,) | (512,) | 512 | Vector |
| layer3.2.bn1.bias | (512,) | (512,) | 512 | Vector |
| layer3.2.conv2.weight | (512, 16, 3, 3) | (512, 16, 3, 3) | 73728 | Tensor rank 4 |
| layer3.2.bn2.weight | (512,) | (512,) | 512 | Vector |
| layer3.2.bn2.bias | (512,) | (512,) | 512 | Vector |
| layer3.2.conv3.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.2.bn3.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.2.bn3.bias | (1024,) | (1024,) | 1024 | Vector |
| layer3.3.conv1.weight | (512, 1024, 1, 1) | (512, 1024) | 524288 | Matrix |
| layer3.3.bn1.weight | (512,) | (512,) | 512 | Vector |
| layer3.3.bn1.bias | (512,) | (512,) | 512 | Vector |
| layer3.3.conv2.weight | (512, 16, 3, 3) | (512, 16, 3, 3) | 73728 | Tensor rank 4 |
| layer3.3.bn2.weight | (512,) | (512,) | 512 | Vector |
| layer3.3.bn2.bias | (512,) | (512,) | 512 | Vector |
| layer3.3.conv3.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.3.bn3.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.3.bn3.bias | (1024,) | (1024,) | 1024 | Vector |
| layer3.4.conv1.weight | (512, 1024, 1, 1) | (512, 1024) | 524288 | Matrix |
| layer3.4.bn1.weight | (512,) | (512,) | 512 | Vector |
| layer3.4.bn1.bias | (512,) | (512,) | 512 | Vector |
| layer3.4.conv2.weight | (512, 16, 3, 3) | (512, 16, 3, 3) | 73728 | Tensor rank 4 |
| layer3.4.bn2.weight | (512,) | (512,) | 512 | Vector |
| layer3.4.bn2.bias | (512,) | (512,) | 512 | Vector |
| layer3.4.conv3.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.4.bn3.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.4.bn3.bias | (1024,) | (1024,) | 1024 | Vector |
| layer3.5.conv1.weight | (512, 1024, 1, 1) | (512, 1024) | 524288 | Matrix |
| layer3.5.bn1.weight | (512,) | (512,) | 512 | Vector |
| layer3.5.bn1.bias | (512,) | (512,) | 512 | Vector |
| layer3.5.conv2.weight | (512, 16, 3, 3) | (512, 16, 3, 3) | 73728 | Tensor rank 4 |
| layer3.5.bn2.weight | (512,) | (512,) | 512 | Vector |
| layer3.5.bn2.bias | (512,) | (512,) | 512 | Vector |
| layer3.5.conv3.weight | (1024, 512, 1, 1) | (1024, 512) | 524288 | Matrix |
| layer3.5.bn3.weight | (1024,) | (1024,) | 1024 | Vector |
| layer3.5.bn3.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.0.conv1.weight | (1024, 1024, 1, 1) | (1024, 1024) | 1048576 | Matrix |
| layer4.0.bn1.weight | (1024,) | (1024,) | 1024 | Vector |
| layer4.0.bn1.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.0.conv2.weight | (1024, 32, 3, 3) | (1024, 32, 3, 3) | 294912 | Tensor rank 4 |
| layer4.0.bn2.weight | (1024,) | (1024,) | 1024 | Vector |
| layer4.0.bn2.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.0.conv3.weight | (2048, 1024, 1, 1) | (2048, 1024) | 2097152 | Matrix |
| layer4.0.bn3.weight | (2048,) | (2048,) | 2048 | Vector |
| layer4.0.bn3.bias | (2048,) | (2048,) | 2048 | Vector |
| layer4.0.downsample.0.weight | (2048, 1024, 1, 1) | (2048, 1024) | 2097152 | Matrix |
| layer4.0.downsample.1.weight | (2048,) | (2048,) | 2048 | Vector |
| layer4.0.downsample.1.bias | (2048,) | (2048,) | 2048 | Vector |
| layer4.1.conv1.weight | (1024, 2048, 1, 1) | (1024, 2048) | 2097152 | Matrix |
| layer4.1.bn1.weight | (1024,) | (1024,) | 1024 | Vector |
| layer4.1.bn1.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.1.conv2.weight | (1024, 32, 3, 3) | (1024, 32, 3, 3) | 294912 | Tensor rank 4 |
| layer4.1.bn2.weight | (1024,) | (1024,) | 1024 | Vector |
| layer4.1.bn2.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.1.conv3.weight | (2048, 1024, 1, 1) | (2048, 1024) | 2097152 | Matrix |
| layer4.1.bn3.weight | (2048,) | (2048,) | 2048 | Vector |
| layer4.1.bn3.bias | (2048,) | (2048,) | 2048 | Vector |
| layer4.2.conv1.weight | (1024, 2048, 1, 1) | (1024, 2048) | 2097152 | Matrix |
| layer4.2.bn1.weight | (1024,) | (1024,) | 1024 | Vector |
| layer4.2.bn1.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.2.conv2.weight | (1024, 32, 3, 3) | (1024, 32, 3, 3) | 294912 | Tensor rank 4 |
| layer4.2.bn2.weight | (1024,) | (1024,) | 1024 | Vector |
| layer4.2.bn2.bias | (1024,) | (1024,) | 1024 | Vector |
| layer4.2.conv3.weight | (2048, 1024, 1, 1) | (2048, 1024) | 2097152 | Matrix |
| layer4.2.bn3.weight | (2048,) | (2048,) | 2048 | Vector |
| layer4.2.bn3.bias | (2048,) | (2048,) | 2048 | Vector |
| fc.weight | (1000, 2048) | (1000, 2048) | 2048000 | Matrix |
| fc.bias | (1000,) | (1000,) | 1000 | Vector |

