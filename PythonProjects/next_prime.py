#Program: Next Prime
#Author: Abdulnasir Mohammed
#Date: 06/10/15

def find_next_prime(m):
    p = m +1
    for n in range(2,p):
        if p%n == 0:
            p = find_next_prime(p)
            break
    return p
 
#find_next_prime(m)
def main():
    m = input("Enter number: ")
    print find_next_prime(m)
 
main()
