import sys

def multi_2_num(num1, num2):
    return num1 * num2


if __name__ == "__main__":
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(multi_2_num(num1, num2))
    except Exception:
        raise