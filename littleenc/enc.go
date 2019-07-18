package main

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha512"
	"crypto/x509"
	"encoding/gob"
	"encoding/pem"
	"flag"
	"fmt"
	"io/ioutil"
)

// GenerateKeyPair generates a new key pair
func GenerateKeyPair(bits int) (*rsa.PrivateKey, *rsa.PublicKey) {
	privkey, err := rsa.GenerateKey(rand.Reader, bits)
	if err != nil {
		panic(err)
	}
	return privkey, &privkey.PublicKey
}

// PrivateKeyToBytes private key to bytes
func PrivateKeyToBytes(priv *rsa.PrivateKey) []byte {
	privBytes := pem.EncodeToMemory(
		&pem.Block{
			Type:  "RSA PRIVATE KEY",
			Bytes: x509.MarshalPKCS1PrivateKey(priv),
		},
	)
	return privBytes
}

// PublicKeyToBytes public key to bytes
func PublicKeyToBytes(pub *rsa.PublicKey) []byte {
	pubASN1, err := x509.MarshalPKIXPublicKey(pub)
	if err != nil {
		panic(err)
	}

	pubBytes := pem.EncodeToMemory(&pem.Block{
		Type:  "RSA PUBLIC KEY",
		Bytes: pubASN1,
	})

	return pubBytes
}

// BytesToPrivateKey bytes to private key
func BytesToPrivateKey(priv []byte) *rsa.PrivateKey {
	block, _ := pem.Decode(priv)
	enc := x509.IsEncryptedPEMBlock(block)
	b := block.Bytes
	var err error
	if enc {
		b, err = x509.DecryptPEMBlock(block, nil)
		if err != nil {
			panic(err)
		}
	}
	key, err := x509.ParsePKCS1PrivateKey(b)
	if err != nil {
		panic(err)
	}
	return key
}

// BytesToPublicKey bytes to public key
func BytesToPublicKey(pub []byte) *rsa.PublicKey {
	block, _ := pem.Decode(pub)
	enc := x509.IsEncryptedPEMBlock(block)
	b := block.Bytes
	var err error
	if enc {
		b, err = x509.DecryptPEMBlock(block, nil)
		if err != nil {
			panic(err)
		}
	}
	ifc, err := x509.ParsePKIXPublicKey(b)
	if err != nil {
		panic(err)
	}
	key, ok := ifc.(*rsa.PublicKey)
	if !ok {
		fmt.Println("not ok")
	}
	return key
}

func PrivateKeyToFile(filename string, priv *rsa.PrivateKey) {
	err := ioutil.WriteFile(filename, PrivateKeyToBytes(priv), 0644)
	if err != nil {
		panic(err)
	}
}

func PublicKeyToFile(filename string, pub *rsa.PublicKey) {
	err := ioutil.WriteFile(filename, PublicKeyToBytes(pub), 0644)
	if err != nil {
		panic(err)
	}
}

func FileToPrivateKey(filename string) *rsa.PrivateKey {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return BytesToPrivateKey(data)
}

func FileToPublicKey(filename string) *rsa.PublicKey {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return BytesToPublicKey(data)
}

func EncryptWithPublicKey(msg []byte, pub *rsa.PublicKey) []byte {
	hash := sha512.New()
	ciphertext, err := rsa.EncryptOAEP(hash, rand.Reader, pub, msg, nil)
	if err != nil {
		panic(err)
	}
	return ciphertext
}

// DecryptWithPrivateKey decrypts data with private key
func DecryptWithPrivateKey(ciphertext []byte, priv *rsa.PrivateKey) []byte {
	hash := sha512.New()
	plaintext, err := rsa.DecryptOAEP(hash, rand.Reader, priv, ciphertext, nil)
	if err != nil {
		panic(err)
	}
	return plaintext
}

