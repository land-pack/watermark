#celery worker -l info --beat

import sys
import struct
import numpy
import matplotlib.pyplot as plt
from PIL import Image
from crypy import AESCipher
from lsb import decompose, assemble, set_bit
from celery.task import task
# ORM ...
from models import ImageORM, engine
from sqlalchemy.orm import sessionmaker

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# Sand Box
def store(session, id=1, embed=1, path='abc/def/'):
    image = ImageORM(id=id, embed=embed, path=path)
    session.add(image)
    session.commit()


@task
def embed_string(image_input, id=1, image_out='steg', data='898823', password='1234'):
    # Process source image
    img = Image.open(image_input)
    (width, height) = img.size
    conv = img.convert("RGBA").getdata()
    # image size show ...
    max_size = width * height * 3.0 / 8 / 1024
    # Usable payload size:
    size_string = len(data)
    # Cncrypt
    cipher = AESCipher(password)
    data_enc = cipher.encrypt(data)
    # Process data from string
    v = decompose(data_enc)
    # Add until multiple of 3
    while (len(v) % 3):
        v.append(0)
    payload_size = len(v) / 8 / 1024.0
    # Encrypted payload size:
    if (payload_size > max_size - 4):
        print "[-] Cannot embed. File too large"
        sys.exit()
    # Create output image
    steg_img = Image.new("RGBA", (width, height))
    data_img = steg_img.getdata()
    idx = 0
    for h in range(height):
        for w in range(width):
            (r, g, b, a) = conv.getpixel((w, h))
            if idx < len(v):
                r = set_bit(r, 0, v[idx])
                g = set_bit(g, 0, v[idx + 1])
                b = set_bit(b, 0, v[idx + 2])
            data_img.putpixel((w, h), (r, g, b, a))
            idx = idx + 3
    steg_img.save(image_input + "-stego.png", "PNG")
    # embedded successfully..
    store(session, id=id)
    return "embedded successfully"


# Extract data embedded into LSB of the input file
@task
def extract(in_file, out_file='', password='1234'):
    # Process source image
    img = Image.open(in_file)
    (width, height) = img.size
    conv = img.convert("RGBA").getdata()
    # Extract LSBs
    v = []
    for h in range(height):
        for w in range(width):
            (r, g, b, a) = conv.getpixel((w, h))
            v.append(r & 1)
            v.append(g & 1)
            v.append(b & 1)
    data_out = assemble(v)
    # Decrypt
    cipher = AESCipher(password)
    data_dec = cipher.decrypt(data_out)

    # Write decrypted data
    # out_f = open(out_file,"wb")
    # out_f.write(data_dec)
    # out_f.close()
    # Return the watermark to client ..
    # out_f.close()
    # Return the watermark to client ..
    return data_dec


if __name__ == '__main__':
    # embed_string(sys.argv[1])
    print extract(sys.argv[1])