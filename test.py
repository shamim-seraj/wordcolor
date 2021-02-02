import main


def test_mean():
    arr = [('#a83b0b', 'terracotta'), ('#d5bda3', 'beige'), ('#007fff', 'azur')]
    assert round(main.calculate_mean(arr), 2) == 243.64


def test_standard_deviation():
    arr = [('#a83b0b', 'terracotta'), ('#d5bda3', 'beige'), ('#007fff', 'azur')]
    assert round(main.calculate_standard_deviation(arr), 2) == 88.37


def test_variance():
    arr = [('#a83b0b', 'terracotta'), ('#d5bda3', 'beige'), ('#007fff', 'azur')]
    assert round(main.calculate_variance(arr), 2) == 7809.78
