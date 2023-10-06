# xlnet-base-cased parameter information

**Number of layers: [ 210 ]**

**Number of parameters: [ 447.504 MiB ] [Top <a href='../README.md'>3</a> ]**

**Number of trainable parameters: [ 447.504 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | Tensor rank 3 | 
|  --- | --- | --- |
| 35.71 | 30.00 | 34.29 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | Tensor rank 3 | 
|  --- | --- | --- |
| 0.07 | 69.74 | 30.18 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| transformer.mask_emb | (1, 1, 768) | (768,) | 768 | Vector |
| transformer.word_embedding.weight | (32000, 768) | (32000, 768) | 24576000 | Matrix |
| transformer.layer.0.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.0.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.0.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.0.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.0.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.0.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.0.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.0.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.0.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.0.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.0.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.0.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.0.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.0.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.0.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.0.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.0.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.1.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.1.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.1.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.1.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.1.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.1.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.1.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.1.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.1.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.1.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.1.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.1.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.1.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.1.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.1.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.1.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.1.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.2.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.2.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.2.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.2.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.2.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.2.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.2.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.2.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.2.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.2.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.2.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.2.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.2.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.2.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.2.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.2.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.2.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.3.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.3.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.3.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.3.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.3.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.3.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.3.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.3.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.3.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.3.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.3.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.3.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.3.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.3.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.3.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.3.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.3.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.4.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.4.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.4.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.4.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.4.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.4.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.4.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.4.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.4.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.4.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.4.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.4.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.4.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.4.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.4.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.4.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.4.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.5.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.5.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.5.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.5.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.5.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.5.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.5.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.5.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.5.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.5.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.5.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.5.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.5.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.5.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.5.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.5.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.5.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.6.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.6.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.6.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.6.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.6.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.6.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.6.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.6.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.6.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.6.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.6.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.6.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.6.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.6.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.6.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.6.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.6.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.7.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.7.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.7.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.7.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.7.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.7.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.7.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.7.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.7.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.7.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.7.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.7.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.7.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.7.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.7.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.7.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.7.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.8.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.8.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.8.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.8.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.8.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.8.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.8.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.8.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.8.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.8.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.8.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.8.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.8.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.8.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.8.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.8.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.8.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.9.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.9.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.9.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.9.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.9.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.9.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.9.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.9.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.9.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.9.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.9.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.9.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.9.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.9.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.9.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.9.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.9.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.10.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.10.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.10.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.10.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.10.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.10.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.10.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.10.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.10.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.10.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.10.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.10.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.10.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.10.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.10.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.10.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.10.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.11.rel_attn.q | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.11.rel_attn.k | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.11.rel_attn.v | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.11.rel_attn.o | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.11.rel_attn.r | (768, 12, 64) | (768, 12, 64) | 589824 | Tensor rank 3 |
| transformer.layer.11.rel_attn.r_r_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.11.rel_attn.r_s_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.11.rel_attn.r_w_bias | (12, 64) | (12, 64) | 768 | Matrix |
| transformer.layer.11.rel_attn.seg_embed | (2, 12, 64) | (2, 12, 64) | 1536 | Tensor rank 3 |
| transformer.layer.11.rel_attn.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.11.rel_attn.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.11.ff.layer_norm.weight | (768,) | (768,) | 768 | Vector |
| transformer.layer.11.ff.layer_norm.bias | (768,) | (768,) | 768 | Vector |
| transformer.layer.11.ff.layer_1.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| transformer.layer.11.ff.layer_1.bias | (3072,) | (3072,) | 3072 | Vector |
| transformer.layer.11.ff.layer_2.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| transformer.layer.11.ff.layer_2.bias | (768,) | (768,) | 768 | Vector |
| sequence_summary.summary.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| sequence_summary.summary.bias | (768,) | (768,) | 768 | Vector |
| logits_proj.weight | (2, 768) | (2, 768) | 1536 | Matrix |
| logits_proj.bias | (2,) | (2,) | 2 | Vector |

