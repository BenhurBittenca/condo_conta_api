from django.db.models import (
    ForeignKey, 
    RESTRICT, 
    Model, 
    UUIDField, 
    DateTimeField, 
    CharField, 
    IntegerField, 
    FloatField
)
from uuid import uuid4
from django.utils import timezone


class currentAccount(Model):    
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_id = IntegerField()
    owner_name = CharField(max_length=255)
    account_value = FloatField()

    def __str__(self):
        return f"{self.owner_name} - {self.account_value}"
    

class savingsAccount(Model):    
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_id = IntegerField()
    owner_name = CharField(max_length=255)
    account_value = FloatField()

    def __str__(self):
        return f"{self.owner_name} - {self.account_value}"
    

class accountHistory(Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    savings_account = ForeignKey(savingsAccount, on_delete=RESTRICT, null=True, blank=True)
    current_account = ForeignKey(currentAccount, on_delete=RESTRICT, null=True, blank=True)
    date = DateTimeField(default=timezone.now)
    description = CharField(max_length=255)
    value = FloatField()

    def __str__(self):
        return f"{self.description} - {self.value}"


