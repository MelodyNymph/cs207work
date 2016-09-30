
from pytest import raises
from binsearch import binary_search
import numpy as np

input = list(range(10))
        
def test_name_NAN():
    with raises(NameError):
        binary_search([NAN, 1], 3)
        
def test_name_NotNumeric():
    with raises(NameError):
        binary_search([a, 1], 3)
        
def test_vacant_input():
    with raises(TypeError):
        binary_search([])        
        
def test_binary_0_input_array():
    assert binary_search([], 2) == -1
    
def test_array_1element_r():
    assert binary_search([3], 3) == 0
    
def test_array_1element_w():
    assert binary_search([3], 2) == -1    
    
def test_binary_right():
    assert binary_search(input, 5) == 5

def test_binary_wrong():
    assert binary_search(input, 4.5) == -1
    
def test_needle_greater_than_range():
    assert binary_search(input, 10) == -1
    
def test_needle_less_than_range():
    assert binary_search(input, -1) == -1
    
def test_needle_inbetween_NotInArray():
    assert binary_search([1,3,5,6,7], 4) == -1
        
def test_binary_extreme_left():
    assert binary_search(input, 0) == 0    
    
def test_binary_extreme_right():
    assert binary_search(input, 9) == 9    
    
def test_binary_inf_array():
    assert binary_search([1, 2, np.inf], 2) == 1       
    
def test_binary_find_inf():
    assert binary_search([1,2,np.inf], np.inf) == 2    

def test_needle_higher_than_bound():
    assert binary_search(input, 5, 1, 3) == -1   
    
def test_needle_in_bounds():
    assert binary_search(input, 3, 1, 5) == 3    
    
def test_needle_lower_than_bound():
    assert binary_search(input, 2, 3, 5) == -1           
    
def test_left_higher_than_right():
    assert binary_search(input, 2, 3, 1) == -1            
    
def test_left_equal_right_same_needle():
    assert binary_search(input, 2, 2, 2) == 2        
    
def test_left_equal_right_diff_needle():
    assert binary_search(input, 5, 2, 2) == -1            