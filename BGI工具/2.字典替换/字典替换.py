import json
import os

def load_and_sort_dict(file_path):
    """
    从给定的JSON文件中加载字典，并按键排序。
    :param file_path: JSON文件的路径。
    :return: 排序后的字典。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        dict_data = json.load(file)
        sorted_dict = dict(sorted(dict_data.items()))
    return sorted_dict

def replace_in_files(directory, dictionary, used_dict):
    """
    遍历指定目录中的所有txt文件，并使用提供的字典替换其中的文本。
    同时记录已经使用过的键值对，并将其写入新的JSON文件。
    :param directory: 要遍历的目录。
    :param dictionary: 包含替换规则的字典。
    :param used_dict: 记录已经使用过的键值对的字典。
    """
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            for key, value in dictionary.items():
                if key in content:
                    content = content.replace(key, value, 1)
                    used_dict[key] = value

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

def main():
    dict_path = 'game.json'
    input_dir = 'TransZone'

    dictionary = load_and_sort_dict(dict_path)
    used_dict = {}

    replace_in_files(input_dir, dictionary, used_dict)

    without_use_data = {k: v for k, v in dictionary.items() if k not in used_dict}
    with open('without_use.json', 'w', encoding='utf-8') as file:
        json.dump(without_use_data, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()