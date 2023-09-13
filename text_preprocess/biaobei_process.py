# 说话人；dataset下processed wav文件路径的文件夹名；raw下源wav的文件夹名
name = 'biaobei'

# INPUT_FILE_PATH = '/absolute_path/input.txt'
INPUT_FILE_PATH = './biaobei_train_filelist.txt'
OUTPUT_FILE_PATH = f"{name}_output.txt"


def process():
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file, open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as output_file:
        # 逐行读取输入文件
        for line in input_file:
            # 分割每行中的wav路径和文本
            wav_path, text = line.strip().split('|')
            # 将格式化后的文本写入输出文件
            output_file.write(f"./dataset/{wav_path}|{name}|ZH|{text}\n")


if __name__ == '__main__':
    process()
