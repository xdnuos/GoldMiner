import json

# Đường dẫn đến tệp JSON
file_path = "data.json"

# Đọc tệp JSON
with open(file_path, "r") as file:
    data = json.load(file)
