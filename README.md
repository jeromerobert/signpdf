# Install dependencies

On Debian and derivatives:

    apt-get install python-pypdf2

Or with pip:

    pip install pypdf2


# Usage

    usage: signpdf.py [-h] (-o OUTPUT | -i) [-s SCALE] [-p PAGE] input x y

    Insert a signature in an existing PDF file.The signature file must be
    ~/.signature.pdf.

    positional arguments:
      input                 input PDF file
      x                     Position of signature on the page in mm
      y                     Position of signature on the page in mm

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
      -i, --overwrite
      -s SCALE, --scale SCALE
                Scaling of the signature.
      -p PAGE, --page PAGE  The page where to add the signature
