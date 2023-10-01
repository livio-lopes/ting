## O que é projeto TING, Trybe Is Not Google?
Esse projeto tinha como objetivo simular o algoritmo de busca do Google. Utilizando POO em Python, o programa deveria ser capaz de identificar ocorrências de termos em arquivos TXT.
## Quais desafios?
1. Na classe `Queue`, implementei uma fila para armazenar os arquivos que serão lidos
2. A função `txt_importer`, do modulo `file_management`, é responsável por fazer a leitura de um arquivo .txt a partir de um caminho determinador e entregar uma lista de frases separadas por quebras de linhas
3. Em `process`, no modulo `file_proces`, a função transforma o conteudo da lista gerada por `txt_importer` em um dicionário que é salvo em uma instancia de `Queue`
4. Em `remove`, também dentro do modulo `file_proces`, é responsável por remover da fila o primeiro arquivo processado
5. Em `file_metadata`, ainda dentro de `file_proces`, é responsável por apresentar informações superficiais de um arquivo processador
6. A classe `PriorityQueue`, é a implementação de uma fila com prioridade, e para garantir o comportamento funcional dela implementei testes unitários
7. A função `exists_word` dentro do modulo `word_search`, é responsável por mapear na fila de arquivos processados onde há ocorrências de palavras inseridas
8. Em `search_by_word`, ainda em `word_search`, além de mapear a ocorrência de palavra, ainda é mapeada o conteudo da frase

## Como iniciar?
1. Clonando o projeto `git clone https://github.com/livio-lopes/ting.git`
2. Criando e acesso seu ambiente virtual `python3 -m venv venv && source .venv/bin/activate`
3. Instalando dependencias `python3 -m pip install -r dev-requirements.txt`
