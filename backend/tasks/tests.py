from django.test import TestCase
from .scoring import calculate_priority

class ScoringTests(TestCase):
    def test_score_calculation(self):
        task = {
            "title": "Test",
            "due_date": "2025-12-01",
            "estimated_hours": 2,
            "importance": 8,
            "dependencies": []
        }
        score = calculate_priority(task)
        self.assertTrue(score > 0)
