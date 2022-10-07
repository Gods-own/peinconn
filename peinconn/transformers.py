from .extensions import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'created_At', 'updated_At')

        interests = ma.Nested(InterestSchema)

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'created_At', 'updated_At')

        interests = ma.Nested(InterestSchema)        