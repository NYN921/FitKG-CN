# SpERT_chinese
基于论文SpERT: "Span-based Entity and Relation Transformer"的中文关系抽取，同时抽取实体、实体类别和关系类别。

## 设置
### Requirements
- Required
  - Python 3.5+
  - PyTorch (tested with version 1.4.0)
  - transformers (+sentencepiece, e.g. with 'pip install transformers[sentencepiece]', tested with version 4.1.1)
  - scikit-learn (tested with version 0.24.0)
  - tqdm (tested with version 4.55.1)
  - numpy (tested with version 1.17.4)
- Optional
  - jinja2 (tested with version 2.10.3) - if installed, used to export relation extraction examples
  - tensorboardX (tested with version 1.6) - if installed, used to save training process to tensorboard
  - spacy (tested with version 3.0.1) - if installed, used to tokenize sentences for prediction

```python
pip install transformers ==4.1.1
pip install tensorboardX
pip install tqdm 
pip install jinja2 
pip install spacy==3.3.1
```

额外的，下载：https://github.com/explosion/spacy-models/releases/download/zh_core_web_sm-3.3.0/zh_core_web_sm-3.3.0.tar.gz 。执行：```pip install zh_core_web_sm-3.3.0.tar.gz```

还需要在huggingface上下载chinese-bert-wwm-ext到model_hub/chinese-bert-wwm-ext/下。


````
train.json  # 训练集
dev.json  # 验证集
fitkg_types.json  # 存储的实体类型和关系类型
entity_types.txt  
relation_types.txt  
````

train.json和dev.json里面的数据格式如下所示：

```python
[
    {"tokens": ["高", "尔", "夫", "\t", "包", "含", "\t", "T", "H", "E", " ", "P", "U", "T", "T", "I", "N", "G", " ", "G", "R", "E", "E", "N"], "entities": [{"type": "运动项目", "start": 0, "end": 3}, {"type": "专业名词", "start": 7, "end": 24}], "relations": [{"type": "包含", "head": 0, "tail": 1}]},
    ......
]
```

需要说明的是relations里面的head和tail对应的是entities里面实体的列表里的索引。

fitkg_types.json格式如下所示：

```python
{"entities": {"身体部位": {"short": "身体部位", "verbose": "身体部位"}, "运动项目": {"short": "运动项目", "verbose": "运动项目"}, "健身动作": {"short": "健身动作", "verbose": "健身动作"}, "器械工具": {"short": "器械工具", "verbose": "器械工具"}, "运动目标": {"short": "运动目标", "verbose": "运动目标"}, "解剖结构": {"short": "解剖结构", "verbose": "解剖结构"}, "营养物质": {"short": "营养物质", "verbose": "营养物质"}, "专业名词": {"short": "专业名词", "verbose": "专业名词"}}, 
"relations": {"位置": {"short": "位置", "verbose": "位置", "symmetric": false}, "形状": {"short": "形状", "verbose": "形状", "symmetric": false}, "起点": {"short": "起点", "verbose": "起点", "symmetric": false}, "止点": {"short": "止点", "verbose": "止点", "symmetric": false}, "包含": {"short": "包含", "verbose": "包含", "symmetric": false}, "从属": {"short": "从属", "verbose": "从属", "symmetric": false}, "锻炼": {"short": "锻炼", "verbose": "锻炼", "symmetric": false}, "功能": {"short": "功能", "verbose": "功能", "symmetric": false}, "使用": {"short": "使用", "verbose": "使用", "symmetric": false}, "实现": {"short": "实现", "verbose": "实现", "symmetric": false}, "需要": {"short": "需要", "verbose": "需要", "symmetric": false}}}
```

## 例子
(1)在fitkg-cn上使用训练集进行训练, 在验证集上进行评估。

```
python ./spert.py train --config configs/fitkg_train.conf
```

(2) 在测试集上进行评估，由于我们没有测试集，里面参数设置为验证集地址。注意修改路径，如果测试集和验证集一样，（1）和（2）为同一结果。

```
python ./spert.py eval --config configs/fitkg_eval.conf
```

(3) 修改fitkg_eval.conf里面保存好的模型的地址。进行预测使用的是fitkg_prediction_example.json，里面有三种格式，均可进行预测

```
python ./spert.py predict --config configs/fitkg_predict.conf
```



# 参考

> [lavis-nlp/spert: PyTorch code for SpERT: Span-based Entity and Relation Transformer (github.com)](https://github.com/lavis-nlp/spert)
>
> [SpERT: "Span-based Entity and Relation Transformer"](https://arxiv.org/abs/1909.07755)
