
import matplotlib.pyplot as plt

class Voter:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.vote = None

class VotingSystem:
    def __init__(self):
        self.voters = []
        self.results = {}

    def register_voter(self, name, age, address):
        if age < 18:
            print("Sorry, you are not permitted to vote.")
            return
        new_voter = Voter(name, age, address)
        self.voters.append(new_voter)

    def vote(self, voter, candidate):
        if voter.age >= 18:
            voter.vote = candidate
            if candidate in self.results:
                self.results[candidate] += 1
            else:
                self.results[candidate] = 1
            print(f"Thank you, {voter.name}, for voting for {candidate}.")

    def show_results(self):
        if not self.results:
            print("No votes recorded yet.")
            return
        print("Voting Results:")
        for candidate, votes in self.results.items():
            print(f"{candidate}: {votes} votes")
        candidates = list(self.results.keys())
        votes = list(self.results.values())
        plt.bar(candidates, votes)
        plt.xlabel('Candidates')
        plt.ylabel('Number of Votes')
        plt.title('Voting Results')
        plt.show()

# Example usage:
voting_system = VotingSystem()

# Register voters
voting_system.register_voter("John", 22, "123 Main St")
voting_system.register_voter("Alice", 17, "456 Elm St")  # Under 18, cannot vote
voting_system.register_voter("Bob", 25, "789 Oak St")

# Vote
voting_system.vote(voting_system.voters[0], "Candidate A")
voting_system.vote(voting_system.voters[1], "Candidate B")
voting_system.vote(voting_system.voters[0], "Candidate B")

# Show results
voting_system.show_results()
