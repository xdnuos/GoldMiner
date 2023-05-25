# import json

# # Đường dẫn đến tệp JSON
# file_path = "data.json"

# # Đọc tệp JSON
# with open(file_path, "r") as file:
#     data = json.load(file)

def write_high_score():
    try:
        with open(high_score_file, "a") as file:
            # Ghi thời gian chơi và điểm số vào file
            file.write(f"{current_time}: {500}\n")
        return True
    except:
        print("có lỗi khi ghi file")
        return False
