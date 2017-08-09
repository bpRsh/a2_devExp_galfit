#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Tue Mar 21, 2017
# Last update :
# Est time    : 0 days,  0 hours,      1 minutes,  8.117644 seconds.

# Imports
from astropy.io import fits
import time


def main():
    """Run main function."""

    num_source_images = 302
    for count in range(0, num_source_images):

        galaxy = '/Users/poudel/jedisim/simdatabase/galaxies'
        ingal = galaxy + '/f814w' + '_gal' + str(count) + '.fits'

        # headers for outut files
        MAG = float(fits.getval(ingal, 'MAG'))
        RADIUS = float(fits.getval(ingal, 'RADIUS'))
        MAG0 = float(fits.getval(ingal, 'MAG0'))
        PIXSCALE = 0.03
        if count >= 101:
            PIXSCALE = 0.06

        #  Note:
        #  MAG0 = 30       for 0-100
        #  MAG0 = 26.6611  for f606w band 101-301
        #  MAG0 = 26.78212 for f814w band 101-301

        #        /Users/poudel/Research/galfit_usage/devauc/galfit_outputs_f8/devauc_res/f814w_devauc_res0.fits
        indir = '/Users/poudel/Research/galfit_usage/devauc/galfit_outputs_f8/devauc_res/'
        outdir = '/Users/poudel/Research/galfit_usage/devauc/galfit_outputs_f8/bulge/'
        devauc_res = indir + 'f814w_devauc_res' + str(count) + '.fits'
        bulge = outdir + 'f814w_bulge' + str(count) + '.fits'

        dat_dev, hdr_dev = fits.getdata(devauc_res, ext=0, header=True)
        hdr_dev['BYTEORDR'] = 'BIG_ENDIAN'
        hdr_dev['MAG'] = MAG
        hdr_dev['MAG0'] = MAG0
        hdr_dev['PIXSCALE'] = PIXSCALE
        hdr_dev['RADIUS'] = RADIUS
        fits.writeto(bulge, dat_dev, hdr_dev, clobber=True)
        print("\n\ningal:", ingal)
        print("outgal:", bulge)


if __name__ == "__main__":
    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    #  Run the main program
    main()

    # print the time taken
    program_end_time = time.time()
    end_ctime = time.ctime()
    seconds = program_end_time - program_begin_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("nBegin time: ", begin_ctime)
    print("End   time: ", end_ctime, "\n")
    print("Time taken: {0: .0f} days, {1: .0f} hours, \
    {2: .0f} minutes, {3: f} seconds.".format(d, h, m, s))
