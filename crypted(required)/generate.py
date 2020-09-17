from Crypto.PublicKey import RSA

#creation d'un couple de cles
key = RSA.generate(1024)

#afficher ses cles:
k = key.exportKey('PEM')    #the private key in PEM format
p = key.publickey().exportKey('PEM')    #the public key in PEM format

#sauvegarder ses cles dans des fichiers:
with open('private.pem','w') as kf:
		kf.write(k.decode())
		kf.close()

with open('public.pem','w') as pf:
		pf.write(p.decode())
		pf.close()
