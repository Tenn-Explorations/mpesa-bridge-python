from python_graphql_client import GraphqlClient

class Client:
    api_key = ""
    base_url = ""

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def request_payment(self, amount_in_cents, phone) -> dict:
        if self.api_key == "" or self.base_url == "":
            raise Exception("Please set the api key and base url")

        try:
            amount_in_cents = int(amount_in_cents)
        except ValueError:
            raise Exception("Amount must be an integer")
        if amount_in_cents < 100:
            raise Exception("You can only request amounts greater than 1 shilling")

        try:
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
        except:
            raise Exception("Something went wrong while sending the request. Please confirm you have the right API key and base url. If the problem persists, please contact support")


    def fetch_transaction(self, transaction_id):
        if self.api_key == "" or self.base_url == "":
            raise Exception("Please set the api key and base url")
        if transaction_id == "":
            raise Exception("Please provide a transaction id")

        try:
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
        except:
            raise Exception("Something went wrong while sending the request. Please confirm you have the right API key and base url. If the problem persists, please contact support")


