
import pytest
import sys
sys.path.insert(1, "./data/user_classification/")
#define function
def roundNum(data, num):
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j]= round(data[i][j],num)
    return data

#test function
def test_roundNum():
    table = [[1.6788, 1.3283, 2.204832, 1.08423, 1.2089], [1.290, 2.93042, 2.89024, 2.90842, 1.9043], [1.29408, 1.4094823, 4.024389, 8.2043, 3.423809]]
    table = roundNum(table,2)
    expected= [[1.68, 1.33, 2.20, 1.08, 1.21], [1.29, 2.93, 2.89, 2.91, 1.90], [1.29, 1.41, 4.02, 8.20, 3.42]]
    assert table == expected
