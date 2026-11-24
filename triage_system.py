from heapq import heappush as _heappush, heappop as _heappop
from itertools import count

class TriageSystem:
    def __init__(self):
        self._arrival_counter = count()
        self._triage_heap = []

    def heappush(self, priority, task):
        _heappush(self._triage_heap,(priority, next(self._arrival_counter), task))

    def heappop(self):
        priority, arrival_order, task = _heappop(self._triage_heap)
        return task



system = TriageSystem()
system.heappush(system, (3, next(system._arrival_counter), "Task A"))

priority, arrival_order, task = system.heappop()
print(task)