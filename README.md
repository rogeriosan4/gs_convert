
# ![Python Script Convert PDF em TXT](/files/pdf-to-txt.jpg?raw=true "Title")

## Conversor de PDF para TXT

gs_convert.py - script simples em python para a utilização do Ghostscript como conversor de arquivos pdf para  arquivo de texto ou imagem.

## Requerimentos

Necessário ter instalados:

* Python 3.6
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

Se estiver interessado em tornar este pacote melhor,
testes, correções de bugs e problemas de desempenho,
Sua ajuda é muito bem vinda!

## Links

[Python](https://www.python.org/)

[Ghostscript](https://www.ghostscript.com/download/gsdnld.html)
