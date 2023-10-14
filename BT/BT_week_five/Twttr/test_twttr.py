from twttr import shorten

def test_shorten_lowercase(self):
    result = shorten("hello")
    self.assertEqual(result, "hll")

def test_shorten_uppercase(self):
    result = shorten("WORLD")
    self.assertEqual(result, "WRLD")

def test_shorten_mixed_case(self):
    result = shorten("AbCdeF")
    self.assertEqual(result, "bCdF")

def test_shorten_empty_input(self):
    result = shorten("")
    self.assertEqual(result, "")

if __name__ == '__main__':
    test_shorten_lowercase()
    test_shorten_uppercase()
    test_shorten_mixed_case()
    test_shorten_empty_input()
