from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa

# Load the certificate from file
with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb') as f:
    cert_bytes = f.read()

# Parse the certificate
cert = x509.load_der_x509_certificate(cert_bytes)

# Extract the public key and modulus
public_key = cert.public_key()
if isinstance(public_key, rsa.RSAPublicKey):
    modulus = public_key.public_numbers().n
    print(modulus)
else:
    print("Certificate does not have an RSA public key")