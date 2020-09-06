#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from unittest import TestCase
import pandas as pd

from data_profilling.data_profiling import Profiling


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)


def test_summary():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    print(1111)
    print(Profiling.summary(iris))
    assert iris == 2, "test failed"
    # assert fib(2) == 1
    # assert fib(7) == 13
    # with pytest.raises(AssertionError):
    #     fib(-10)
