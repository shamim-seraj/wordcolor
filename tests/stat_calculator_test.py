"""
This module is to test all the functions of the module "stat_calculator.py"
"""
from wordcolor import stat_calculator


def test_color_diff():
    """
    :return: nothing
    """
    assert stat_calculator.color_diff("#ffffff", "#123456") == 354.8788525680278
    assert stat_calculator.color_diff("#8f2971", "#107611") == 176.84456451924103


def test_mean():
    """
    :return: nothing
    """
    original_data = {"terracotta": "#a83b0b", "caramel": "#be6d33", "charcoal": "#464646"}
    estimated_data = {"terracotta": "#e2725b", "caramel": "#85461e", "charcoal": "#35454f"}
    assert stat_calculator.calculate_mean(original_data, estimated_data) == 68.18


def test_standard_deviation():
    """
    :return: nothing
    """
    original_data = {"terracotta": "#a83b0b", "caramel": "#be6d33", "charcoal": "#464646"}
    estimated_data = {"terracotta": "#e2725b", "caramel": "#85461e", "charcoal": "#35454f"}
    assert stat_calculator.calculate_standard_deviation(original_data, estimated_data) == 38.41


def test_variance():
    """
    :return: nothing
    """
    original_data = {"terracotta": "#a83b0b", "caramel": "#be6d33", "charcoal": "#464646"}
    estimated_data = {"terracotta": "#e2725b", "caramel": "#85461e", "charcoal": "#35454f"}
    assert stat_calculator.calculate_variance(original_data, estimated_data) == 1475.29
