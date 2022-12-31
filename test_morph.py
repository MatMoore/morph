import pytest
from morph import morph_noun, ends_in_vowel

@pytest.mark.parametrize(
  'input,expected',
  [
    ('사람', {'사람이', '사람은', '사람을', '사람에', '사람에서', '사람으로'}),
    ('차', {'차가', '차는', '차를', '차에', '차에서', '차로'}),
  ]
)
def test_morph_noun(input, expected):
  assert morph_noun(input) == expected


@pytest.mark.parametrize(
  'input',
  ['사람', '음식', '반찬', '술']
)
def test_ends_in_consonent(input):
  assert not ends_in_vowel(input)


@pytest.mark.parametrize(
  'input',
  ['차', '배', '비행기']
)
def test_ends_in_vowel(input):
  assert ends_in_vowel(input)
