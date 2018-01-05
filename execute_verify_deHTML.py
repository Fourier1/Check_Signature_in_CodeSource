#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from chek_HTML import veriify_signature


def set_options():
    """
    Entrer les options
    :return: 
    """
    parser = ArgumentParser()
    parser.add_argument('-u',
                        '--url',
                        dest='url',
                        required='True',
                        type=str,
                        help='Entrer l\'URL cible.')

    parser.add_argument('-s',
                        '--signature',
                        dest='signature',
                        required='True',
                        type=str,
                        help='Spécification de votre signature sur l\'URL cible.')
    args = parser.parse_args()
    options = args.__dict__
    return options


if __name__ == '__main__':
    options = set_options()

    h = veriify_signature(options['url'],
                          options['signature'])
