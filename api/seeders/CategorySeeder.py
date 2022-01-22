from django_seed import Seed
from faker.generator import random

from api.models import Category

seeder = Seed.seeder()

seeder.add_entity(Category, 10, {
    'id': lambda x: random.randint(0, 1000),
    'name': lambda x: seeder.faker.user_name(),
})
seeder.execute()
