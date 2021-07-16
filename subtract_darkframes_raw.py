#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Description: Creates image of raw DN - darkframes

"""
script to subtract dark frames from Specim hyperspectral data to provide a quick quality check.

Needs the arsf_tools library installed (for the ENVI reader) from: https://github.com/pmlrsg/arsf_tools/

Can install with conda using:

conda install -c https://data.neodaas.ac.uk/files/conda/arsf_tools

Usage is:

python subtract_darkframes_raw.py in_raw.raw out_dark_frame_subtracted.bil

Author: Dan Clewley, NEODAAS, PML
Creation Date: 2021-07-16

"""

from __future__ import print_function
import argparse
import numpy

from arsf_envi_reader import numpy_bin_reader
from arsf_envi_reader import envi_header

def run_subtract_darkframes(in_file, out_file):
    """
    Create BIL file with raw data - dark frames
    """

    in_header = envi_header.find_hdr_file(in_file)
    header_data = envi_header.read_hdr_file(in_header)

    darkframe_startline = int(header_data["autodarkstartline"])

    dark_frames_lines = []

    # Open input file
    in_data = numpy_bin_reader.BilReader(in_file)

    # Open file for output
    out_data = open(out_file, "wb")

    print("Getting dark frames...")
    for i, line in enumerate(in_data):
        if i >= darkframe_startline:
            dark_frames_lines.append(line)

    average_dark_frames = numpy.average(dark_frames_lines, axis=0)

    in_data.file_handler.seek(0)
    in_data.current_line = 0

    print("Applying to raw data...")
    for i, line in enumerate(in_data):
        if i <= darkframe_startline:
            print(" Line {0:05}/{1:05}".format(i, darkframe_startline), end="\r")
            line = numpy.where(line > average_dark_frames, line - average_dark_frames, 0)
            line.astype(in_data.numpy_dtype).tofile(out_data)

    print(" Line {0:05}/{0:05}".format(darkframe_startline), end="\n")

    # Write out header (will be less lines as don't include darkframes)
    output_header_data = header_data
    output_header_data["lines"] = darkframe_startline - 1

    envi_header.write_envi_header(out_file + ".hdr",
                                  output_header_data)

    in_data = None
    out_data.close()

    print("Saved to {}".format(out_file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subtract darkframes from raw pixel values.")
    parser.add_argument("infile", type=str,
                        help="Raw data file (.raw)")
    parser.add_argument("outfile", type=str,
                        help="Output file (.bil")
    args = parser.parse_args()

    run_subtract_darkframes(args.infile, args.outfile)
