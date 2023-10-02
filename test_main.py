from mylib.delete import delete
from mylib.extract import extract
from mylib.query import query
from mylib.transform_load import load
from mylib.update import update

def testMain():
    extract()
    load()
    assert query()[1][1]=='1'
    update()
    assert query()[1][1]=='one'
    delete()
    assert query()[1][0]=='4394761'

if __name__ == '__main__':
    testMain()
    pass