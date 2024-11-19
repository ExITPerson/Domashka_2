import json

from src.utils import read_json


def test_read_json(tmp_path):
    data = [{"name": "Alice", "Age": 32}]
    file = tmp_path / "data.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    assert read_json(file) == [{"name": "Alice", "Age": 32}]