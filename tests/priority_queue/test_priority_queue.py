from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    archive_priority = {"qtd_linhas": 4}
    other_archive_priority = {"qtd_linhas": 3}
    no_priority_archive = {"qtd_linhas": 6}
    other_no_priority_archive = {"qtd_linhas": 7}
    priority_queue = PriorityQueue()
    priority_queue.enqueue(archive_priority)
    priority_queue.enqueue(other_archive_priority)
    priority_queue.enqueue(no_priority_archive)
    priority_queue.enqueue(other_no_priority_archive)
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue.high_priority) == 2
    assert priority_queue.__len__() == 4
    index = 1
    assert priority_queue.search(index) == other_archive_priority
    index = 3
    assert priority_queue.search(index) == other_no_priority_archive
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(99)

    given = priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 1
    assert given == archive_priority
    priority_queue.dequeue()
    given = priority_queue.dequeue()
    assert len(priority_queue.regular_priority) == 1
    assert given == no_priority_archive
