from .extensions import ma

#User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'created_At', 'updated_At')

        interests = ma.Nested("InterestSchema")
        country = ma.Nested("CountrySchema") 

#Init User Schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)        

#Country Schema
class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'created_At', 'updated_At')  

#Init Country Schema
country_schema = CountrySchema(strict=True)
countries_schema = CountrySchema(many=True, strict=True) 

#Interest Schema
class InterestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'hobby', 'created_At', 'updated_At')   

#Init Interest Schema
interest_schema = InterestSchema(strict=True)
interests_schema = InterestSchema(many=True, strict=True)          

#Activity Schema
class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'user', 'activity', 'picture', 'interest', 'like_no', 'created_At', 'updated_At')    

        user = ma.Nested("UserSchema")
        interest = ma.Nested("InterestSchema")  

        # links = ma.Hyperlinks({
        #     'firstPage':
        #     'lastPage':
        #     'prevPage':
        #     'nextPage':
        #     'meta': {
        #         'paging': {
        #         'paegCount':
        #         'totalPages':
        #         'page':
        #         'hasPrevPage':
        #         'hasNextPage':
        #         }
        #     }
        # })

#Init Activity Schema
activity_schema = ActivitySchema(strict=True)
activities_schema = ActivitySchema(many=True, strict=True)         

#Liked Schema
class LikedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'user', 'activity_id', 'activity', 'created_At', 'updated_At')

        user = ma.Nested("UserSchema")
        activity = ma.Nested("ActivitySchema", exclude("user",)) 

#Init Liked Schema
liked_schema = LikedSchema(strict=True)        
