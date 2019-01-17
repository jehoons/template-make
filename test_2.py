import os
import sys
import argparse 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='xxx') 

    parser.add_argument('-i', '--input', metavar='INPUT_FILE', type=str, 
            help='output', default='test.txt')

    args = parser.parse_args()

    args_dict = vars(args)

    # print(args)