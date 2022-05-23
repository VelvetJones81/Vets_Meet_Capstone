from rest_framework import serializers
from .models import VeteranUser

class VeteranUser(serializers.ModelSerializer):
    class Meta:
        model = VeteranUser
        fields = ["id", "first_name", "last_name", "email_address", "address", "city", "state", "zip_code","branch_id", "rank_id", "time_served"]
        depth = 1
        
    branch_id = serializers.IntegerField(write_only=True)
    rank_id = serializers.IntegerField(write_only=True)