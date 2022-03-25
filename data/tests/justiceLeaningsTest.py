
import pytest
import sys
sys.path.insert(1, "./data/user_classification/")
#define function
def roundNum(data, num):
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j]= round(data[i][j],num)
    return data

def adjustVals(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if(data[i][j] == "nan"):
                continue
            else:
                if(data[i][j]>1.5):
                    data[i][j] = (2 - data[i][j]) + 1
                elif(data[i][j]<1.5):
                    data[i][j] = 2 - (data[i][j] - 1)
    return data

#test function
def test_roundNum():
    table = [[1.6788, 1.3283, 2.204832, 1.08423, 1.2089], [1.290, 2.93042, 2.89024, 2.90842, 1.9043], [1.29408, 1.4094823, 4.024389, 8.2043, 3.423809]]
    table = roundNum(table,2)
    expected= [[1.68, 1.33, 2.20, 1.08, 1.21], [1.29, 2.93, 2.89, 2.91, 1.90], [1.29, 1.41, 4.02, 8.20, 3.42]]
    assert table == expected

def test_roundNum1():
    table = [[1.6788, 1.3283, 2.204832, 1.08423, 1.2089], [1.290, 2.93042, 2.89024, 2.90842, 1.9043], [1.29408, 1.4094823, 4.024389, 8.2043, 3.423809]]
    table = roundNum(table,1)
    expected= [[1.7, 1.3, 2.2, 1.1, 1.2], [1.3, 2.9, 2.9, 2.9, 1.9], [1.3, 1.4, 4.0, 8.2, 3.4]]
    assert table == expected


def test_roundNum2():
    table = [[1.6788, 1.3283, 2.204832, 1.08423, 1.2089], [1.290, 2.93042, 2.89024, 2.90842, 1.9043], [1.29408, 1.4094823, 4.024389, 8.2043, 3.423809]]
    table = roundNum(table,3)
    expected= [[1.679, 1.328, 2.205, 1.084, 1.209], [1.290, 2.930, 2.890, 2.908, 1.904], [1.294, 1.409, 4.024, 8.204, 3.424]]
    assert table == expected

def test_adjustVals():
    table = [[1.50, 1.32, 1.20, 1.08, 1.20], [1.29, 1.93, 1.89, 1.90, 1.90], [1.29, 1.40, 1.09, 1.20, 1.42]]
    table = adjustVals(table)
    print(table)
    expected = [[1.50, 1.68, 1.8, 1.92, 1.80], [1.71, 1.07, 1.11, 1.1, 1.1], [1.71, 1.6, 1.91, 1.8, 1.58]]
    assert table == expected


