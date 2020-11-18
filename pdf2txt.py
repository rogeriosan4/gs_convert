import os
import platform

    
#path for portable ghostscript
#(if ghostscript command is not in the path of environment variables)
PORTABLE_ENGINE = ''

def __gspath__():
    if PORTABLE_ENGINE == '':
        if platform.system() == 'Windows':
            return 'gswin64c' # windows command
        else:
            return 'gs' # linux command
        return PORTABLE_ENGINE

def convert(file_in, file_out=None):
    if file_out == None:
        file_out = file_in.split('.pdf')[0]+'%03d.txt'

    gs = __gspath__()
        
    gs_command = '{} -sDEVICE=txtwrite -sOutputFile={} -q -dNOPAUSE -dBATCH {}'.format(gs, file_out, file_in)

    os.system(gs_command)


    
