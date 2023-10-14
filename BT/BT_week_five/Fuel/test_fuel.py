from fulel import calculate_fuel_percentage


def test_valid_percentage(self):
    result = calculate_fuel_percentage(30, 50)
    self.assertEqual(result, '60%')

def test_empty_input(self):
    result = calculate_fuel_percentage('', '50')
    self.assertEqual(result, "X and Y must be positive integers")

def test_invalid_negative_input(self):
    result = calculate_fuel_percentage(-20, 50)
    self.assertEqual(result, "X and Y must be positive integers")

def test_invalid_x_greater_than_y(self):
    result = calculate_fuel_percentage(60, 50)
    self.assertEqual(result, "X must be less than or equal to Y")

def test_empty_y(self):
    result = calculate_fuel_percentage(30, '')
    self.assertEqual(result, "X and Y must be positive integers")

def test_zero_y(self):
    result = calculate_fuel_percentage(30, '0')
    self.assertEqual(result, "Y cannot be zero")

def test_fuel_empty(self):
    result = calculate_fuel_percentage(0, 50)
    self.assertEqual(result, 'E')

def test_fuel_full(self):
    result = calculate_fuel_percentage(50, 50)
    self.assertEqual(result, 'F')

if __name__ == '__main__':
    test_valid_percentage()
    test_empty_input()
    test_invalid_negative_input()
    test_invalid_x_greater_than_y()
    test_empty_y()
    test_zero_y()
    test_fuel_empty()
    test_fuel_full()
    
    
