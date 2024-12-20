from ics import Calendar, Event
from datetime import datetime, timedelta

# Initialize the calendar
calendar = Calendar()

# Define the start date
start_date = datetime.now()

# Updated schedule (tasks to be added only on weekdays)
tasks = [
    # Week 1: Foundations
    ("Arrays & Hashing", ["Review NeetCode's video explanations on arrays and hashing.", 
                          "Solve 2-3 problems from the 'Arrays & Hashing' section."]),
    ("Two Pointers", ["Watch tutorials on two-pointer methods.", "Solve 3 two-pointer problems."]),
    ("Sliding Window", ["Study sliding window strategies.", "Solve 3 sliding window problems."]),
    ("Stacks", ["Study NeetCode's explanations on stack operations.", "Solve 3 stack problems."]),
    ("Queues", ["Understand queue operations and their uses.", "Solve 3 queue problems."]),
    ("Binary Search", ["Review binary search concepts.", "Solve 3 binary search problems."]),
    ("Review & Practice (Week 1)", ["Review Week 1 topics.", "Revisit challenging problems.", 
                                    "Solve 2 new problems from any covered topic."]),
    
    # Week 2: Intermediate Concepts
    ("Linked List", ["Watch NeetCode's linked list tutorials.", "Solve 3 linked list problems."]),
    ("Trees - Basics", ["Learn tree traversal methods.", "Solve 3 basic tree problems."]),
    ("Trees - Advanced", ["Understand advanced tree algorithms.", "Solve 3 advanced tree problems."]),
    ("Tries", ["Study NeetCode's videos on tries.", "Solve 2 trie-related problems."]),
    ("Backtracking", ["Learn backtracking strategies.", "Solve 3 backtracking problems."]),
    ("Heaps & Priority Queue", ["Study heap operations.", "Solve 3 heap-related problems."]),
    ("Review & Practice (Week 2)", ["Review Week 2 topics.", "Revisit challenging problems.", 
                                    "Solve 2 new problems from any covered topic."]),
    
    # Week 3: Advanced Concepts
    ("Graphs - Basics", ["Learn graph representations and traversals.", "Solve 3 graph problems."]),
    ("Graphs - Advanced", ["Study advanced graph algorithms.", "Solve 3 advanced graph problems."]),
    ("Dynamic Programming (DP) - Basics", ["Watch NeetCode's DP explanations.", 
                                           "Solve 3 basic DP problems."]),
    ("Dynamic Programming (DP) - Advanced", ["Learn advanced DP strategies.", 
                                             "Solve 3 advanced DP problems."]),
    ("Greedy Algorithms", ["Understand greedy strategies.", "Solve 3 greedy algorithm problems."]),
    ("Intervals", ["Learn interval-related problem-solving techniques.", 
                   "Solve 3 interval problems."]),
    ("Final Review & Mock Assessment", ["Review all notes and problem solutions.", 
                                        "Identify weak areas.", 
                                        "Take a timed assessment with problems from different topics."])
]

# Add tasks to the calendar, skipping weekends
current_date = start_date
for title, task_list in tasks:
    # Skip weekends
    while current_date.weekday() >= 5:  # Saturday (5) or Sunday (6)
        current_date += timedelta(days=1)

    # Create and add the event
    event = Event()
    event.name = title
    event.begin = current_date
    event.description = "\n".join(task_list)
    event.duration = timedelta(hours=2)  # Assuming 2 hours per task
    calendar.events.add(event)

    # Move to the next day
    current_date += timedelta(days=1)

# Save the calendar to a .ics file
calendar_path = "NeetCode_Roadmap_Calendar.ics"
with open(calendar_path, 'w') as f:
    f.writelines(calendar)

print(f"Calendar saved as {calendar_path}")
