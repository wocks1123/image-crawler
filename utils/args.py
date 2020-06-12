import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--driver-path', type=str, required=True)
parser.add_argument('--keyword', type=str, required=True)
parser.add_argument('--dest-path', type=str, required=True)
parser.add_argument('--count', type=int, default=10)
parser.add_argument('--site', type=str,  default="google", help="google or naver")


args = parser.parse_args()
