import argparse
from PIL import Image, ExifTags
import piexif

def main():
    parser = argparse.ArgumentParser(prog='Spider',
                    description='Scrap image from a url',
                    epilog='./spider [-rlp] URL')
    parser.add_argument('-g', type=str, help="A hexadecimal key of at least 64 characters", nargs=1)
    parser.add_argument('-k', default=False, action='store_true', help="generates a new temporary password based on the key given as argument and prints it on the standard output")
    args = parser.parse_args()

    try:
        assert len(args.g) >= 64, "The hexadecimal key is to short"
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()