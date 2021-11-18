def sum_fraction(fract_A, fract_B):
  return Fraction((fract_A.numerateur * fract_B.denominateur + fract_B.numerateur * fract_A.denominateur),
                  fract_A.denominateur * fract_B.denominateur)


class Fraction:
  def __init__(self, numerateur, denominateur):
    self.numerateur = numerateur
    self.denominateur = denominateur
