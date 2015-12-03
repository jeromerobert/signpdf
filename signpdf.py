#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Insert a signature in an existing PDF file.'
   'The signature file must be ~/.signature.pdf.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-o', '--output')
group.add_argument('-i', '--overwrite', action='store_true')

parser.add_argument('input', help='input PDF file')
parser.add_argument('x', type=float, help='Position of signature on the page in mm')
parser.add_argument('y', type=float, help='Position of signature on the page in mm')
parser.add_argument('-s', '--scale', default=1., type=float,
                   help='Scaling of the signature.')
parser.add_argument('-p', '--page', nargs=1, default=0, type=int,
                   help='The page where to add the signature')

args = parser.parse_args()
if args.overwrite:
    args.output = args.input

import sys
import os
try:
    import PyPDF2 as pypdf
except ImportError:
    print """
PyPDF2 cannot be found. It may be installed with:
pip install pypdf2
or
apt-get install python-pypdf2
"""
    quit()

sig_file_name = os.path.expanduser(os.path.join('~', '.signature.pdf'))
with open(args.input, "rb") as in_file, open(sig_file_name, "rb") as sig_file:
    in_pdf = pypdf.PdfFileReader(in_file)
    in_page = in_pdf.getPage(args.page)
    sign_pdf = pypdf.PdfFileReader(sig_file).getPage(0)
    in_page.mergeScaledTranslatedPage(sign_pdf, args.scale,
        args.x / 25.4 * 72, args.y / 25.4 * 72)
    writer = pypdf.PdfFileWriter()
    for i in xrange(in_pdf.getNumPages()):
        writer.addPage(in_pdf.getPage(i))
    with open(args.output, 'wb') as out_file:
        writer.write(out_file)
