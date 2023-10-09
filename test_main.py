from mylib.create import create
from mylib.query import query

def testMain():
    create()
    output = query()
    # test GROUPBY
    assert output[0][3] == 260
    # test ORDERBY
    assert output[0][3] > output[1][3]
    assert output[1][3] > output[2][3]
    # test WHERE
    sex_l = [t[2] for t in output]
    assert 'Male' not in sex_l
    assert len(output) == 3
if __name__ == '__main__':
    testMain()
    pass