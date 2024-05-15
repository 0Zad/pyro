import pytest
from calc_press_cyl import model_s

def test_model_s():

    d = 0.6
    r = 0.2
    
    alpha_lim, ct, rsdd = model_s(r, d, 90)
    
    assert alpha_lim == 75.52248781407006
    assert ct == 1.0119733183126847
    assert rsdd == 0.25012227941024423