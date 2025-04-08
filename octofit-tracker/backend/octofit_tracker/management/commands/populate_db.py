from django.core.management.base import BaseCommand
from octofit_tracker.settings import MONGO_DB
from octofit_tracker.sample_data import test_data
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        MONGO_DB['users'].delete_many({})
        MONGO_DB['teams'].delete_many({})
        MONGO_DB['activities'].delete_many({})
        MONGO_DB['leaderboard'].delete_many({})
        MONGO_DB['workouts'].delete_many({})

        # Populate users
        users = {}
        for user_data in test_data['users']:
            # Debug: Log user creation
            self.stdout.write(self.style.NOTICE(f"Creating user: {user_data['username']}"))
            user_id = MONGO_DB['users'].insert_one(user_data).inserted_id
            users[user_data['username']] = user_id

        # Populate teams
        for team_data in test_data['teams']:
            # Debug: Log team creation
            self.stdout.write(self.style.NOTICE(f"Creating team: {team_data['name']}"))
            team_data['members'] = [users[username] for username in team_data['members']]
            MONGO_DB['teams'].insert_one(team_data)

        # Populate activities
        for activity_data in test_data['activities']:
            # Debug: Log activity creation
            self.stdout.write(self.style.NOTICE(f"Creating activity for user: {activity_data['user']}"))
            activity_data['user'] = users[activity_data['user']]
            MONGO_DB['activities'].insert_one(activity_data)

        # Populate leaderboard
        for idx, leaderboard_data in enumerate(test_data['leaderboard']):
            leaderboard_data['leaderboard_id'] = idx  # Assign a unique ID
            leaderboard_data['user'] = users[leaderboard_data['user']]
            MONGO_DB['leaderboard'].insert_one(leaderboard_data)

        # Populate workouts
        for idx, workout_data in enumerate(test_data['workouts']):
            # Debug: Log workout creation
            self.stdout.write(self.style.NOTICE(f"Creating workout: {workout_data['name']}"))
            workout_data['workout_id'] = idx  # Assign a unique ID
            MONGO_DB['workouts'].insert_one(workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
