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

#dechiffrage
#data/file to decrypt
with open('crypted.txt','rb') as f:
	x = privat.decrypt(f.read())
	x = x.decode('utf-8')

#saves the decrypted msg in decrypted.txt
f = open("decrypted.txt","w")
f.write(str(x))
f.close

