from flask_seeder import Seeder, Faker
from peinconn.peinconn.models import Country
from peinconn.peinconn.extensions import db
from country_list import countries_for_language

countries = dict(countries_for_language('en'))

class CountrySeeder(Seeder):
    def run(self):
        fakers = []
        for key, value in countries.items():
            faker = Faker(
                cls=Country,
                init={
                    "country_abbrev": key,
                    "country": value.lower()
                }
            )
            fakers.append(faker)

        for faker in fakers:
            for country in faker.create(1):  
                self.db.session.add(country) 