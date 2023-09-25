import os
import json

# 指定要讀取的文件路徑和文件名
file_path = "./input/武器.txt"

# 檢查文件是否存在
if os.path.isfile(file_path):
    # 打開文件並讀取內容
    with open(file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()
else:
    print("文件不存在：", file_path)
    exit()

output_list = []
lines = input_text.split('\n')

for line in lines:
    if line.strip() != "":
        parts = line.split(':')
        value = int(parts[0])
        label = parts[1]

        line_dict = {
            "label": label,
            "value": value
        }

        output_list.append(line_dict)

# 將 Python 對象轉換為格式化的 JSON 字符串，並禁用自動轉義
output_text = json.dumps(output_list, indent=4, ensure_ascii=False)

# 指定保存的文件路徑和文件名
output_file_path = "./output/武器.json"

# 檢查 output_text 是否為空
if output_text:
    # 創建目錄
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # 將文本保存到文件中
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(output_text)

    print("文本已保存到文件：", output_file_path)
else:
    print("無需創建文件，輸出文本為空。")
