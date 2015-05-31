from __future__ import unicode_literals
import re
import unittest
import strutil

#===============================================================================
class TestReplaceString(unittest.TestCase):
    '''
    Tests for ``replace`` using strings.
    
    Signature: ::
    
        replace(text, old, new, count=None, strip=False)
        
    '''
    # 
    
    #---------------------------------------------------------------------------
    def test_replace_1(self):
        self.assertEqual('is expected', strutil.replace(
            '  not expected \t \n',
            'not',
            'is',
            strip=True
        ))


#===============================================================================
class TestReplaceRegex(unittest.TestCase):
    '''
    Tests for ``replace`` using regular expression.
    
    Signature: ::
    
        replace(text, old, new, count=None, strip=False)
        
    '''
    
    #---------------------------------------------------------------------------
    def test_replace_re1(self):
        self.assertEqual('here are random numbers', strutil.replace(
            'here are 123 random 456 numbers',
            re.compile(r'\s+\d+\s+'),
            ' '
        ))


################################################################################
if __name__ == '__main__':
    unittest.main()
