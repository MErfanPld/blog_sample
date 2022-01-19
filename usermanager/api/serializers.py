from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from usermanager.models import User


# Register instance of model
class User_Register(serializers.ModelSerializer) :

    '''
    special for owner
    '''
    class Meta :
        model = User
        fields = (
            'groups','username','first_name',
            'last_name','password','email',
            'phone_number', "id"    
        )

    def to_internal_value(self, data) :
        ret = super().to_internal_value(data)
        

        hash_password = make_password(ret['password'])
        extra = {
            'password':hash_password,
            'is_superuser':True,
            'is_staff':True
        }
        for key,value in extra.items() :
            ret[key]=value

        return ret


    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret

 
