From task import Task

def test_mark_done():
    task = Task("Testi ülesanne")
    task.mark_down()
    assert task.status == "done"