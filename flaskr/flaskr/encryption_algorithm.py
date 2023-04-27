## Reto ECSDA


#importing libraries
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.signature import Signature
from ellipticcurve.utils.file import File




### Testing code ####
# Generate Keys
privateKey = PrivateKey()
publicKey = privateKey.publicKey()

message = "My test message"

# Generate Signature
signature = Ecdsa.sign(message, privateKey)

# Verify if signature is valid
print (Ecdsa.verify(message, signature, publicKey))

### MAIN  ####

def ecsda():
    signatureDer = File.read("/Users/macuser/Documents/TEC UNI/TEC SEM.6/Cryptography/Reto ECSDA/Andyboi.txt", "rb")
    signature_test=signatureDer.decode("utf-8") 
    signature = Ecdsa.sign(signature_test, privateKey)

    # Verify if signature is valid
    print (Ecdsa.verify(signature_test, signature, publicKey))

