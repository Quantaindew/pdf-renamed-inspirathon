import os
import PyPDF2
import shutil

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        content = ' '.join([reader.getPage(i).extractText() for i in range(reader.getNumPages())])
    return content

def remove_spaces_from_name(name):
    return name.replace(' ', '-')

def rename_pdf(file_path, new_name, new_directory):
    new_name = remove_spaces_from_name(new_name)
    new_name += "-CERTIFICATE"  # Add "certificate" to the end of the name
    new_file_path = os.path.join(new_directory, new_name + '.pdf')
    shutil.move(file_path, new_file_path)
    print(file_path, '->', new_file_path)

def process_pdfs(directory, new_directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            content = read_pdf(file_path)
            rename_pdf(file_path, content, new_directory)
    print('Done!')

process_pdfs('/pdfs', '/renamed')