import pdf2txt 


if __name__ == "__main__":

    #gs_portable_path_example = 'C:/Users/<username>/Downloads/CommonFiles/Ghostscript/bin/gswin64c'
    #pdf2txt.PORTABLE_PATH = gs_portable_path_example 
    
    #declaring output file: convert all pages to a file
    pdf2txt.convert('files/file.pdf', 'files/file.txt')
    
    #omitting output file: convert all pages to separate files
    #pdf2txt.convert('files/file.pdf')
    
