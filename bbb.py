def a():
    try:
        if 1==1:raise Exception
    except Exception:
        print(1)
        raise Exception
    finally:
        print(4)
        return 5

if __name__ == '__main__':
    try:
        a()
        print(2)
    except Exception:
        print(3)