import hashlib
def hashing ():
    try:
        md_5 = hashlib.md5()
        password = input('Enter the password you want to be hashed: ')
        md_5.update(password.encode())
        hashed_md5 = md_5.hexdigest()
        print(hashed_md5)

        sha_256 = hashlib.sha256()
        password = input('Enter the password you want to be hashed: ')
        sha_256.update(password.encode())
        hashed_sha256 = sha_256.hexdigest()
        print(hashed_sha256)


        sha_512 = hashlib.sha512()
        password = input('Enter the password you want to be hashed: ')
        sha_512.update(password.encode())
        hashed_sha512 = sha_512.hexdigest()
        print(hashed_sha512)
    except:
        print("Nothing is working")



hashing()