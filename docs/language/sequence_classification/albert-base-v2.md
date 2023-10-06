# albert-base-v2 parameter information

**Number of layers: [ 27 ]**

**Number of parameters: [ 44.575 MiB ] [Top <a href='./README.md'>Check rank</a> ]**

**Number of trainable parameters: [ 44.575 MiB ]**

**Proportional of each form** (%)

| Vector | Matrix | 
|  --- | --- |
| 55.56 | 44.44 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | 
|  --- | --- |
| 0.10 | 99.90 | 

# Layer information


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| albert.embeddings.word_embeddings.weight | (30000, 128) | (30000, 128) | 3840000 | Matrix |
| albert.embeddings.position_embeddings.weight | (512, 128) | (512, 128) | 65536 | Matrix |
| albert.embeddings.token_type_embeddings.weight | (2, 128) | (2, 128) | 256 | Matrix |
| albert.embeddings.LayerNorm.weight | (128,) | (128,) | 128 | Vector |
| albert.embeddings.LayerNorm.bias | (128,) | (128,) | 128 | Vector |
| albert.encoder.embedding_hidden_mapping_in.weight | (768, 128) | (768, 128) | 98304 | Matrix |
| albert.encoder.embedding_hidden_mapping_in.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.full_layer_layer_norm.weight | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.full_layer_layer_norm.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.query.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.key.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.value.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.dense.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.attention.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn.bias | (3072,) | (3072,) | 3072 | Vector |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn_output.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| albert.encoder.albert_layer_groups.0.albert_layers.0.ffn_output.bias | (768,) | (768,) | 768 | Vector |
| albert.pooler.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| albert.pooler.bias | (768,) | (768,) | 768 | Vector |
| classifier.weight | (2, 768) | (2, 768) | 1536 | Matrix |
| classifier.bias | (2,) | (2,) | 2 | Vector |

