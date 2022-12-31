import pytest
from morph import morph_noun, ends_in_vowel


testdata =   [
  ('사람', {'사람이'}),
  ('차', {'차가'}),
]

@pytest.mark.parametrize(
  'input,expected',
  testdata
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
