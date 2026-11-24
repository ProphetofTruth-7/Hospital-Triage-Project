from heapq import heappush as _heappush, heappop as _heappop
from itertools import count

class TriageSystem:
    def __init__(self):
        self._arrival_counter = count()
        self._triage_heap = []



system = TriageSystem()

heapq.heappush(system._triage_heap, 4)