import unittest

import numpy.testing as npt

from task import Task


class TestTask(unittest.TestCase):
    def test_solve_system(self):
        task = Task()
        task.work()
        npt.assert_allclose(task.a @ task.x, task.b)
