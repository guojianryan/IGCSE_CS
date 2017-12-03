def gen_check_digit(isbn):
    odd_total, even_total = 0, 0

    for idx in range(0, len(isbn)):
        if(idx % 2 == 0):
            odd_total = odd_total +  int(isbn[idx])
        else:
            even_total = even_total +  int(isbn[idx])

    remainder = (odd_total + even_total * 3) % 10

    return  10 - remainder if remainder != 0 else remainder

def check_isbn(isbn):
    return str(gen_check_digit(isbn[0:12])) == isbn[12] 

