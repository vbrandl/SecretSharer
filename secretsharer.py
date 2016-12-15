#!/usr/bin/env python2

from secretsharing import PlaintextToHexSecretSharer
import argparse, sys

version = 0.5

def restore(args):
    shares = args.IN.read().splitlines()
    print shares
    secret = PlaintextToHexSecretSharer.recover_secret(shares)
    args.out.write(secret)

def share(args):
    plain = args.IN.read()

    if len(plain) >= 193:
        print 'The input length must be less than 193 bytes'
        sys.exit(1)

    s = PlaintextToHexSecretSharer.split_secret(plain, args.threshold, args.shares)

    for l in s:
        print>>args.out, l


parser = argparse.ArgumentParser(description='Split a secret into some shares')
subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='command to execute')
p_share = subparsers.add_parser('share', description='share a secret', help='share a secret')
p_share.add_argument('-s', '--shares', metavar='S', type=int, help='amount of shares', required=True)
p_share.add_argument('-t', '--threshold', dest='threshold', metavar='T', type=int, help='threshold to restore secret', required=True)
p_share.set_defaults(func=share)

p_restore = subparsers.add_parser('restore', description='restore a secret', help='restore a secret')
p_restore.set_defaults(func=restore)

parser.add_argument('-i', '--in', dest='IN', default=sys.stdin, help='input file (default: stdin)', nargs='?', type=argparse.FileType('r'))
parser.add_argument('-o', '--out', dest='out', default=sys.stdout, help='output file (default: stdout)', nargs='?', type=argparse.FileType('w'))
parser.add_argument('-v', '--version', action='version', version="%%(prog)s %s" % version)

args = parser.parse_args()
args.func(args)
