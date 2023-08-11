from python_graphql_client import GraphqlClient

class Client:
    api_key = ""
    base_url = ""

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def request_payment(self, amount_in_cents, phone) -> dict:
        client = GraphqlClient(endpoint=self.base_url)
        query = """
        mutation {
            initateDeposit(input:{
            amountInCents: %s,
            userPhoneNumber: "%s"
            }){
            Txid
            Status

            }
        }
        """ % (amount_in_cents, phone)

        # add headers
        headers = {
                "Authorization": "Bearer " + self.api_key,
                "Content-Type": "application/json"
        }

        data = client.execute(query=query, headers=headers)
        return data

    def fetch_transaction(self, transaction_id):
        client = GraphqlClient(endpoint=self.base_url)
        query = """
        query {
            fetchTransactionByTxId(input: "%s"){
            id
            amount
            type
            status
            mpesaReference
            }
        }
        """ % (transaction_id)

        # add headers
        headers = {
                "Authorization": "Bearer " + self.api_key,
                "Content-Type": "application/json"
        }

        data = client.execute(query=query, headers=headers)

        return data
