import heapq
from itertools import count

class TriageSystem:
    def __init__(self):
        self._arrival_counter = count()
        self._triage_heap = []

    def add_patient(self, priority, task):
        #negative priorities(-5 is first, -1 is last)
        heapq.heappush(self._triage_heap, (priority, next(self._arrival_counter), task))

    def get_patient(self):
        return heapq.heappop(self._triage_heap)



system = TriageSystem()
system.add_patient(-3, "Abby")
system.add_patient(-1, "Lawrence")
system.add_patient(-3, "Catherine")
system.add_patient(-5, "Diego")
system.add_patient(-1, "Julian")
system.add_patient(-4, "Roach")
print(system.get_patient())