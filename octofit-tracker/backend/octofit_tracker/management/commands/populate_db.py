from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_data
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = []
        for user_data in test_data['users']:
            user = User(_id=ObjectId(), **user_data)
            user.save()
            users.append(user)

        # Create teams
        for team_data in test_data['teams']:
            team = Team(_id=ObjectId(), name=team_data['name'])
            team.save()
            for username in team_data['members']:
                team.members.add(next(user for user in users if user.username == username))

        # Create activities
        for activity_data in test_data['activities']:
            user = next(user for user in users if user.username == activity_data['user'])
            activity = Activity(_id=ObjectId(), user=user, activity_type=activity_data['activity_type'], duration=timedelta(hours=int(activity_data['duration'].split(':')[0]), minutes=int(activity_data['duration'].split(':')[1])))
            activity.save()

        # Create leaderboard entries
        for leaderboard_data in test_data['leaderboard']:
            user = next(user for user in users if user.username == leaderboard_data['user'])
            leaderboard = Leaderboard(_id=ObjectId(), user=user, score=leaderboard_data['score'])
            leaderboard.save()

        # Create workouts
        for workout_data in test_data['workouts']:
            workout = Workout(_id=ObjectId(), **workout_data)
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
