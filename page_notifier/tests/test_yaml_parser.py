import unittest

from libs.yaml_parser import YamlParser

class TestYamlParser(unittest.TestCase):

    def test_parse(self):
        p = YamlParser()
        p.parse('./tests/test_links.yaml')
        self.assertEqual(len(p.urls), 2)
        self.assertEqual(p.urls[0], "http://quotes.toscrape.com/page/1/")