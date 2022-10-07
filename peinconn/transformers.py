from .extensions import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'created_At', 'updated_At')

        interests = ma.Nested("InterestSchema")
        country = ma.Nested("CountrySchema") 

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'created_At', 'updated_At')     

class InterestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'hobby', 'created_At', 'updated_At')    

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

class LikedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'user', 'activity_id', 'activity', 'created_At', 'updated_At')

        user = ma.Nested("UserSchema")
        activity = ma.Nested("ActivitySchema", exclude("user",)) 
