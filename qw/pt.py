import re

def process_titles(line):
    # 匹配标题并添加相应数量的 #
    line = re.sub(r'^(\d+)\s*、', r'## \1 ', line)
    line = re.sub(r'^(\d+\.\d+)\s*、', r'### \1 ', line)
    line = re.sub(r'^(\d+\.\d+\.\d+)\s*、', r'#### \1 ', line)
    return line

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            new_line = process_titles(line)
            file.write(new_line)

if __name__ == "__main__":
    input_file = 'TALES OF KOTOR——旧共和国武士彩蛋小集锦.md'
    output_file = 'TALES OF KOTOR——旧共和国武士彩蛋小集锦_processed.md'
    process_file(input_file, output_file)