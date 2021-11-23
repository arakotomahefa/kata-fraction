def sum_fraction(fract_A, fract_B):
  return Fraction((fract_A.numerateur * fract_B.denominateur + fract_B.numerateur * fract_A.denominateur),
                  fract_A.denominateur * fract_B.denominateur)

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

def reduced_fraction(a,b):
    val_gcd = gcd(sum_fraction(a,b).numerateur,sum_fraction(a,b).denominateur)
    return Fraction(sum_fraction(a,b).numerateur/val_gcd,sum_fraction(a,b).denominateur/val_gcd)

class Fraction:
  def __init__(self, numerateur, denominateur):
    self.numerateur = numerateur
    self.denominateur = denominateur


