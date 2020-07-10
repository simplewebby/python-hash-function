import hashlib,csv

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

with open(r"C:\Users\Tsagan\Desktop\Proclivity\oncology_email.csv") as inputlist:
    reader=csv.reader(inputlist,delimiter='\n')
    print("Email" + "  " + "Sha256Hash")
    for row in reader:
        row = str(row).strip().replace("[", "").replace("]", "").replace("'", "")
        hash=str(row).strip().replace("[","").replace("]","").replace("'","")
        hash = encrypt_string(hash)
        print (row + "  " + hash)
        result_file = open(r"C:\Users\Tsagan\Desktop\Proclivity\hashed_emails.txt", "a+")
        result_file.write(hash + "\n")
       