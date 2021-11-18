from kata_fraction import Fraction,sum_fraction

def test_should_return_a_fraction():
    actual = Fraction(3,2)
    expected = Fraction(3,2)
    assert actual.numerateur == expected.numerateur
    assert actual.denominateur == expected.denominateur


def test_should_return_sum_fraction():
    fract_1 = Fraction(3,2)
    fract_2 = Fraction(3,2)
    actual = sum_fraction(fract_1,fract_2)
    expected = Fraction(12,4)
    assert isinstance(actual,Fraction)
    assert actual.numerateur == expected.numerateur
    assert actual.denominateur == expected.denominateur




