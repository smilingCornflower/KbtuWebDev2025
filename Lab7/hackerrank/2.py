# is weird?

def check_weird(n: int):
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  # n > 20
        print("Not Weird")

n = int(input().strip())
check_weird(n)
