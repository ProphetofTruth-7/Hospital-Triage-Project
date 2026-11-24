import unittest
from triage_system import TriageSystem


class TestTriageSystem(unittest.TestCase):

    def setUp(self):
        self.triage_system = TriageSystem()

    def test_invariant_peek(self):
        self.triage_system.add_patient(-1, "Lawrence")
        self.triage_system.add_patient(-4, "Joshua")
        self.triage_system.add_patient(-3, "Caleb")

        self.assertEqual(self.triage_system.queue_size(), 3)
        self.assertEqual(self.triage_system.peek_patient()[0], -4)
        self.assertEqual(self.triage_system.peek_patient()[2], "Joshua")
        self.assertEqual(self.triage_system.queue_size(), 3)

    def test_push_simple(self):
        self.triage_system.add_patient(-1, "Lawrence")

        self.assertEqual(self.triage_system.queue_size(), 1)
        self.assertEqual(self.triage_system.peek_patient()[0], -1)
        self.assertEqual(self.triage_system.peek_patient()[2], "Lawrence")

    def test_push_complex(self):
        self.triage_system.add_patient(-1, "Lawrence")
        self.triage_system.add_patient(-4, "Joshua")
        self.triage_system.add_patient(-3, "Caleb")

        self.assertEqual(self.triage_system.queue_size(), 3)
        self.assertEqual(self.triage_system.peek_patient()[0], -4)
        self.assertEqual(self.triage_system.peek_patient()[2], "Joshua")

    def test_pop_simple(self):
        self.triage_system.add_patient(-1, "Lawrence")
        self.triage_system.add_patient(-4, "Joshua")
        self.triage_system.add_patient(-3, "Caleb")

        self.assertEqual(self.triage_system.queue_size(), 3)
        self.assertEqual(self.triage_system.process_patient(), (-4, 1, "Joshua"))
        self.assertEqual(self.triage_system.queue_size(), 2)
        self.assertEqual(self.triage_system.peek_patient()[0], -3)
        self.assertEqual(self.triage_system.peek_patient()[2], "Caleb")

    def test_pop_full(self):
        self.triage_system.add_patient(-1, "Lawrence")
        self.triage_system.add_patient(-4, "Joshua")
        self.triage_system.add_patient(-3, "Caleb")

        self.assertEqual(self.triage_system.queue_size(), 3)
        self.assertEqual(self.triage_system.process_patient(), (-4, 1, "Joshua"))
        self.assertEqual(self.triage_system.process_patient(), (-3, 2, "Caleb"))
        self.assertEqual(self.triage_system.process_patient(), (-1, 0, "Lawrence"))
        self.assertEqual(self.triage_system.queue_size(), 0)

    def test_clear_queue(self):
        self.triage_system.add_patient(-1, "Lawrence")
        self.triage_system.add_patient(-4, "Joshua")
        self.triage_system.add_patient(-3, "Caleb")

        self.assertEqual(self.triage_system.queue_size(), 3)
        self.triage_system.clear_queue()
        self.assertEqual(self.triage_system.queue_size(), 0)


if __name__ == "__main__":
    unittest.main()