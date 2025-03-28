import os
import re
import sys
import subprocess

folder_path="merged"

# Папка с файлами
if len(sys.argv) < 2:
    print("Usage: python script.py <folder_path>")
    sys.exit(1)

source_folder = sys.argv[1]

folder_name = os.path.basename(source_folder)

chapter_files = {}


# Перебираем файлы в папке
files = sorted(os.listdir(source_folder), key=lambda x: [int(num) if num.isdigit() else num for num in re.split(r'(\d+)', x)])
for filename in files:
    if os.path.isfile(os.path.join(source_folder, filename)):
        # Извлекаем номер главы
        match = re.search(r'(\d{3})', filename)
        if match:
            chapter = match.group(1)
            # Добавляем файл в список соответствующей главы
            if chapter not in chapter_files:
                chapter_files[chapter] = []
            chapter_files[chapter].append(os.path.join(source_folder, filename))

# Передача файлов в merger.exe
for chapter, files in chapter_files.items():
    try:
        # print(*files)
        subprocess.run(["merger.exe", *files], check=True)
        print(f"Chapter {chapter}: Files merged successfully.\n")
        # input()
    except subprocess.CalledProcessError as e:
        print(f"Error merging files for Chapter {chapter}: {e}\n")

#Переименование файла
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        match = re.search(r'(\d{3})', filename)
        if match:
            tom_number = match.group(1)
            new_name = f'{tom_number}-{folder_name}.pdf'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

input("\nНажмите Enter, чтобы выйти...")  # Ожидает ввода, чтобы не закрылась консоль