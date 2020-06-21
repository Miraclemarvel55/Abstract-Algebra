"""
author:sida
time:2020.06.21
"""
"""
关于数论的一些函数，像求整数N的单位根或者单位原根。

functions about number theory,like unit root or unit original root for number N.
"""
import numpy as np

isTest = __name__ == "__main__"

def getUnitRoot(N = 1):
    """
    获得单位根

    get the unit root
    :return: complex number list sorted
    ：返回：复数列表从小到大
    """
    numbersLessThanN = np.arange(N)
    roots = np.apply_along_axis(func1d = lambda x:np.e**(2*np.pi*x*1j/N),axis=0,arr = numbersLessThanN)
    if isTest:
        print(N,roots)
    return roots

if __name__ == "__main__":
    getUnitRoot(2)