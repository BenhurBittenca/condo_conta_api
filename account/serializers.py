from rest_framework import serializers, validators
from account import models


class CurrentAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.currentAccount
        fields = '__all__'    

        validators = [
            validators.UniqueTogetherValidator(
                queryset=models.currentAccount.objects.filter(),
                fields=['owner_id'],
                message="Já existe uma conta corrente cadastrada com o ID do proprietário informado!"
            )
        ]


class SavingsAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.savingsAccount    
        fields = '__all__'        

        validators = [
            validators.UniqueTogetherValidator(
                queryset=models.savingsAccount.objects.filter(),
                fields=['owner_id'],
                message="Já existe uma conta poupança cadastrada com o ID do proprietário informado!"
            )
        ]


class AccountHistorySerializer(serializers.ModelSerializer):
    current_account_value = serializers.SerializerMethodField()
    savings_account_value = serializers.SerializerMethodField()

    class Meta:
        model = models.accountHistory
        fields = ('date', 'description', 'value', 'current_account_value', 'savings_account_value')

    def get_current_account_value(self, obj):    
        if obj.current_account:
            return obj.current_account.account_value

    def get_savings_account_value(self, obj):        
        if obj.savings_account:
            return obj.savings_account.account_value        