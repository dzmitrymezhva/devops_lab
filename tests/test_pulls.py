from unittest import TestCase
import json
import handlers.pulls


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_content_1(self):
        with open('data/empty_length.json') as f:
            response = json.load(f)
        result = handlers.pulls.content(response)
        self.assertEqual(len(result), 0)

    def test_content_2(self):
        with open("data/parsing.json") as f:
            response = json.load(f)
        result = handlers.pulls.content(response)
        variable = [{'created': '2020-09-23T00:08:34Z',
                     'link': 'https://github.com/alenaPy/devops_lab/pull/39',
                     'login': 'supreme8888', 'num': 39,
                     'title': 'Homework3: Viktor Gulinskiy'}]
        self.assertEqual(result, variable)

    def test_content_3(self):
        with open("data/length.json") as f:
            response = json.load(f)
        result = handlers.pulls.content(response)
        self.assertEqual(len(result), 10)

    def test_get_pulls_1(self):
        state = ["open", "closed", "needs work", "invalid", "all", "accepted"]
        for item in state:
            result = handlers.pulls.get_pulls(item)
            self.assertIsInstance(result, list)

    def test_get_pulls_2(self):
        result = handlers.pulls.get_pulls(None)
        self.assertIsInstance(result, list)

    def tearDown(self):
        """Finish"""
