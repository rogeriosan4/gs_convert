import gs_convert as gs 


if __name__ == "__main__":
    
    ##optional call to portable library, if you don't have ghostscript recognized in environment variables
    ##gs_portable_path_example = 'C:/Users/<username>/Downloads/CommonFiles/Ghostscript/bin/gswin64c'
    ##gs.PORTABLE_ENGINE = gs_portable_path_example 
    
    #declaring output file: convert all pages to a one file
    #gs.pdf2txt('files/file.pdf', 'files/file.txt')
    
    #omitting output file: convert all pages to separate files
    #gs.pdf2txt('files/file.pdf')
