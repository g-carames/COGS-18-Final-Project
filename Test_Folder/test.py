""" Test File """

import sys
sys.path.append('/home/gcarames/FinalProject')

import functions as f
import pytest

def test_end_chat():
    assert f.end_chat('quit') == True
    assert f.end_chat('Quit') == True
    assert f.end_chat('test') == False
    assert f.end_chat('never quit') == False

      
def test_remove_punctuation():
    assert f.remove_punctuation('hi!!!') == 'hi'
    assert f.remove_punctuation('...hi') == 'hi'

    
def test_prepare_text():
    assert f.prepare_text('WhAt') == 'what'
    assert f.prepare_text('hey you') == ['hey', 'you']
    assert f.prepare_text('...hi') == 'hi'