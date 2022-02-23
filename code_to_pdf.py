from fpdf import FPDF 
from pathlib import Path
import os, sys

def text_to_pdf(root_path, dir_full_path, extensions_list):
    list_current_dir = os.listdir(dir_full_path)

    for entry in list_current_dir:

        entry_full_path = os.path.join(dir_full_path, entry)

        if os.path.isdir(entry_full_path):
            text_to_pdf(root_path, entry_full_path, extensions_list)

        elif os.path.isfile(entry_full_path) and entry.endswith(tuple(extensions_list)):
           
            pdf = FPDF() 
            pdf.add_page() 
            pdf.set_font("Times", size = 8) 
            
            file = open(entry_full_path,'r')
            for text in file: 
                pdf.multi_cell(200, 4, txt = text)
            
            relative_path = os.path.relpath(dir_full_path, root_path)
            output_path = "output/" + relative_path
    
            Path(output_path).mkdir(parents=True, exist_ok=True)

            pdf.output(output_path + "/" + entry + ".pdf") 

            file.close()

 
dir_name = sys.argv[1]

extensions_file = open("extensions.txt", "r")
extensions = extensions_file.read()
extensions_list = extensions.split('\n')

text_to_pdf(dir_name, dir_name, extensions_list)
