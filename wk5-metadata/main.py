#EXIF EDITOR

import exif, argparse, random, string
from PIL import Image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Exif Scrambler", description="Generates random data in place of real metadata", epilog="Written by Addison Teschan")

    parser.add_argument('-f','--file',help='path to file for exif image',type=str,required=True)
    parser.add_argument('-r','--remove',help='removes all exif data',action='store_true')
    parser.add_argument('-o','--output',help='path to a new image',type=str,required=True)
    parser.add_argument('-e','--edit',help='edit each tag individually',action='store_true')
    
    args = parser.parse_args()
    
    #Removes all data given the -r flag
    if (args.remove == True):
        pillow_image = Image.open(args.file)
        exif_bulk = pillow_image.info.get('exif')
        if (exif_bulk):
            print("EXIF found! Removing...")
            pillow_image.save(args.output, exif=b'')
        else:
            print("No EXIF detected")
            pillow_image.save(args.output)

    #Edits data line by line given the -e flag
    elif(args.edit == True):
        with open(args.file, 'rb') as image:
            exif_image = exif.Image(image)
            if (exif_image.has_exif):
                try:
                    print("Exif data found!")
                    print(exif_image.list_all())
                    print(exif_image["make"])
                    data_array = dir(exif_image)
                    for i in data_array:
                        print("KEY: " , i , "VAL: ", exif_image.get(i))
                        inp = input("EDIT? Y/N\n")
                        if (inp == 'Y'):
                            val = input("ENTER NEW VALUE\n")
                            exif_image.i = val
                            print(exif_image.i)
                        else:
                            print("SKIP EDIT FOR ", i)
                    
                    with open(args.output, 'wb') as new_image_file:
                        new_image_file.write(exif_image.get_file())
                    print("Edit mode complete. Saved to", args.output)

                
                except:
                    print("Unreadable exif data") 
            else:
                print("No EXIF detected")

        
    #Reads all exif data given no other flags
    else:
        with open(args.file, 'rb') as image:
            exif_image = exif.Image(image)
            if (exif_image.has_exif):
                try:
                    print("Exif data found!")
                    print(exif_image.list_all())
                    print(exif_image["make"])
                    data_array = dir(exif_image)
                    for i in data_array:
                        print(exif_image.get(i))
                except:
                    print("Unreadable exif data") 
            else:
                print("No EXIF detected")
