nama=input("Nama :")
ttl=input("Tempat tanggal lahir :")

x=nama.split()
y=ttl.split()

if len(x)>2:
    print("Haloo!",x[2],",",x[0],x[1])
else:
    print("Haloo",x[1],",",x[0])
print("Anda lahir di",y[0],"pada tanggal",y[1],y[2],y[3])
