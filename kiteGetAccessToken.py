import kitesettings
from kiteconnect import KiteConnect
import webbrowser

kite = KiteConnect(kitesettings.API_KEY)
print(kite.login_url())
webbrowser.open(kite.login_url(), new=0)
reqt_token = input("Request Token: ")
gen_ssn = kite.generate_session(request_token=reqt_token, api_secret=kitesettings.api_secret)
acc_tok = gen_ssn['access_token']
print("Access Token: ", acc_tok)
kite.set_access_token(acc_tok)
