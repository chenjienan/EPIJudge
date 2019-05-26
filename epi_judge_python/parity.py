from test_framework import generic_test


def parity(x):
    num_of_one = 0
    s = bin(x)
    for c in s[2:]:
        if c == '1':
            num_of_one += 1
    return 1 if num_of_one % 2 != 0 else 0 


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
    # parity(55042960196257)