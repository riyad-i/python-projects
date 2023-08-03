class User:
    def __init__(self, papers=10):
        self.papers = papers
    def double_paper(self):
        self.papers *= 2


user1 = User(16)
print(user1.papers)
user2 = User()

print(user2.papers + user1.papers)
user1.double_paper()
print(user1.papers)
user1.double_paper()
user1.double_paper()
print(user1.papers)
