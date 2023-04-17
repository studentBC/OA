import os
import random

from faker import Faker
import faker_commerce

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.db import connection

from app.models import User
from app.models import Project
from app.models import Audit


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = self.seed_users()
        self.seed_projects(users)
        self.seed_audits(users)
        print("Successfully completed the seeding process")

    def create_record_project(self, user):
        fake = Faker()
        fake.add_provider(faker_commerce.Provider)

        return Project.objects.create(
            title=fake.ecommerce_name(), description=fake.paragraph(), owner_id=user.id)

    def create_record_audit(self, user):
        fake = Faker()

        event = random.choice([
            'authentication:logout',
            'authentication:new',
            'invoice:create',
            'invoice:send',
            'settings:change',
        ])
        status = random.choice(['started', 'in progress', 'finished', 'error'])
        message = fake.paragraph()
        context = {}
        user_id = user.id

        return Audit.objects.create(event=event, status=status,
                                    message=message, context=context, user_id=user_id)

    def seed_users(self):
        print("Seeding [users]...")
        users = [
            User(
                email="test@example.com",
                password=make_password("password"),
                first_name="User",
                last_name="Test"
            ), User(
                email="test2@example.com",
                password=make_password("password"),
                first_name="User",
                last_name="Test 2"
            )
        ]

        return User.objects.bulk_create(users)

    def seed_projects(self, users):
        print("Seeding [projects]...")

        projects = []

        for _ in range(10):
            user = random.choice(users)
            project = self.create_record_project(user)
            projects.append(project)

        return projects

    def seed_audits(self, users):
        # Seed with fake data
        print('Seeding [audits]...')
        records = []

        try:
            for _ in range(100):
                user = random.choice(users)
                records.append(self.create_record_audit(user))
        except Exception as e:
            print(e)

        return records

    def clear_db(self):
        if os.getenv("ENV") != "test":
            raise Exception("ClearDB can only be run on TEST DB!!!")

        # Clear [projects] and restart the sequence
        Project.objects.all().delete()
        User.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE app_project_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE auth_user_id_seq RESTART WITH 1")

        print("Successfully cleared the DB")
