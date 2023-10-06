# xlnet-large-cased parameter information

**Number of layers: [ 414 ]**

**Number of parameters: [ 1.346 GiB ] [Top <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 1.346 GiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | 
|  --- | --- | --- |
| 35.51 | 29.71 | 34.78 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | 
|  --- | --- | --- |
| 0.06 | 65.10 | 34.84 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| transformer.mask_emb | (1, 1, 1024) | (1024,) | 1024 | Vector |
| transformer.word_embedding.weight | (32000, 1024) | (32000, 1024) | 32768000 | Matrix |
| transformer.layer.0.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.0.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.0.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.0.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.0.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.0.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.0.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.0.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.0.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.0.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.0.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.0.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.0.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.0.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.0.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.0.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.0.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.1.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.1.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.1.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.1.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.1.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.1.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.1.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.1.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.1.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.1.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.1.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.1.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.1.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.1.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.1.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.1.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.1.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.2.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.2.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.2.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.2.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.2.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.2.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.2.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.2.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.2.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.2.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.2.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.2.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.2.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.2.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.2.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.2.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.2.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.3.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.3.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.3.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.3.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.3.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.3.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.3.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.3.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.3.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.3.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.3.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.3.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.3.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.3.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.3.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.3.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.3.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.4.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.4.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.4.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.4.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.4.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.4.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.4.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.4.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.4.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.4.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.4.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.4.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.4.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.4.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.4.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.4.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.4.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.5.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.5.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.5.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.5.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.5.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.5.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.5.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.5.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.5.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.5.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.5.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.5.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.5.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.5.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.5.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.5.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.5.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.6.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.6.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.6.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.6.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.6.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.6.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.6.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.6.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.6.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.6.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.6.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.6.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.6.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.6.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.6.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.6.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.6.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.7.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.7.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.7.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.7.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.7.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.7.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.7.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.7.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.7.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.7.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.7.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.7.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.7.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.7.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.7.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.7.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.7.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.8.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.8.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.8.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.8.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.8.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.8.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.8.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.8.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.8.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.8.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.8.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.8.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.8.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.8.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.8.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.8.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.8.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.9.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.9.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.9.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.9.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.9.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.9.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.9.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.9.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.9.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.9.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.9.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.9.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.9.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.9.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.9.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.9.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.9.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.10.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.10.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.10.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.10.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.10.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.10.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.10.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.10.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.10.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.10.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.10.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.10.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.10.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.10.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.10.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.10.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.10.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.11.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.11.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.11.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.11.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.11.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.11.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.11.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.11.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.11.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.11.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.11.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.11.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.11.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.11.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.11.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.11.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.11.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.12.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.12.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.12.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.12.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.12.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.12.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.12.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.12.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.12.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.12.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.12.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.12.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.12.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.12.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.12.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.12.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.12.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.13.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.13.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.13.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.13.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.13.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.13.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.13.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.13.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.13.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.13.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.13.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.13.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.13.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.13.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.13.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.13.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.13.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.14.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.14.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.14.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.14.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.14.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.14.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.14.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.14.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.14.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.14.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.14.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.14.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.14.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.14.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.14.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.14.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.14.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.15.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.15.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.15.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.15.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.15.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.15.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.15.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.15.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.15.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.15.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.15.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.15.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.15.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.15.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.15.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.15.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.15.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.16.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.16.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.16.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.16.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.16.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.16.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.16.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.16.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.16.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.16.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.16.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.16.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.16.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.16.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.16.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.16.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.16.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.17.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.17.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.17.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.17.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.17.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.17.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.17.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.17.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.17.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.17.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.17.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.17.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.17.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.17.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.17.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.17.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.17.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.18.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.18.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.18.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.18.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.18.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.18.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.18.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.18.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.18.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.18.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.18.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.18.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.18.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.18.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.18.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.18.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.18.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.19.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.19.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.19.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.19.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.19.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.19.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.19.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.19.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.19.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.19.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.19.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.19.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.19.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.19.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.19.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.19.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.19.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.20.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.20.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.20.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.20.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.20.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.20.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.20.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.20.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.20.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.20.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.20.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.20.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.20.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.20.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.20.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.20.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.20.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.21.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.21.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.21.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.21.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.21.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.21.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.21.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.21.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.21.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.21.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.21.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.21.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.21.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.21.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.21.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.21.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.21.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.22.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.22.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.22.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.22.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.22.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.22.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.22.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.22.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.22.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.22.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.22.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.22.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.22.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.22.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.22.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.22.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.22.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.23.rel_attn.q | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.23.rel_attn.k | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.23.rel_attn.v | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.23.rel_attn.o | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.23.rel_attn.r | (1024, 16, 64) | (1024, 16, 64) | 1048576 | Tensor rank 3 |
| transformer.layer.23.rel_attn.r_r_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.23.rel_attn.r_s_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.23.rel_attn.r_w_bias | (16, 64) | (16, 64) | 1024 | Matrix |
| transformer.layer.23.rel_attn.seg_embed | (2, 16, 64) | (2, 16, 64) | 2048 | Tensor rank 3 |
| transformer.layer.23.rel_attn.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.23.rel_attn.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.23.ff.layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.23.ff.layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| transformer.layer.23.ff.layer_1.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| transformer.layer.23.ff.layer_1.bias | (4096,) | (4096,) | 4096 | Vector |
| transformer.layer.23.ff.layer_2.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| transformer.layer.23.ff.layer_2.bias | (1024,) | (1024,) | 1024 | Vector |
| sequence_summary.summary.weight | (1024, 1024) | (1024, 1024) | 1048576 | Matrix |
| sequence_summary.summary.bias | (1024,) | (1024,) | 1024 | Vector |
| logits_proj.weight | (2, 1024) | (2, 1024) | 2048 | Matrix |
| logits_proj.bias | (2,) | (2,) | 2 | Vector |

