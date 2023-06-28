from authorizenet import apicontractsv1
from authorizenet.apicontrollers import getSettledBatchListController
api_login_id = '92gDrV9HsJ'
transaction_key = '9553wQY586rTGaa4'

# Crear una instancia del controlador de lista de lotes liquidados
settled_batch_list_controller = getSettledBatchListController()

# Configurar las credenciales de autenticación
settled_batch_list_controller.setenvironment(os.environ.get('AUTHORIZE_NET_ENVIRONMENT'))
settled_batch_list_controller.setmerchantauthentication(api_login_id, transaction_key)

# Configurar los parámetros de la consulta
request = apicontractsv1.GetSettledBatchListRequest()
request.firstSettlementDate = "2023-06-01"
request.lastSettlementDate = "2023-06-27"

# Obtener la lista de lotes liquidados
response = settled_batch_list_controller.get_settled_batch_list(request)

# Procesar la respuesta
if response is not None:
    if response.messages.resultCode == "Ok":
        for batch in response.batchList:
            for transaction in batch.transactions:
                print("ID de transacción:", transaction.transId)
                print("Importe:", transaction.settleAmount)
                print("Estado:", transaction.transactionStatus)
    else:
        print("Código de respuesta:", response.messages.resultCode)
        print("Mensaje de error:", response.messages.message[0].text)
else:
    print("No se recibió respuesta")