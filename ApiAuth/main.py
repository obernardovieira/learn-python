import pyotp
# import time
import qrcode

# totp = pyotp.TOTP('base32secret3232')
# dick = totp.now()
# print(dick) # => 492039

# OTP verified for current time
# print(totp.verify(dick)) # => True
# time.sleep(30)
# print(totp.verify(dick)) # => False

base = pyotp.random_base32()
totp = pyotp.totp.TOTP(base)
print(base)
app_account_ref = "alice@google.com"
app_name = "Secure App"
uri = totp.provisioning_uri(app_account_ref, issuer_name=app_name)
print(uri)

img = qrcode.make(uri)
img.save("myqr.png")

auth_code = input("write your code:")
print("Current OTP:", totp.now())
if int(totp.now()) == int(auth_code):
    print("Great")
else:
    print("No")

