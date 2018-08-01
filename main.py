import inqcipher
import sys
import os
import json
from argparse import ArgumentParser


if __name__ == '__main__':
    if not os.path.isfile('config.json'):
        print('Missing config file!')
        raise SystemExit

    with open('config.json', 'r') as raw:
        config = json.loads(raw.read())
        chars = config['chars']
        levels = config['levels']

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(title='Available commands.')

    # Encrypt options
    encrypt = subparsers.add_parser('encrypt', description='Encrypt a plain text.')
    encrypt.add_argument('plain', help='Plain text to encrypt.')
    encrypt.add_argument('key', help='Key to encrypt.')

    # Decrypt options
    decrypt = subparsers.add_parser('decrypt', description='Decrypt a ciphered message.')
    decrypt.add_argument('plain', help='Ciphered message to decrypt.')
    decrypt.add_argument('key', help='Key to decrypt.')

    # Generate options
    generate = subparsers.add_parser('generate', description='Generate a random key.')

    args = parser.parse_args()

    if args.encrypt:
        wheel = inqcipher.decrypt_key(chars, args.encrypt.key, levels)
        print(inqcipher.encrypt(args.encrypt.plain, wheel, chars))
    if args.decrypt:
        wheel = inqcipher.decrypt_key(chars, args.key, levels)
        print(inqcipher.decrypt(args.decrypt, wheel, chars))
    if args.generate:
        print(inqcipher.generate_key(chars, inqcipher.generate_wheel(chars, levels)))
