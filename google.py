from importlib_metadata import requires
import requests

# Google OAuth2
# clientId = '1063302825449-ejgqeu5q3sp1jr2ch0mjdqnmp8a753vm.apps.googleusercontent.com'
# clientSecret = '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'

redirectUri = 'https%3A%2F%2Flocalhost%3A9000%2Foauth%2Fgoogle%2Fcallback'

# uri = f'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id={clientId}&redirect_uri={redirectUri}&response_type=code&scope=email%20profile&flowName=GeneralOAuthFlow'

# code = '4/0AX4XfWgZ1qKH3VzW696nUCJXAWazX3D7p6UGZEGJU7EkVMiOaFIGpwhjYS8RrJHRzBxNcA'

# print(uri)

# body = {
#   'code': code,
#   'grant_type': 'authorization_code',
#   'client_id': clientId,
#   'client_secret': clientSecret,
#   'redirect_uri': 'http://localhost:9000/oauth/google/callback',
# }

# access = requests.post('https://www.googleapis.com/oauth2/v4/token', data=body, headers={
#   'Content-Type': 'application/x-www-form-urlencoded'
# }).json()

# res = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json', headers={
#   'Authorization': f"Bearer {access['access_token']}"
# })

# print(res.json())

# Facebook OAuth2
appId = '693452471833848'
appSecret = '29b4571e4e2e94842a947ab4fd1af6a2'

uri = f'https://www.facebook.com/v10.0/dialog/oauth?response_type=code&display=popup&client_id={appId}&redirect_uri={redirectUri}&scope=email%2Cpublic_profile'

# print(uri)

code = 'AQA1iAey-WDGr-bJ-F0TXKogCzBceNpiUyNy6b0iN33THKuGQske1NCg4bKag0cTr1Lg8m-0R2HFhsFNTWo8NiwJx02yIEtZ8oMQ2Yv5XU-D5Sm2bHMJrYMLLr_FXwD5KOg8yj3TmgvvN1f319KhPW6spyP_joM0X5qd_AoZLndHl9gnwrWEqvig8K0i3R73mMLWvg3jiunU3rC8-PUF7UkIHcXXGQh5Z2G0B_6kfA-6necrCYPoMg_4ua1iiIOOA87R-WNuNr8-b_gSTfcoR_1-T6oF3uEJVNG2SvR6DcwGPNH4KDpEzsdB35Bla_1YZqdTlHFMaVcq2l5TVtwSVJQijrcHhh3LKdG9cOeQXV_qzEZ_I8o-NRnrNg9AIsTbHch6MUYIT3HVHpQ0uwz2eSN-#_=_'

tokenUri = f'https://graph.facebook.com/v2.4/oauth/access_token?redirect_uri={redirectUri}&client_id={appId}&client_secret={appSecret}&code={code}'

access = requests.get(tokenUri).json()

res = requests.get('https://graph.facebook.com/v10.0/me?fields=id,first_name,last_name,email,picture', headers={
  'Authorization': f"Bearer {access['access_token']}"
})

print(res)
