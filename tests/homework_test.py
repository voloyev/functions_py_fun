from functions_py_fun import homework
import pytest


def test_exercise_1():
    assert homework.exercise_1([]) == 0
    assert homework.exercise_1_1([]) == 0
    with pytest.raises(TypeError):
        assert homework.exercise_1([None, "String"])
        assert homework.exercise_1_1([None, "String"])

    assert homework.exercise_1([1]) == 1
    assert homework.exercise_1_1([1]) == 1

    assert homework.exercise_1([1, 2, 3, 4, 5]) == 15
    assert homework.exercise_1_1([1, 2, 3, 4, 5]) == 15

    assert homework.exercise_1([-1, 2, 3, -4, 5]) == 5
    assert homework.exercise_1_1([-1, 2, 3, -4, 5]) == 5


def test_exercise_2():
    assert homework.exercise_2([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4, 5]
    assert homework.exercise_2([1, 5000, -13, 4, 5]) == [1, -13, 5000, 4, 5]


def test_exercise_3():
    assert homework.exercise_3([0, 1, 2, 3, 4, 5]) == 1
    assert homework.exercise_3([-1, -2, -3, -4, 0, 5]) == 5
    assert homework.exercise_3([0, 1, 2, 3, 4, -5], positive=False) == 5

    assert homework.exercise_3(["Hey", -2, -3, -4, 0, 5]) == None
    assert homework.exercise_3([]) == None
