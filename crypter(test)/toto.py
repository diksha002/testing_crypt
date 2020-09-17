from Crypto.PublicKey import RSA
	
	
#creation d´un couple de clés
key = RSA.generate(1024)

#afficher ses clés:
k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')
	
#sauvegarder ses clés dans des fichiers:
with open('private.pem','w') as kf:
	kf.write(k.decode())
	kf.close()
	
with open('public.pem','w') as pf:
	pf.write(p.decode())
	pf.close()


#importer des clés à partir d'un fichier
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

#dechiffrage
#data/file to decrypt
with open('crypted.txt','rb') as f:
	x = privat.decrypt(enc_data)
	x = x.decode('utf-8')

#saves the decrypted msg in decrypted.txt
f = open("decrypted.txt","w")
f.write(str(x))
f.close

