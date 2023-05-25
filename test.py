import datetime

# Đường dẫn đến file txt
file_path = "high_scores.txt"

# Lấy thời gian hiện tại
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mở file để ghi danh sách điểm cao
with open(file_path, "a") as file:
    # Ghi thời gian chơi và điểm số vào file
    file.write(f"{current_time}: {500}\n")

# Đọc danh sách điểm cao từ file
high_scores = []
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        time_score = line.strip().split(": ")
        time = time_score[0]
        score = int(time_score[1])
        high_scores.append({"time": time, "score": score})

# In danh sách điểm cao
for score in high_scores:
    print(score["time"], score["score"])
