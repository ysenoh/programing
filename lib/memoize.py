#  --*-coding:utf-8-*--

# メモ化する関数デコレータ

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper
