from rest_framework import serializers
from .models import Rank

class Rank(serializers.ModelSerializer):
    model = Rank
    fields = ["rank", "rank_id"]
    depth  = 1