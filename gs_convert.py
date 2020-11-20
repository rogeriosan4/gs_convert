import os
import platform

    
#path for portable ghostscript
#(if ghostscript command is not in the path of environment variables)
PORTABLE_ENGINE = None

def __gs__():
    if not PORTABLE_ENGINE:
        if platform.system() == 'Windows':
            return 'gswin64c' # windows command
        else:
            return 'gs' # linux command
    return os.path.abspath(PORTABLE_ENGINE)

def pdf2txt(file_in, file_out=None):
    file_in = os.path.abspath(file_in)
    if not file_out:
        file_out = file_in.split('.pdf')[0]+'%03d.txt'
    gs_command = '{} -sDEVICE=txtwrite -sOutputFile={} -q -dNOPAUSE -dBATCH {}'.format(__gs__(), file_out, file_in)
    os.system(gs_command)

def pdf2png(file_in, file_out=None):
    file_in = os.path.abspath(file_in)
    if not file_out:
        file_out = file_in.split('.pdf')[0]+'%03d.png'
    gs_command = '{} -sDEVICE=png16m -sOutputFile="{}" -q -dNOPAUSE -dBATCH {}'.format(__gs__(), file_out, file_in)
    os.system(gs_command)
    
