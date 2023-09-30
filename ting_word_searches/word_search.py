def exists_word(word, instance):
    """Aqui irá sua implementação"""
    load = []
    transform = {"palavra": "", "arquivo": "", "ocorrencias": []}
    for data in instance.fifo:
        transform["arquivo"] = data["nome_do_arquivo"]
        transform["palavra"] = word
        for index, phrase in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in phrase.lower():
                transform["ocorrencias"].append({"linha": index + 1})
        if len(transform["ocorrencias"]) == 0:
            return load
        load.append(transform)
    return load


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    load = []
    for data in instance.fifo:
        occorrences = [
            {"linha": index + 1, "conteudo": phrase}
            for index, phrase in enumerate(data["linhas_do_arquivo"])
            if word.lower() in phrase.lower()
        ]
        if len(occorrences) == 0:
            return load
        load.append(
            {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": occorrences,
            }
        )
    return load
