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
        return heapq.heappop(self._triage_heap)

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

        


system = TriageSystem()
system.add_patient(-1, "Lawrence")
system.add_patient(-3, "Catherine")
system.add_patient(-5, "Diego")
system.add_patient(-1, "Julian")
system.add_patient(-4, "Roach")
print(system.peek_patient())
print(system.queue_size())

system.clear_queue()

print(system.queue_size())
print(system.peek_patient())