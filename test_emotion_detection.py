import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am very angry")
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], 'sadness')

if __name__ == "__main__":
    unittest.main()