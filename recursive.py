def count_digits(num):
    if num>10:
        return 1+count_digits(num//10)
    else:
        return 1
    
    #1+count_digits(1234)->5
    #   1+count_digits(123)->4
    #       1+count_digits(12)->3
    #           1+count_digits(1)->2
    #               1