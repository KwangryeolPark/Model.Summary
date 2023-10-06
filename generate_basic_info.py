import json
import os

INFO_JSON = "./basic_info.json"
DOC_PATH = "./docs"
JSON_PATH = "./docs/json"
IMAGE_PATH = "./docs/images"

with open(INFO_JSON, "w") as f:
    f.write(json.dumps({
        "json_path": JSON_PATH,
        "image_path": IMAGE_PATH,
        "docs_path": DOC_PATH,
        "json_name": "data.json",
        "rank_name": "README.md"
    }, indent=4, sort_keys=True))