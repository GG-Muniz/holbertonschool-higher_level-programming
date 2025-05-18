#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer elements silently
            continue
        except IndexError:
            # This will be raised if x is greater than list length
            raise
    print()
    return count
