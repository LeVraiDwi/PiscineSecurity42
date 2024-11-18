import argparse
from PIL import Image, ExifTags
import piexif

def main():
    parser = argparse.ArgumentParser(prog='Scorpion',
                    description='print img exif',
                    epilog='./Scorpion Paths')
    parser.add_argument('Paths', type=str, help="path to file", nargs='*')
    args = parser.parse_args()
    
    if (len(args.Paths) <= 0):
        print("you must specified a path to a img")
        return

    for path in args.Paths:
            image: Image.ImageFile
            try:
                image = Image.open(path)
            except:
                print(f"can' t open file with path: {path}")
                continue
            
            name = str.split(path, '/')
            name = name[len(name) - 1]
            print(f"file: {name}")

            exif_data = image.getexif()
            if exif_data is None:
                print('No metadata found')
            else:
                for key, val in exif_data.items():
                    if key in ExifTags.TAGS:
                        print(f' - {ExifTags.TAGS[key]}: {val}')

if __name__ == "__main__":
    main()