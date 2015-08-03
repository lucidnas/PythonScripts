def gcd(a, b):
        if (0 == a % b):
            return b
        return gcd(b, a%b)


class Fraction():

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom


    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):
        
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    
def anagrams(a, b):
    s = [];
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                s.append(i)
            else:
                return 'not anagrams'
    return s
