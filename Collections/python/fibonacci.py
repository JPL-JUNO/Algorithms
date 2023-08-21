"""
@Description: 斐波拉契数列的实现
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-21 11:34:43
"""
import timeit


def fib_rec(n: int):
    """递归算法"""
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


from functools import lru_cache as cache


@cache(maxsize=None)
def fib_rec_cache(n: int):
    """缓存中间结果来计算斐波拉契数列

    递归算法的主要问题是中间结果不会缓存，而是重新计算。为了避免出现这种特有的问题，可以使用一个装器（decorator）来负责缓存中间结果。它可以将执行速度提高好几个数量级：
    Parameters
    ----------
    n : int
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if n < 2:
        return n
    else:
        return fib_rec_cache(n - 1) + fib_rec_cache(n - 2)


def fib_it(n: int):
    """循环（迭代）算法"""
    x, y = 0, 1
    for _ in range(1, n + 1):
        x, y = y, x + y
    return x


def main(n: int):
    rec_time_start = timeit.default_timer()
    fib_rec(n)
    print(f"递归运行时间：{timeit.default_timer() - rec_time_start}s")

    cache_time_start = timeit.default_timer()
    fib_rec_cache(n)
    print(f"缓存运行时间：{timeit.default_timer() - cache_time_start}s")

    it_time_start = timeit.default_timer()
    fib_it(n)
    print(f"循环运行时间：{timeit.default_timer() - it_time_start}s")


if __name__ == '__main__':
    # fib_rec(35)
    main(35)
