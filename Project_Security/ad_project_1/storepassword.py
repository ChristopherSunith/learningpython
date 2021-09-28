#usage of bcrypt to secure password and print hashed password

import bcrypt

passwd = b'mark@1124'

#Hash a passwd for the first time
hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())

print ("Password hash is: " , hashed)

