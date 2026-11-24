import heapq
from itertools import count

class TriageSystem:
    def __init__(self):
        self._arrival_counter = count()
        self._triage_heap = []

    def add_patient(self, priority, task):
        #negative priorities(-5 is first, -1 is last)
        heapq.heappush(self._triage_heap, (priority, next(self._arrival_counter), task))

    def process_patient(self):
        return heapq.heappop(self._triage_heap)

    def queue_empty(self):
        return len(self._triage_heap) == 0

    def queue_size(self):
        return len(self._triage_heap)

    def peek_patient(self):
        if not self.queue_empty():
            return self._triage_heap[0]
        else:
            return None


system = TriageSystem()
system.add_patient(-1, "Lawrence")
system.add_patient(-3, "Catherine")
system.add_patient(-5, "Diego")
system.add_patient(-1, "Julian")
system.add_patient(-4, "Roach")
print(system.peek_patient())
print(system.queue_size())
print(system.process_patient())