import unittest
from drift import compare
class Tests(unittest.TestCase):
    def test_equal(self): self.assertEqual(compare({'a':1},{'a':1}),[])
    def test_added_and_removed(self): self.assertEqual([c['change'] for c in compare({'a':1},{'b':2})],['removed','added'])
    def test_nested(self): self.assertEqual(compare({'a':{'b':1}},{'a':{'b':2}})[0]['path'],'/a/b')
    def test_pointer_escaping(self): self.assertEqual(compare({'a/b~':1},{'a/b~':2})[0]['path'],'/a~1b~0')
    def test_ignore_subtree(self): self.assertEqual(compare({'meta':{'x':1}},{'meta':{'x':2}},['/meta']),[])
    def test_types_differ(self): self.assertEqual(len(compare({'x':True},{'x':1})),1)
    def test_arrays_atomic(self): self.assertEqual(compare([1,2],[2,1])[0]['path'],'')
    def test_ignore_does_not_use_prefix(self): self.assertEqual(len(compare({'ab':1},{'ab':2},['/a'])),1)
if __name__=='__main__': unittest.main()
