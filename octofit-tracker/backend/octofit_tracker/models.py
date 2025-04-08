# Remove djongo models and replace with plain Python classes or data structures
# Models will now be handled directly via pymongo

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

class Activity:
    def __init__(self, user, activity_type, duration):
        self.user = user
        self.activity_type = activity_type
        self.duration = duration

class Leaderboard:
    def __init__(self, user, score):
        self.user = user
        self.score = score

class Workout:
    def __init__(self, name, description):
        self.name = name
        self.description = description
