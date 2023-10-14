from Plate import is_valid

def test_valid_plate(self):
    self.assertTrue(is_valid("AB1234"))

def test_invalid_plate_short(self):
    self.assertFalse(is_valid("A1"))

def test_invalid_plate_long(self):
    self.assertFalse(is_valid("ABC12345"))

def test_invalid_plate_start_with_digit(self):
    self.assertFalse(is_valid("1AB123"))

def test_invalid_plate_zero_in_third_position(self):
    self.assertFalse(is_valid("AB0123"))

if __name__ == '__main__':
    test_valid_plate()
    test_invalid_plate_short()
    test_invalid_plate_long()
    test_invalid_plate_start_with_digit()
    test_invalid_plate_zero_in_third_position()