#pytest has 3 phases 
#arrange 
#act 
#assert 

#import the bmi.py from lab 2
import Lab2.bmi as bmi 

def test_bmi_normal_weight(): 
    #arrange 
    height = 1.73 
    weight = 57 
    #act 
    result = bmi.calculate_bmi(height, weight)
    #assert 
    assert result == 0 

def test_bmi_over_weight(): 
    assert bmi.calculate_bmi(1.73,80) == 1 #assert rightaway

def test_bmi_under_weight():
    height = 1.73 
    weight = 50 
    result = bmi.calculate_bmi(height,weight)
    assert result == -1 



