"1. Găsește ultimul număr prim mai mic decât un număr dat."
def get_largest_prime_below(n):
    if n<=2:
        print("Nu exista")
    else:
        while True:
            n = n-1
            ok=True
            for i in range(2,n):
                if n%i == 0:
                    ok = False
                    break
            if ok == True :
                print(n)
                break

def test_get_largest_prime_below():
    n= int(input("1) n = "))
    get_largest_prime_below(n)

  
"Exercitiul 3."


def is_prime(n):

  if(n==0 or n == 1):
    return False
  for d in range(2, n//2):
    if (n%d==0):
        return False
  return True

def get_goldbach(n):
    ok=True
    for i in range(2,n//2+1):
        p1=i
        p2=n-i
        if is_prime(p1) and is_prime(p2):
            ok=False
            print(p1,p2)
            break
    if ok==True:
        print("Nu are proprietatea")
def test_get_goldbach():
    n=n= int(input("3) n = "))
    get_goldbach(n)

test_get_largest_prime_below()
test_get_goldbach()
    

