import json

# Đường dẫn đến tệp JSON
file_path = "levels.json"

# Đọc dữ liệu từ tệp JSON
with open(file_path, "r") as file:
    data = json.load(file)

# Truy cập và sử dụng dữ liệu từ dictionary
print(data["LDEBUG"]['type'])  # Output: John Doe