import img2pdf
import os
import sys
from PyPDF2 import PdfMerger

def images_to_pdf(folder, output_file):
    files = sorted([f for f in os.listdir(folder) if f.endswith('.png')])
    full_paths = [os.path.join(folder, f) for f in files]
    with open(output_file, "wb") as f:
        f.write(img2pdf.convert(full_paths))

def merge_pdfs(*pdf_files):
    if len(pdf_files) < 2:
        print("Нужно минимум два PDF для объединения")
        sys.exit(1)

    output_file = os.path.splitext(pdf_files[0])[0] + "_merged.pdf"
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
    print(f"Объединенный PDF сохранен: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python3 main.py <папка> [-a pdf1.pdf pdf2.pdf ...]")
        sys.exit(1)

    if "-a" in sys.argv:
        idx = sys.argv.index("-a")
        pdf_files = sys.argv[idx + 1:]
        merge_pdfs(*pdf_files)
    else:
        folder = sys.argv[1]
        folder_name = os.path.basename(folder)
        output_file = os.path.join(folder, f"{folder_name}.pdf")
        images_to_pdf(folder, output_file)
        print(f"PDF из PNG сохранен: {output_file}")
