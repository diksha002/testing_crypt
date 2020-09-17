from Crypto.PublicKey import RSA

#importer des cles a partir d'un fichier
with open('private.pem','r') as fk:
	priv = fk.read()
	fk.close()

with open('public.pem','r') as fp:
	pub = fp.read()
	fp.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)

#chiffrage
#data/file to encrypt
with open('tocrypt.txt','rb') as f:
	data = f.read()
	enc_data = public.encrypt(data, 32)

#saves the encrypted msg in crypted.txt
f = open("crypted.txt","w")
f.write(str(enc_data))
f.close
