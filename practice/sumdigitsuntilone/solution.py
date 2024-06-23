def seek_single_digit_sum(number) -> int:
    current_sum = number
    while True:
        current_sum = sum(n for n in [int(i) for i in str(current_sum)])
        if current_sum < 10: return current_sum
