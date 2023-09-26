import os
import json

input_folder = "./input"
output_folder = "./output"
specific_filenames = ["CustomCommands.txt","PlayerProperty.txt"]# 跳过这两个文件

# 检查输出文件夹是否存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# 遍历input文件夹中的所有txt文件
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        txt_file_path = os.path.join(input_folder, filename)
        json_file_path = os.path.join(output_folder, filename.replace('.txt', '.json'))

        # 检查文件名是否在特定文件名列表中
    if filename in specific_filenames:
        continue  # 跳过当前文件

    # 执行原來的操作，例如读取文件并进行更改
    with open(txt_file_path, 'r') as input_file:
        
        # 读取txt文件内容并去除注释行
        with open(txt_file_path, 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()
        
        input_text = ""
        for line in lines:
            line = line.strip()
            if line and not line.startswith("//"):
                input_text += line + "\n"

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

        # 将结果保存到json文件
        with open(json_file_path, 'w', encoding='utf-8') as file:
            file.write(output_text)

        print("文本已保存到文件：", json_file_path)
