import os
contact={}

def clsr():
    os.system("pause")
    os.system("cls")

def title(args):
    print("==========================================================")
    print("             Kontak Toko Maju jaya jaya jaya            ")
    print("==========================================================")
    print(">> " + args)

def menu():
    title("Menu <<")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Lihat Kontak")
    print("0. Keluar.")
    Choose = int(input("Choose : "))
    clsr()
    return Choose

def isKey(key):
    global contact
    if key in contact.keys():
        return True
    else:
        return False 

def Add_Contact():
    global contact
    title("Tambah Kontak")
    name = input("Nama  : ")
    number = input("Nomor    : ")
    if not isKey(name):
        contact[name] = number
    else:
        print("Sorry the name already exsist !")
    
def del_contact():
    global contact
    title ("Hapus Kontak")
    key = input("Who's phone number you wanna delete?    : ")
    if isKey(key=key):
        del contact[key]
    else:
        print("Sorry "+key+" not in your contact!")

def display_contact():
    global contact
    print(contact)

def main():
    i = -1
    while i != 0:
        i = menu()
        if i == 1:
            Add_Contact()
        elif i == 2:
            del_contact()
        elif i == 3:
            display_contact()
        else:
            print("All data delete after this!")
        clsr()

if __name__ == "__main__":
    clsr()
    main()        
