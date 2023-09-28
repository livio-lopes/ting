from ting_file_management.abstract_queue import AbstractQueue

# initial commit


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.fifo = []
        self.__length = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return self.__length

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.fifo.append(value)
        self.__length += 1

    def dequeue(self):
        """Aqui irá sua implementação"""
        self.__length -= 1
        return self.fifo.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index <= (len(self.fifo)-1):
            return self.fifo[index]
        raise IndexError("Índice Inválido ou Inexistente")
