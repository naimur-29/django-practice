from datetime import datetime
from rest_framework import serializers
from mongoengine import Document, EmbeddedDocument, ObjectIdField, StringField, DateTimeField, EmbeddedDocumentField, BooleanField

class Name(EmbeddedDocument):
    first_name = StringField()
    last_name = StringField()

class Guardian(EmbeddedDocument):
    pass

class LocalGuardian(EmbeddedDocument):
    pass

class Student(Document):
    pk_id = ObjectIdField(primary_key=True)
    id = StringField()
    fk_user = ObjectIdField()
    name = EmbeddedDocumentField(Name)
    gender = StringField()
    date_of_birth = DateTimeField()
    email = StringField()
    contact_no = StringField()
    emergency_contact_no = StringField()
    present_address = StringField()
    permanent_address = StringField()
    guardian = EmbeddedDocumentField(Guardian)
    local_guardian = EmbeddedDocumentField(LocalGuardian)
    profile_image = StringField()
    academic_department = ObjectIdField()
    is_deleted = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    
    meta = {'collection': 'students'}
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Student
        fields = '__all__'
