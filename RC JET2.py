jenis_KOMPONEN = ["MPPF FORM 5x100x900mm", "CONTROL HORN", "PUSH ROD WIRE [10 SET]", "BRUSHLESS MOTOR", "LINKAGE STOPPER", "ESC(SW50A)", "RECEIVER(IA10B)", "CARBON FIBER ROD 3mm", "SERVO 9g", "RC LIPO BATTERY", "PROPELLER", "FLYSKY-i6X REMOTE CONTROL"]
harga_KOMPONEN = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print(" ****KEDAI PERALATAN ELEKTRONIK MIDEA****")
print("\n    SENARAI HARGA :")
print("\nMPPF FORM 5x1000x900mm = RM23") 
print("CONTROL HORN = RM3")
print("PUSH ROD WIRE = RM 2")
print("BRUSHLESS MOTOR = RM 15.79")
print("LINKAGE STOPPER = RM 12")
print("ESC(SW50A) = RM67")
print("RECEIVER (IA10B RX) = RM61")
print("CARBON FIBER ROD 3mm = RM25.30")
print("SERVO 9g = RM5.20")
print("RC LIPO BATTERY = RM57.56")
print("PROPELLER = RM5.50")
print("FLYSKY-i6X REMOTE CONTROL = RM161")

a=int(input("\nMasukkan tempahan untuk MPPF FORM:"))
b=int(input("Masukkan tempahan untuk CONTROL HORN:"))
c=int(input("Masukkan tempahan untuk PUSH ROD WIRE:"))
d=int(input("Masukkan tempahan untuk BRUSHLESS MOTOR:"))
e=int(input("Masukkan tempahan untuk LINKAGE STOPPER:"))
f=int(input("Masukkan tempahan untuk ESC(SW50A):"))
g=int(input("Masukkan tempahan untuk RECEIVER(IA10B):"))
h=int(input("Masukkan tempahan untuk CARBON FIBER ROD:"))
i=int(input("Masukkan tempahan untuk SERVO 9g:"))
j=int(input("Masukkan tempahan untuk RC LIPO BATTERY:"))
k=int(input("Masukkan tempahan untuk PROPELLER:"))
l=int(input("Masukkan tempahan untuk FLYSKY-i6X REMOTE CONTROL:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga() :
    for i in range (12) :
        jumlah[i] = harga_KOMPONEN[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"komponen", jenis_KOMPONEN[0])
    print(b,"komponen", jenis_KOMPONEN[1])    
    print(c,"komponen", jenis_KOMPONEN[2])
    print(d,"komponen", jenis_KOMPONEN[3])
    print(e,"komponen", jenis_KOMPONEN[4])
    print(f,"komponen", jenis_KOMPONEN[5])
    print(g,"komponen", jenis_KOMPONEN[6])
    print(h,"komponen", jenis_KOMPONEN[7])
    print(i,"komponen", jenis_KOMPONEN[8])
    print(j,"komponen", jenis_KOMPONEN[9])
    print(k,"komponen", jenis_KOMPONEN[10])
    print(l,"komponen", jenis_KOMPONEN[11])

    print("\nJumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()