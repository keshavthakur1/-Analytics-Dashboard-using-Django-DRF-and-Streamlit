from rest_framework import serializers
from customer.models import Customer  # Correct import
from ..choice import GENDER_CHOICE

class GenderChoiceFieldSerializer(serializers.Field):
    def to_representation(self, obj):
        return dict(GENDER_CHOICE)[obj]
    
    def to_internal_value(self, data):
        return data
        
class CustomerSerializer(serializers.ModelSerializer):
    gender = GenderChoiceFieldSerializer()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'gender',
            'age',
            'favorite_number',  # Ensure this matches your model field
            'created',
        )

    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d')  # Formatting date properly
