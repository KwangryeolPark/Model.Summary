# albert-large-v2 parameter information

**Number of layers: [ 27 ]**

**Number of parameters: [ 67.467 MiB ] [Top <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 67.467 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | 
|  --- | --- |
| 55.56 | 44.44 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | 
|  --- | --- |
| 0.09 | 99.91 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| albert.embeddings.word_embeddings.weight | (30000, 128) | (30000, 128) | 3840000 | Matrix |
| albert.embeddings.position_embeddings.weight | (512, 128) | (512, 128) | 65536 | Matrix |
| albert.embeddings.token_type_embeddings.weight | (2, 128) | (2, 128) | 256 | Matrix |
| albert.embeddings.LayerNorm.weight | (128,) | (128,) | 128 | Vector |
| albert.embeddings.LayerNorm.bias | (128,) | (128,) | 128 | Vector |
| albert.encoder.embedding_hidden_mapping_in.weight | (1024, 128) | (1024, 128) | 131072 | Matrix |
| albert.encoder.embedding_hidden_mapping_in.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.full_layer_layer_norm.weight | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.full_layer_layer_norm.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.query.weight | (1024, 1024) | (1024, 1024) | 1048576 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.query.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.key.weight | (1024, 1024) | (1024, 1024) | 1048576 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.key.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.value.weight | (1024, 1024) | (1024, 1024) | 1048576 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.value.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.dense.weight | (1024, 1024) | (1024, 1024) | 1048576 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.dense.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.LayerNorm.weight | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.LayerNorm.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn.weight | (4096, 1024) | (4096, 1024) | 4194304 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn.bias | (4096,) | (4096,) | 4096 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn_output.weight | (1024, 4096) | (1024, 4096) | 4194304 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn_output.bias | (1024,) | (1024,) | 1024 | Vector |
| albert.pooler.weight | (1024, 1024) | (1024, 1024) | 1048576 | Matrix |
| albert.pooler.bias | (1024,) | (1024,) | 1024 | Vector |
| classifier.weight | (2, 1024) | (2, 1024) | 2048 | Matrix |
| classifier.bias | (2,) | (2,) | 2 | Vector |

