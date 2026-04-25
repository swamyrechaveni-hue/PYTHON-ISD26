from src.to_do_list import main, tasks


def test_add_task(monkeypatch):
    tasks.clear()
    inputs = iter(["1", "Task A", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    assert "Task A" in tasks


def test_view_tasks(monkeypatch, capsys):
    tasks.clear()
    tasks.append("Task 1")

    inputs = iter(["2", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()

    output = capsys.readouterr().out
    assert "Task 1" in output


def test_remove_task(monkeypatch):
    tasks.clear()
    tasks.append("Task 1")

    inputs = iter(["3", "1", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()

    assert len(tasks) == 0