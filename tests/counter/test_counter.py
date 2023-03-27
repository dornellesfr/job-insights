from src.pre_built.counter import count_ocurrences


def test_counter():
    result = count_ocurrences('data/jobs.csv', 'JavaScript')
    result2 = count_ocurrences('data/jobs.csv', 'Python')
    assert result == 122
    assert result2 == 76
