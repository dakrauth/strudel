import re
import unittest
import strutil

class TestReplaceString(unittest.TestCase):
    '''
    Tests for ``replace`` using strings.
    
    Signature: ::
    
        replace(text, old, new, count=None, strip=False)
        
    '''
    
    def test_replace_1(self):
        self.assertEqual('is expected', strutil.replace(
            '  not expected \t \n',
            'not',
            'is',
            strip=True
        ))


class TestReplaceRegex(unittest.TestCase):
    '''
    Tests for ``replace`` using regular expression.
    
    Signature: ::
    
        replace(text, old, new, count=None, strip=False)
        
    '''
    
    def test_replace_re1(self):
        self.assertEqual(
            'here are random numbers',
            strutil.replace(
                'here are 123 random 456 numbers',
                re.compile(r'\s+\d+\s+'),
                ' '
            )
        )


class TestSplitter(unittest.TestCase):
    '''
    Signature: ::
    
        def splitter(text, token=None, expected=2, default='', strip=False)
        
    '''
    def test_splitter_1(self):
        self.assertEqual(
            ['Hello, world', '', '', ''],
            strutil.splitter('Hello, world', token='@', expected=4)
        )

    def test_splitter_2(self):
        self.assertEqual(
            ['Hello,', 'world', ''],
            strutil.splitter('Hello, world', expected=3)
        )
        
    def test_splitter_3(self):
        self.assertEqual(
            ['1', '2', '0'],
            strutil.splitter('X 1 Y 2', re.compile(r' ?[A-Z] ?'), expected=3, default='0')
        )

    
class TestFindFirst(unittest.TestCase):
    
    def test_find_first_1(self):
        items = 'abc 123 ------ spam eggs'.split()
        self.assertEqual(strutil.find_first(items, '-'), 2)
        self.assertEqual(strutil.find_first(items, re.compile(r'\d+')), 1)
        self.assertEqual(strutil.find_first(items, 'X'), None)


class TestReplaceEach(unittest.TestCase):
    
    def test_replace_each_1(self):
        self.assertEqual(
            strutil.replace_each(
                'line 1\nline 2\nline 3',
                (('line', 'Line'), (re.compile(r'(\d+)'), r'#\1'))
            ),
            'Line #1\nLine #2\nLine #3'
        )


if __name__ == '__main__':
    unittest.main()
