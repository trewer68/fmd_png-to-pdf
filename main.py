import os
import sys
import pikepdf

def merge_pdfs(*pdf_files):
    if len(pdf_files) < 2:
        print("Нужно минимум два PDF для объединения")
        sys.exit(1)

    # Получаем имя первого PDF-файла без расширения для выходного файла
    output_file = os.path.splitext(pdf_files[0])[0] + "_merged.pdf"

    print("Объединяем следующие файлы:")
    for pdf in pdf_files:
        print(pdf)

    with pikepdf.Pdf.new() as pdf_out:
        for pdf in pdf_files:
            with pikepdf.open(pdf) as pdf_in:
                pdf_out.pages.extend(pdf_in.pages)
        pdf_out.save(output_file)

    print(f"Объединенный PDF сохранен: {output_file}")
    input("Нажмите Enter, чтобы выйти...")  # Ожидает ввода, чтобы не закрылась консоль

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python3 main.py <pdf1.pdf pdf2.pdf ...>")
        sys.exit(1)

    pdf_files = sys.argv[1:]
    merge_pdfs(*pdf_files)