func PKCS5Padding(ciphertext []byte, blockSize int) []byte {
	padding := blockSize - len(ciphertext)%blockSize
	padtext := bytes.Repeat([]byte{byte(padding)}, padding)
	return append(ciphertext, padtext...)
}

func PKCS5UnPadding(plaintext []byte) []byte {
	length := len(plaintext)
	unpadding := int(plaintext[length-1])
	return plaintext[:(length - unpadding)]
}

func AESEncrypt(plaintext []byte, key []byte) []byte {
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	blockSize := block.BlockSize()
	plaintext = PKCS5Padding(plaintext, blockSize)
	blockMode := cipher.NewCBCEncrypter(block, key[:blockSize])
	ciphertext := make([]byte, len(plaintext))
	blockMode.CryptBlocks(ciphertext, plaintext)
	return ciphertext
}

func AESDecrypt(ciphertext []byte, key []byte) []byte {
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}
	blockSize := block.BlockSize()
	blockMode := cipher.NewCBCDecrypter(block, key[:blockSize])
	plaintext := make([]byte, len(ciphertext))
	blockMode.CryptBlocks(plaintext, ciphertext)
	plaintext = PKCS5UnPadding(plaintext)
	return plaintext
}

type CipherFile struct {
	Key  []byte
	Data []byte
}

func main() {

	var (
		showHelp    bool
		enc         bool
		dec         bool
		gen         bool
		prefix      string
		filename    string
		outfilename string
	)
	flag.BoolVar(&showHelp, "h", false, "show this help")
	flag.BoolVar(&enc, "e", false, "encrypt file")
	flag.BoolVar(&dec, "d", false, "decrypt file")
	flag.BoolVar(&gen, "g", false, "generate key pair")
	flag.StringVar(&prefix, "p", "prefix", "key pair prefix")
	flag.StringVar(&filename, "f", "", "filename to encrypt or decrypt")
	flag.StringVar(&outfilename, "o", "", "output filename to encrypt or decrypt")

	flag.Parse()
	if showHelp {
		flag.Usage()
		return
	}

	priname := prefix + "-private.key"
	pubname := prefix + "-public.key"

	if enc {
		aeskey := make([]byte, 16)

		_, err := rand.Read(aeskey)
		if err != nil {
			panic(err)
		}
		if err != nil {
			panic(err)
		}
		pub := FileToPublicKey(pubname)
		encKey := EncryptWithPublicKey(aeskey, pub)
		data, err := ioutil.ReadFile(filename)
		if err != nil {
			panic(err)
			return
		}
		encData := AESEncrypt(data, aeskey)
		buf := bytes.NewBuffer(nil)
		cipherfile := &CipherFile{
			Key:  encKey,
			Data: encData,
		}
		err = gob.NewEncoder(buf).Encode(cipherfile)
		if err != nil {
			panic(err)
		}
		if len(outfilename) == 0 {
			outfilename = filename + ".enc"
		}
		err = ioutil.WriteFile(outfilename, buf.Bytes(), 0644)
		if err != nil {
			panic(err)
		}
		return
	}

	if dec {
		pri := FileToPrivateKey(priname)
		data, err := ioutil.ReadFile(filename)
		if err != nil {
			panic(err)
		}
		var cipherfile CipherFile
		buf := bytes.NewBuffer(data)
		err = gob.NewDecoder(buf).Decode(&cipherfile)
		if err != nil {
			panic(err)
		}
		aeskey := DecryptWithPrivateKey(cipherfile.Key, pri)
		decData := AESDecrypt(cipherfile.Data, aeskey)

		if len(outfilename) == 0 {
			outfilename = filename + ".dec"
		}
		err = ioutil.WriteFile(outfilename, decData, 0644)
		if err != nil {
			panic(err)
		}
		return
	}

	if gen {
		pri, pub := GenerateKeyPair(4096)
		PrivateKeyToFile(priname, pri)
		PublicKeyToFile(pubname, pub)
		return
	}
}
