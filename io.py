import os
import json

input_folder = "./input"
output_folder = "./output"

# 檢查輸出文件夾是否存在，如果不存在則創建
os.makedirs(output_folder, exist_ok=True)

# 遍歷input文件夾中的所有txt文件
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        txt_file_path = os.path.join(input_folder, filename)
        json_file_path = os.path.join(output_folder, filename.replace('.txt', '.json'))

        # 讀取txt文件內容
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()

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
        output_text = json.dumps(output_list, indent=4, ensure_ascii=False)

        # 將結果保存到json文件
        with open(json_file_path, 'w', encoding='utf-8') as file:
            file.write(output_text)

        print("文本已保存到文件：", json_file_path)
