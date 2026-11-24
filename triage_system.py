import heapq
from itertools import count

class TriageSystem:
    def __init__(self):
        self._arrival_counter = count()
        self._triage_heap = []

    def add_patient(self, priority, task):
        #negative priorities(-5 is first, -1 is last)
        if not task == "" and isinstance(task, str):
            if priority > -6 and priority < 0 and isinstance(priority, int):
                heapq.heappush(self._triage_heap, (priority, next(self._arrival_counter), task))
            else:
                raise ValueError("Invalid Priority")
        else:
            raise ValueError("Invalid Task")

    def process_patient(self):
        if not self.queue_empty():
            priority, arrival_number, patient = heapq.heappop(self._triage_heap)
            return (-priority, arrival_number, patient)
        else:
            return None

    def queue_empty(self):
        return len(self._triage_heap) == 0

    def queue_size(self):
        return len(self._triage_heap)

    def clear_queue(self):
        while not len(self._triage_heap) == 0:
            heapq.heappop(self._triage_heap)

    def peek_patient(self):
        if not self.queue_empty():
            return self._triage_heap[0]
        else:
            return None

        


