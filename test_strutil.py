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


#===============================================================================
class TestSplitter(unittest.TestCase):
    '''
    Signature: ::
    
        def splitter(text, token=None, expected=2, default='', strip=False)
        
    '''
    #---------------------------------------------------------------------------
    def test_splitter_1(self):
        self.assertEqual(
            ['Hello, world', '', '', ''],
            strutil.splitter('Hello, world', token='@', expected=4)
        )

    #---------------------------------------------------------------------------
    def test_splitter_2(self):
        self.assertEqual(
            ['Hello,', 'world', ''],
            strutil.splitter('Hello, world', expected=3)
        )
        
    #---------------------------------------------------------------------------
    def test_splitter_3(self):
        self.assertEqual(
            ['1', '2', '0'],
            strutil.splitter('X 1 Y 2', re.compile(r' ?[A-Z] ?'), expected=3, default='0')
        )
        

################################################################################
if __name__ == '__main__':
    unittest.main()
