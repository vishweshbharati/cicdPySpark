# tests/test_main.py
import unittest
from mock import patch
from src.main import count_words

class TestMain(unittest.TestCase):

    @patch('src.main.SparkSession')
    def test_count_words(self, mock_spark):
        mock_spark.builder.appName().getOrCreate().sparkContext.textFile().flatMap().countByValue.return_value = {'hello': 2, 'world': 1}
        result = count_words('file.txt')
        self.assertEqual(result, {'hello': 2, 'world': 1})
