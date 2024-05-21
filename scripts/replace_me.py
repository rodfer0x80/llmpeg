import os
import sys 
import re

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        
    new_contents = re.sub(old_text, new_text, file_contents)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_contents)

def replace_in_dir(dir_path, old_text, new_text):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                replace_text_in_file(file_path, old_text, new_text)
                print(f'Replaced text in: {file_path}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
      print("Usage: __main__ <dir_path> <old_text> <new_text>")
      exit(1)
    else: 
      dir_path = sys.argv[1]
      old_text = sys.argv[2]
      new_text = sys.argv[3]
    replace_in_dir(dir_path, old_text, new_text)
    exit()


