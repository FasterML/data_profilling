import pandas as pd


def test_summary():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

    assert iris.shape[0] == 150
