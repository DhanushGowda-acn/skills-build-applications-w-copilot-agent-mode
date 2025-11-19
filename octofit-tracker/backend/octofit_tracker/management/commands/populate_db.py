from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data (delete individually)
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in User.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        thor = User.objects.create(name='Thor', email='thor@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2025-11-19')
        Activity.objects.create(user=batman, type='Cycling', duration=45, calories=400, date='2025-11-19')
        Activity.objects.create(user=thor, type='Swimming', duration=60, calories=500, date='2025-11-19')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body strength', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Core strength', difficulty='Hard')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
