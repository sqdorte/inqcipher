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
    parser.add_argument(
        '-e', '--encrypt',
        help='Use this to encrypt a plain text.'
    )
    parser.add_argument(
        '-d', '--decrypt',
        help='Use this to decrypt a ciphered message.'
    )
    parser.add_argument(
        '-k', '--key',
        help='The key to encrypt/decrypt a message.'
    )
    parser.add_argument(
        '-g', '--generate',
        help='Use this to generate a key.',
        action='store_true'
    )

    args = parser.parse_args()

    if len(sys.argv) > 5:
        print('You shoud\'nt use the args that way!')
        raise SystemExit
    if len(sys.argv) == 5 and not args.key:
        print('You shoud\'nt use the args that way!')
        raise SystemExit
    if len(sys.argv) > 2 and args.generate:
        print('You shoud\'nt use the args that way!')
        raise SystemExit

    if args.encrypt:
        wheel = inqcipher.decrypt_key(chars, args.key, levels)
        print(inqcipher.encrypt(args.encrypt, wheel, chars))
    if args.decrypt:
        wheel = inqcipher.decrypt_key(chars, args.key, levels)
        print(inqcipher.decrypt(args.decrypt, wheel, chars))
    if args.generate:
        print(inqcipher.generate_key(chars, inqcipher.generate_wheel(chars, levels)))