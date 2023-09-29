import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    TXT_EXTENSION = ".txt"
    if path_file.endswith(TXT_EXTENSION):
        try:
            with open(path_file) as file:
                content = file.read()
                content = content.split("\n")
            return content
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido")
