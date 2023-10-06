# bert parameter information

**Number of layers: [ 199 ]**

**Number of parameters: [ 109.48M ]**

**Proportional of each form** (%)

| Vector | Matrix | 
|  --- | --- |
| 61.81 | 38.19 | 

**Proportional of parameters by form** (%)


| Vector | Matrix | 
|  --- | --- |
| 0.11 | 99.89 | 

<img src="../figs/bert_pie_chart.png" alt="pie_chart" width="500"/>

**Layer information**


| Name | Shape | Squeezed shape | Number of parameters | Form |
| --- | --- | --- | --- | --- |
| embeddings.word_embeddings.weight | (30522, 768) | (30522, 768) | 23440896 | Matrix |
| embeddings.position_embeddings.weight | (512, 768) | (512, 768) | 393216 | Matrix |
| embeddings.token_type_embeddings.weight | (2, 768) | (2, 768) | 1536 | Matrix |
| embeddings.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| embeddings.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.0.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.0.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.0.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.0.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.0.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.0.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.0.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.0.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.1.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.1.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.1.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.1.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.1.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.1.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.1.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.1.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.2.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.2.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.2.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.2.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.2.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.2.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.2.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.2.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.3.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.3.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.3.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.3.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.3.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.3.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.3.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.3.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.4.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.4.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.4.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.4.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.4.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.4.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.4.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.4.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.5.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.5.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.5.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.5.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.5.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.5.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.5.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.5.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.6.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.6.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.6.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.6.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.6.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.6.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.6.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.6.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.7.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.7.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.7.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.7.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.7.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.7.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.7.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.7.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.8.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.8.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.8.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.8.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.8.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.8.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.8.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.8.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.9.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.9.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.9.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.9.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.9.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.9.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.9.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.9.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.10.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.10.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.10.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.10.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.10.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.10.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.10.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.10.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.attention.self.query.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.11.attention.self.query.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.attention.self.key.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.11.attention.self.key.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.attention.self.value.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.11.attention.self.value.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.attention.output.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| encoder.layer.11.attention.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.attention.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.attention.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.intermediate.dense.weight | (3072, 768) | (3072, 768) | 2359296 | Matrix |
| encoder.layer.11.intermediate.dense.bias | (3072,) | (3072,) | 3072 | Vector |
| encoder.layer.11.output.dense.weight | (768, 3072) | (768, 3072) | 2359296 | Matrix |
| encoder.layer.11.output.dense.bias | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.output.LayerNorm.weight | (768,) | (768,) | 768 | Vector |
| encoder.layer.11.output.LayerNorm.bias | (768,) | (768,) | 768 | Vector |
| pooler.dense.weight | (768, 768) | (768, 768) | 589824 | Matrix |
| pooler.dense.bias | (768,) | (768,) | 768 | Vector |

