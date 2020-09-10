import random

# function for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# uses extened euclidean algorithm to get the d value
# for more info look here: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
# will also be explained in class
def get_d(e, z):
    d_old = 0
    d_new = 1
    r_old = z
    r_new = e

    while r_new > 0:
        qu = r_old // r_new
        (d_old, d_new) = (d_new, d_old - qu * d_new)
        (r_old, r_new) = (r_new, r_old % r_new)
    d = d_old % z if r_old == 1 else None
    return d


def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
            else:
                return True

    else:
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    z = (p-1)*(q-1)
    x = random.randint(2,n)
    while gcd(x,z) != 1:
        x = random.randint(2,n)
    e = x
    d = get_d(e,z)
    print(e, d)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # plaintext is a single character
    # cipher is a decimal number which is the encrypted version of plaintext
    # the pow function is much faster in calculating power compared to the ** symbol !!!
    e = pk[0]
    n = pk[1]
    m = ord(plaintext)
    cipher = pow(m, e,n)
    return cipher


def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    # ciphertext is a single decimal number
    # the returned value is a character that is the decryption of ciphertext

    d,n = pk
    decr_value = pow(ciphertext, d,n)
    print(decr_value)
    ch = chr(decr_value)
    return ''.join(ch)

