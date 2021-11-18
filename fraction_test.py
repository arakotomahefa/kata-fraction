from kata_fraction import Fraction

def test_should_return_sum_2_fractions():
    actual = Fraction(3,2)
    expected = Fraction(3,2)
    assert actual.numerateur == expected.numerateur
    assert actual.denominateur == expected.denominateur


