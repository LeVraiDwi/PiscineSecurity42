from cryptography.fernet import Fernet


def main():
    key = Fernet.generate_key()
    print(key)

if __name__ == "__main__":
    main()