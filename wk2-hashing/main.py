#Duplicate Destroyer
#Addison Teschan
#Given a filepath, recursively sift through all files using hashing and permanently erase duplicate items


#TODO add to garbage generator to add random file amounts with random subdirectories


import argparse, hashlib, os, glob
if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Duplicate Destroyer", description="Sifts recursively through a directory to elminate duplicate files", epilog="Written by Addison Teschan")
    parser.add_argument('-y','--yes',help='Yes to delete all',action='store_true')
    parser.add_argument('-f','--filepath',help='Specify a directory to iterate through',required=True)
    parser.add_argument('-H','--hash',help='Specify hash type used, included filetypes are sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256, blake2b, and blake2s and md5 ',type=str)
    args = parser.parse_args()

    #To reduce computational overhead, it would be preferred to hash all the files and compare digests afterward
    #Dict, key=filename
    hashes = {}
    md5hash = hashlib.md5()
    files = glob.glob(args.filepath + '/**', recursive=True)

    for file in files:
        if os.path.isfile(file) == True:
            with open(file, 'rb') as f:
                match args.hash:
                    case 'md5':
                        hashes[file] = hashlib.md5(f.read()).hexdigest()
                    case 'sha1':
                        hashes[file] = hashlib.sha1(f.read()).hexdigest()
                    case 'sha224':
                        hashes[file] = hashlib.sha224(f.read()).hexdigest()
                    case 'sha256':
                        hashes[file] = hashlib.sha256(f.read()).hexdigest()
                    case 'sha384':
                        hashes[file] = hashlib.sha384(f.read()).hexdigest()
                    case 'sha512':
                        hashes[file] = hashlib.sha512(f.read()).hexdigest()
                    case 'sha3_224':
                        hashes[file] = hashlib.sha3_224(f.read()).hexdigest()
                    case 'sha3_256':
                        hashes[file] = hashlib.sha3_256(f.read()).hexdigest()
                    case 'sha3_384':
                        hashes[file] = hashlib.sha3_384(f.read()).hexdigest()
                    case 'sha3_512':
                        hashes[file] = hashlib.sha3_512(f.read()).hexdigest()
                    case 'shake_128':
                        hashes[file] = hashlib.shake_128(f.read()).hexdigest()
                    case 'shake_256':
                        hashes[file] = hashlib.shake_256(f.read()).hexdigest()
                    case 'blake2b':
                        hashes[file] = hashlib.blake2b(f.read()).hexdigest()
                    case 'blake2s':
                        hashes[file] = hashlib.blake2s(f.read()).hexdigest()
                    case _:
                        hashes[file] = hashlib.md5(f.read()).hexdigest()


    #Garbage and unreadable. I have it set to remove the longer of the filenames.
    count = 0
    forbidden = []
    for key1 in hashes:
        if key1 in forbidden:
            continue
        for key2 in hashes:
            if key2 in forbidden:
                continue
            if hashes[key1] == hashes[key2] and key1 != key2 :
                count+=1
                print("DUPLICATE DETECTED : " , key1 , "HASH: ", hashes[key1], " IS A COPY OF ", key2, "HASH: ", hashes[key2])
                if len(key1) > len(key2) :
                    os.remove(key1)
                    forbidden.append(key1)
                else:
                    os.remove(key2)
                    forbidden.append(key2)

    print(count, "files deleted")
