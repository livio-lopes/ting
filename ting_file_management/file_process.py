import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    extract = txt_importer(path_file)
    file_in_queue = None
    for index in list(range(instance.__len__())):
        file_in_queue = (
            instance.search(index)
            if instance.search(index)["nome_do_arquivo"] == path_file
            else None
        )
    if extract and not file_in_queue:
        transform = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(extract),
            "linhas_do_arquivo": extract,
        }
        # loading
        instance.enqueue(transform)
        sys.stdout.write(f"{transform}")
        # print(sys.stdout)


# fila_do_bode = Queue()
# process('statics/arquivo_teste.txt', fila_do_bode)


def remove(instance):
    """Aqui irá sua implementação"""
    leaving_queue = instance.dequeue()
    if not leaving_queue:
        sys.stdout.write("Não há elementos\n")
        return
    path_file = leaving_queue["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
    return


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
