def A(a):
    def B(b):
        print(b ** a)
    return B
A(2)(5)
A(3)(3)