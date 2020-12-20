![](https://img.shields.io/badge/plataforma-win32--win64--linux64--linux32-blue)
![](https://img.shields.io/badge/python-3.x.x-blue)

# gs_convert - converte PDF em TXT

gs_convert.py - script simples em python para a utilização do Ghostscript como conversor de arquivos pdf para  arquivo de texto ou imagem.

## Requerimentos

Necessário ter instalados:

* Python 3.x.x
* Ghostscript 9.53

Se o sofware ghostscript não estiver nas variaveis de ambiente do sistema operacional [PATH], use Ghostscript portável dando a referencia do caminho da pasta onde se encontra o executável do programa:

```sh
gs_convet.PORTABLE_ENGINE = 'C:/Users/<username>/Downloads/CommonFiles/Ghostscript/bin/gswin64c'
```

## Como usar

```sh
# chamada opcional para a biblioteca portátil, se você não tiver o ghostscript reconhecido nas variáveis de ambiente [PATH]
gs_portable_path_example = 'C:/Users/<username>/Downloads/CommonFiles/Ghostscript/bin/gswin64c'
gs.PORTABLE_ENGINE = gs_portable_path_example

# declaring output file: convert all pages to a one file
gs.pdf2txt(file_in='files/file.pdf', file_out='files/file.txt')

# omitting output file: convert all pages to separate files
gs.pdf2txt(file_in='files/file.pdf')

# import text from pdf file to string variable
out = gs.pdf2string(file_in='files/file.pdf')
print(out)
```

## Status do projeto

Não terminado - refatorando código e ampliando recursos.

## Como contribuir para o projeto

Caso você encontrar um bug [Click-aqui](https://github.com/rogeriosan4/gs_convert/issues/new) crie um issue para eu corrigi-lo.
Se estiver interessado em tornar este pacote melhor, sua ajuda é muito bem vinda!

## Links

[Python](https://www.python.org/)

[Ghostscript](https://www.ghostscript.com/download/gsdnld.html)
