#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Thu Mar 9, 2017

# Imports
import os
import subprocess
import glob
import re
import natsort
from astropy.io.fits import getval


def open_in_ds9(gout_de, gout_e, gout_d, n, gtype='f814w'):
    """Open fitsfiles in ds9 with some flgs.

    Arguments:     n: galaxy number

    ds9 flgs:
        ds9 -scale log -cmap a -tile grid layout 10 4
            -match colorbar -match scale -match scalelimits
            FITSFILES_NAMES

    Reference:
        http://ds9.si.edu/doc/ref/command.html#scale

    """
    # path of four fitsfiles to open
    simgal = '/Users/poudel/jedisim/simdatabase/'
    flgs = '-scale log -cmap a ' + '-tile grid layout 5 3 ' +\
        '-match colorbar -match scale -match scalelimits' + ' '

    # main galaxy name is in the end, it is because while matching colorbar
    # and scale limits, ds9 used last opened galxy to match all the galaxies.
    # expdisk_devauc/galfit_outputs_f8/expdisk/f814w_expdisk0.fits
    # expdisk_devauc/galfit_outputs_f8/devauc_res/f814w_devauc_res0.fits
    f0 = gout_de + 'expdisk/' + gtype + '_expdisk' + str(n) + '.fits'
    f1 = gout_de + 'expdisk_res/' + gtype + '_expdisk_res' + str(n) + '.fits'
    f2 = gout_de + 'devauc/' + gtype + '_devauc' + str(n) + '.fits'
    f3 = gout_de + 'devauc_res/' + gtype + '_devauc_res' + str(n) + '.fits'
    f4 = gout_de + 'residual/' + gtype + '_res' + str(n) + '.fits'
    f5 = gout_e + 'expdisk/' + gtype + '_expdisk' + str(n) + '.fits'
    f6 = gout_e + 'expdisk_res/' + gtype + '_expdisk_res' + str(n) + '.fits'
    f7 = gout_e + 'residual/' + gtype + '_res' + str(n) + '.fits'
    f8 = simgal + 'galaxies/' + gtype + '_gal' + str(n) + '.fits'
    f9 = simgal + 'galaxies/' + gtype + '_gal' + str(n) + '.fits'
    f10 = gout_d + 'devauc/' + gtype + '_devauc' + str(n) + '.fits'
    f11 = gout_d + 'devauc_res/' + gtype + '_devauc_res' + str(n) + '.fits'
    f12 = gout_d + 'residual/' + gtype + '_res' + str(n) + '.fits'
    f13 = simgal + 'galaxies/' + gtype + '_gal' + str(n) + '.fits'
    f14 = simgal + 'galaxies/' + gtype + '_gal' + str(n) + '.fits'

    lfiles = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]
    lfiles = [f if os.path.isfile(f) else 'null.fits' for f in lfiles]
    files = ' '.join(lfiles)
    files_print = '\n'.join(lfiles)
    print(files_print)

    # ds9 commands
    ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
    cmd = ds9 + ' -height 1200 ' + ' -width 2500 ' + flgs + files
    subprocess.call(cmd, shell=True)


def find_color(f606, f814):
    """Find difference in magnitudes of f606 and f814 bands."""
    mag1 = getval(f606, 'MAG')
    mag2 = getval(f814, 'MAG')
    print(f606[-20:], '==>', '%.2f' % (mag1 - mag2))


def main_ds9():
    """Run main function."""
    # galaxy numbers to open in ds9
    nums = [1, 14, 31, 33, 38, 40, 41, 44, 46, 52, 54,
            56, 59, 69, 73, 76, 79, 80, 81, 85, 90, 92, 95]

    # print magnitude difference
    # /Users/poudel/jedisim/simdatabase/galaxies/f606w_gal195.fits
    f606 = '/Users/poudel/jedisim/simdatabase/galaxies/f606w_gal'
    f814 = '/Users/poudel/jedisim/simdatabase/galaxies/f814w_gal'

    # open galaxies
    # galfit outputs with "/" in the end
    gout_de = 'expdisk_devauc/galfit_outputs_f8/'
    gout_e = 'expdisk/galfit_outputs_f8/'
    gout_d = 'devauc/galfit_outputs_f8/'
    for n in nums:
        find_color(f606 + str(n) + '.fits', f814 + str(n) + '.fits')
        open_in_ds9(gout_de, gout_e, gout_d, n, 'f814w')


if __name__ == "__main__":
    main_ds9()
