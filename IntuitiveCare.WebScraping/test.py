
import os

work_dir = os.getcwd()

files_report = os.listdir(work_dir)

pdf_files = [file for file in files_report if file.endswith('.pdf')]

print(pdf_files)