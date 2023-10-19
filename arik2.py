import hashlib
import os

def aurkitu(fitxategi):
	with open(fitxategi, "rb") as f: 
		info = f.read();
		kode = hashlib.new("md5")
		kode.update(info)
		return kode.hexdigest() 

karpeta="~/Descargas/irudia"
fitx_lista=os.listdir(karpeta)
aurk=False
ind=0
while aurk==False and ind<len(fitx_lista):
	fitx=fitx_lista[ind]
	fitx=karpeta+os.sep+fitx 
	if os.path.isfile(fitx): 
		hashbalioa=aurkitu(fitx) 
		if(hashbalioa=="e5ed313192776744b9b93b1320b5e268"):
			aurk=True
			print("fitxategia honako hau da " + fitx)
	ind=ind+1
