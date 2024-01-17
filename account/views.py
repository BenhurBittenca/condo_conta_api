from rest_framework.views import APIView
from account import models, serializers
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404

class currentAccountViewSet(APIView):

    def get_current_account(self, account_id):
        try:
            return models.currentAccount.objects.get(id=account_id)
        except models.currentAccount.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = serializers.CurrentAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        current_account = self.get_current_account(pk)
        serializer = serializers.CurrentAccountSerializer(current_account, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        
    def get(self, request):
        print('entrou no get')
        

class savingsAccountViewSet(APIView):

    def get_savings_account(self, account_id):
        try:
            return models.savingsAccount.objects.get(id=account_id)
        except models.savingsAccount.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = serializers.SavingsAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        current_account = self.get_savings_account(pk)
        serializer = serializers.SavingsAccountSerializer(current_account, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        

class getAccountViewSet(APIView):
    def get(self, request):
        owner_id = request.query_params.get('owner_id', None)
        type_account = request.query_params.get('type_account', None)

        if not owner_id:
            return Response('Owner ID da conta não informado!', status=400) 
        
        if not type_account:
            return Response('Tipo da conta bancária que deseja consultar não informado, opções: current OU savings!', status=400) 
        
        if type_account == 'current':
            account = get_object_or_404(models.currentAccount, owner_id=owner_id)
            serializer = serializers.CurrentAccountSerializer(account)
        else:
            account = get_object_or_404(models.savingsAccount, owner_id=owner_id)
            serializer = serializers.SavingsAccountSerializer(account)

        return Response(serializer.data)
    

class transferAccountViewSet(APIView):

    def post(self, request):
        owner_id = request.query_params.get('owner_id', None)
        transfer_type = request.query_params.get('transfer_type', None)

        if request.data['value'] <= 0:
            return Response('Valor da transferência não informado', status=400)                            
    
        current_account = models.currentAccount.objects.filter(owner_id=owner_id)
        if not current_account:
            return Response('Owner ID da conta corrente não localizado', status=400)                            
        
        savings_account = models.savingsAccount.objects.filter(owner_id=owner_id)
        if not savings_account:
            return Response('Owner ID da conta poupança não localizado', status=400)  
                                  
        if transfer_type == 'investment':            
            request.data['current_account'] = current_account[0].id
            current_value = (current_account[0].account_value - request.data['value'])
            savings_value = (savings_account[0].account_value + request.data['value'])
            models.currentAccount.objects.select_for_update().filter(id=current_account[0].id).update(account_value=current_value)
            models.savingsAccount.objects.select_for_update().filter(id=savings_account[0].id).update(account_value=savings_value)

        else:                        
            request.data['savings_account'] = savings_account[0].id
            current_value = (current_account[0].account_value + request.data['value'])
            savings_value = (savings_account[0].account_value - request.data['value'])
            models.currentAccount.objects.select_for_update().filter(id=current_account[0].id).update(account_value=current_value)
            models.savingsAccount.objects.select_for_update().filter(id=savings_account[0].id).update(account_value=savings_value)

        serializer = serializers.AccountHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data, status=200)
        return Response('', status=200)