from docs.base import Base


class OpenSSL(Base):

    _doc = {
        "cer": """
# extract cem
openssl x509 -inform der -in certificate.cer -out certificate.pem
# extract public key
openssl x509 -inform der -in certificate.cer -pubkey -noout > public.key
""",
        "rsa": """
# gen key
openssl genrsa -aes256 -out private.key 8912
openssl rsa -in private.key -pubout -out public.key

# encrypt
openssl rsautl -encrypt -pubin -inkey public.key -in plaintext.txt -out encrypted.txt
# decrypt
openssl rsautl -decrypt -inkey private.key -in encrypted.txt -out plaintext.txt
""",
        "pem": """
# encrypt file with certificate
openssl smime -encrypt -binary -aes-256-cbc -in plainfile.zip -out encrypted.zip.enc -outform DER certificate.pem
openssl smime -encrypt -aes-256-cbc -in input.txt -out output.txt -outform DER certificate.pem

openssl smime -decrypt -binary -in encrypted.zip.enc -inform DER -out decrypted.zip -inkey private.key -passin pass:your_password
openssl smime -decrypt -in encrypted_input.txt -inform DER -out decrypted_input.zip -inkey private.key -passin pass:your_password
""",
        "aes": """
openssl aes-256-cbc -salt -a -e -in plaintext.txt -out encrypted.txt
openssl aes-256-cbc -salt -a -d -in encrypted.txt -out plaintext.txt
""",
    }
