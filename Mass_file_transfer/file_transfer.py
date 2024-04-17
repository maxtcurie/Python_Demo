from globus_sdk import NativeAppAuthClient

CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
client = NativeAppAuthClient(CLIENT_ID)
client.oauth2_start_flow(refresh_tokens=True)

authorize_url = client.oauth2_get_authorize_url()
print('Visit this URL to authorize the application:', authorize_url)
