# Code to PDF

This repository contains scripts to help converting a source code directory into a directory of PDFs. It is usefull for generating documents to register software.

<!-- comentário para fazer o repositório aparecer na busca -->
<!-- converter código para PDF para fazer registro no INPI -->

## Running

First, select a repository with source code that you want to convert to PDF and get the full path to it.

Then fill the _extensions.txt_ with the file extensions that you want to be converted (only textual files supported). If you wish, you can run 

`python list_extensions.py <full/path/to/directory>` 

to automatically fill this file with all the extensions in the provided directory and then remove the ones you don't want to convert by hand.


Finally, run 

`python code_to_pdf.py <full/path/to/directory>`

The resulting PDFs will be located in the _output_ folder at the current directory. The directory tree will be the same as the one passed as argument.
