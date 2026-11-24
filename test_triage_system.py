import unittest
from triage_system import TriageSystem


class TestTriageSystem(unittest.TestCase):

    def setUp(self):
        self.triage_system = TriageSystem()

    def test_push(self):
        self.triage_system.add_patient(-1, "Lawrence")

        self.assertEqual(self.triage_system.queue_size(), 1)
        self.assertEqual(self.triage_system.peek_patient()[0], -1)
        self.assertEqual(self.triage_system.peek_patient()[2], "Lawrence")



if __name__ == "__main__":
    unittest.main()