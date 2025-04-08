from octofit_tracker.settings import MONGO_DB
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/'
    })

# Example of a view using pymongo
@api_view(['GET'])
def get_users(request):
    users = list(MONGO_DB['users'].find({}, {'_id': 0}))  # Exclude MongoDB's _id field
    return Response(users)
