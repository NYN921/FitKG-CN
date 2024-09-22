import json

file_path = 'G://标注数据//整体//1-config.txt'
newdatas = []

with open(file_path, 'r', encoding='utf-8') as file:
    dataset = json.load(file)

for data in dataset[0]["data"]:
    newdata = {}
    newdata["tokens"] = [strx for strx in data["fileContent"]]

    # 重新编号labels中的id
    id_mapping = {}  # 旧id到新id的映射
    new_labels = []  # 存储重新编号后的labels
    for idx, label in enumerate(data["labels"]):
        new_id = idx
        # 更新id映射
        id_mapping[label["id"]] = new_id
        label["id"] = new_id
        new_labels.append(label)

    newdata["entities"] = []
    for label in new_labels:
        entity_type = None
        for category in dataset[0]["labelCategories"]:
            if category["id"] == label["categoryId"]:
                entity_type = category["text"]
                break
        if entity_type:
            newdata["entities"].append({
                "type": entity_type,
                "start": label["startIndex"],
                "end": label["endIndex"]
            })

    newdata["relations"] = []
    for con in data["connections"]:
        if con["fromId"] in id_mapping and con["toId"] in id_mapping:  # 检查连接的 ID 是否存在
            relation_type = None
            for category in dataset[0]["connectionCategories"]:
                if category["id"] == con["categoryId"]:
                    relation_type = category["text"]
                    break
            if relation_type:
                newdata["relations"].append({
                    "type": relation_type,
                    "head": id_mapping[con["fromId"]],
                    "tail": id_mapping[con["toId"]]
                })

    if newdata["entities"]:  # 如果entities不为空，则添加数据
        newdatas.append(newdata)

filename = 'G://标注数据//整体//1.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(newdatas, f, ensure_ascii=False)
