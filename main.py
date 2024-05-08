from PyPDF2 import PdfReader, PdfWriter
import os, sys

def merge_pdfs(input_paths, output_path):
    pdf_writer = PdfWriter()

    for path in input_paths:
        with open(path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # Check if command-line arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python pdf_merge.py input1.pdf input2.pdf ... output.pdf")
        sys.exit(1)

    input_paths = [os.path.abspath(path) for path in sys.argv[1:-1]]

    output_path = sys.argv[-1]

    # Merge PDFs
    merge_pdfs(input_paths, output_path)

    print(f"PDFs merged successfully. Merged PDF saved at: {os.path.abspath(output_path)}")