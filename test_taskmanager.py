from TaskManager import TaskManager
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture
def task():
    return TaskManager()


def test_add_task(task):
    task.add_task('Cleaning')
    task.add_task('Washing')
    assert len(task.task_list) == 2
    assert task.task_list[0].task == 'Cleaning'
    assert task.task_list[1].task == 'Washing'


def test_show_list(task, capsys):
    task.add_task('Cleaning')
    task.show_list()
    captured = capsys.readouterr()
    assert 'Cleaning' in captured.out


def test_complete_task(task, capsys):
    task.add_task('Cleaning')
    task.complete_task('Cleaning')
    task.show_list()
    captured = capsys.readouterr()
    assert 'Cleaning is ✅ Completed' in captured.out


def test_remove_from_list(task, capsys):
    task.add_task('Cleaning')
    task.show_list()
    captured = capsys.readouterr()
    assert 'Cleaning' in captured.out

    task.remove_from_list('Cleaning')
    task.show_list()
    captured = capsys.readouterr()
    assert 'Cleaning removed from list' in captured.out
