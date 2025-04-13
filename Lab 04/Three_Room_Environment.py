import random
import time

class ThreeRoomVacuumEnvironment:
    def __init__(self):
        self.rooms = ['A', 'B', 'C']
        self.room_status = {room: random.choice(['Dirty', 'Clean']) for room in self.rooms}
        self.agent_location = random.choice(self.rooms)
        self.score = 0
        self.time_elapsed = 0
    
    def display(self):
        print(f"Time: {self.time_elapsed}s | Score: {self.score}")
        for room in self.rooms:
            status = "Dirty" if self.room_status[room] == 'Dirty' else "Clean"
            agent = "*" if room == self.agent_location else " "
            print(f"[{room}]{agent} {status}")
        print("------------------------")
    
    def update_score(self, action):
        # Scoring rules:
        # -1 for moving
        # +25 for cleaning
        # -10 per dirty room (penalty for leaving rooms dirty)
        if action == "Move":
            self.score -= 1
        elif action == "Clean":
            self.score += 25
        
        # Penalty for dirty rooms
        dirty_count = sum(1 for status in self.room_status.values() if status == 'Dirty')
        self.score -= dirty_count * 10
    
    def step(self):
        # Agent perceives current room status
        current_room_status = self.room_status[self.agent_location]
        
        # Agent decides action
        if current_room_status == 'Dirty':
            action = "Clean"
            self.room_status[self.agent_location] = 'Clean'
        else:
            action = "Move"
            # Move to a random adjacent room (for simplicity)
            adjacent_rooms = [r for r in self.rooms if r != self.agent_location]
            self.agent_location = random.choice(adjacent_rooms)
        
        # Update score based on action
        self.update_score(action)
        self.time_elapsed += 1
        self.display()
        time.sleep(1)  # Pause for 1 second between actions

# Run the environment
def run_three_room_environment(steps=20):
    env = ThreeRoomVacuumEnvironment()
    print("Initial State:")
    env.display()
    for _ in range(steps):
        env.step()
    print(f"Final Score: {env.score}")

run_three_room_environment()