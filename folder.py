import os
import re
import sys
import subprocess

# Папка с файлами
if len(sys.argv) < 2:
    print("Usage: python script.py <folder_path>")
    sys.exit(1)

source_folder = sys.argv[1]

chapter_files = {}

# Перебираем файлы в папке
for filename in os.listdir(source_folder):
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
        subprocess.run(["!merger.exe", *files], check=True)
        print(f"Chapter {chapter}: Files merged successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error merging files for Chapter {chapter}: {e}")