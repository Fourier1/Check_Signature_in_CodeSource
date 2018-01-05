#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import dryscrape


def veriify_signature(url, sign):
    """
    Verification de lapresence d'une signature spécifique dans le code source de votre page
    :param url: 
    :return: 
    """

    dryscrape.start_xvfb()
    sess = dryscrape.Session()
    # Nous n'avons pas besoin des images
    sess.set_attribute('auto_load_images', False)
    # visite du site
    sess.visit(url)
    corp = sess.body()
    if sign in corp:
        print('\n[Ok] * Signature présent dans le code source de la page Web\n')
    else:
        print('\n[Warning] * Pas de signature trouver dans le code source de votre page Web')
        print

#
# if __name__ == '__main__':
#     veriify_signature(url="http://dryscrape.readthedocs.io/en/latest/installation.html", sign="utf-2138")
