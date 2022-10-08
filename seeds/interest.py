from flask_seeder import Seeder, Faker
from peinconn.peinconn.models import Interest
from peinconn.peinconn.extensions import db

hobbies = {'Reading':'https://f.hubspotusercontent30.net/hubfs/5191137/blog/Blog-10-essential-reads-to-improve-reading-comprehension.jpg', 
'Music':'https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/YT_Music.jpg', 
'Sports':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTI1fZ6SlO7pKo8MfWfniskSb5DXHmD7bsHKw&usqp=CAU', 
'Travelling':'https://thumbs.dreamstime.com/b/passport-flight-fly-travelling-travel-citizenship-concept-airplane-traveller-air-stock-image-86057681.jpg', 
'Painting':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtk-VLE8iCEvqguV96IwvtFa9IiGD8TKq3Zw&usqp=CAU', 
'Movies':'https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/101631641/original/417f783ed60d8acbaf9eda4b51494627abb0255e/recomend-you-movies-in-genre-u-want.jpg', 
'Photography':'https://www.adorama.com/alc/wp-content/uploads/2017/06/2-shutterstock_172791128.jpg', 
'Writing':'https://sweetlovemessages.com/wp-content/uploads/2021/02/How-to-Make-Writing-Your-Favorite-Hobby.jpg', 
'Dancing':'https://bath.co.uk/wp-content/uploads/2011/05/fitness-dance.jpg', 
'Cooking':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxfZuOo-vTGRPDh5JgYmG78kIYAx4OMAIHg&usqp=CAU', 
'Christianity':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIvftzi9-_kM2ugb5wlzz0qI_s1WjZbrGJwg&usqp=CAU', 
'Knitting':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTFSG2mQ07l_DhBeydX19vCaISA9qPNo76Pw&usqp=CAU', 
'Fashion':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1Pj5ep4oDYP-lutEp6r1zR3ExYeKhzPh6Aw&usqp=CAU', 
'Pottery':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuuyj_WLlhMvS5AjxCwVBAiciDsR3OwBUntw&usqp=CAU', 
'Coding':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHH4LCiIDn-OGwk8lPD60LVUYGhuFKxmGKOQ&usqp=CAU', 
'Mixology':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6G78S2q5MfNuanQ4h8bt6uzPgWR6RTRxjxQ&usqp=CAU'}

class InterestSeeder(Seeder):
    def run(self):
        fakers = []
        for key, value in hobbies.items():
            faker = Faker(
                cls=Interest,
                init={
                    "hobby": key.lower(),
                    "hobby_image": value
                }
            )
            fakers.append(faker)

        for faker in fakers:
            for interest in faker.create(1):  
                self.db.session.add(interest) 