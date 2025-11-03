import sys
from pathlib import Path

# Add the parent directory (src) to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from datetime import date, datetime 
import unittest

from note import *
class TestNote(unittest.TestCase):
    def test_equal(self):
        md = "test"
        note = Note(md)
        self.assertEqual(note,"test")
    def test_repr(self):
        md = "test"
        note = Note(md)
        self.assertEqual(note.__repr__(),f"Title: Untitled Note\t Tags: []\nCreated: {datetime.now().date()}\tLast Edited: {datetime.now().date()}\nNote length: 4\ntest")
    def test_str(self):
        md = "test"
        note = Note(md)
        self.assertEqual(str(note),f"Title: Untitled Note\t Tags: []\nCreated: {datetime.now().date()}\tLast Edited: {datetime.now().date()}\nNote length: 4")
    def test_header(self):
        md = """
---
title: Testnote
tags: [test, testcase, tests]
created: 2077-08-19
last_modified: 1988-09-19
---
test note with normal header
"""
        note = Note(md)
        self.assertEqual(note.yaml_header,"\ntitle: Testnote\ntags: [test, testcase, tests]\ncreated: 2077-08-19\nlast_modified: 1988-09-19\n")
        self.assertEqual(note.title,"Testnote")
        self.assertEqual(note.tags,["test","testcase","tests"])
        self.assertEqual(note.created_date,datetime(2077, 8, 19, 0, 0))
        self.assertEqual(note.modified_date,datetime(1988, 9, 19, 0, 0))
    
    #it should be fine to choose what ever date to input in created/last_modified as long as its valid
    # if its not valid it will default to current date
    def test_invalid_yaml_date(self):
        md = """
---
created = 2077/17/19
last_modifed = 1988/19/19
---
test note with normal(?) header
"""
        note = Note(md)
        self.assertEqual(note.created_date.date(),datetime.now().date())
        self.assertEqual(note.modified_date.date(),datetime.now().date())
    def test_date(self):
        md = """
---
created: 2077-17-19
last_modifed: 1988-19-19
---
test note with normal(?) header
"""
        note = Note(md)
        self.assertEqual(note.created_date.date(),datetime.now().date())
        self.assertEqual(note.modified_date.date(),datetime.now().date())
if __name__ == "__main__":
    unittest.main()
