from triage_system import TriageSystem

triage_system = TriageSystem()

triage_system.add_patient(-5, "Sofia")
triage_system.add_patient(-2, "Bob")
triage_system.add_patient(-4, "Charlie")
triage_system.add_patient(-3, "Diana")
triage_system.add_patient(-1, "Eli")
triage_system.add_patient(-4, "Tom")
triage_system.add_patient(-5, "Alice")
triage_system.add_patient(-4, "Rachel")

while not triage_system.queue_empty():
    print(f"Peeked the next patient; {triage_system.peek_patient()[2]}. The size is still {triage_system.queue_size()}")
    print(f"The severity of this patient's injury was {triage_system.peek_patient()[0]}, and {triage_system.process_patient()[2]} was processed in a timely manner.")
    print()

print(f"The queue has been cleared. The current size(as expected) is {triage_system.queue_size()}")
print()
print(f"Peeking(returns {triage_system.peek_patient()}) and Processing (returns {triage_system.process_patient()}) on this queue returns none")