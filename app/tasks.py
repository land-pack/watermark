# celery worker -l info --beat

import sys

from PIL import Image
from celery.task import task
from algorithm.crypy import AESCipher
from algorithm.lsb import decompose, assemble, set_bit

# ORM ...
from models import engine, ImageModel, ExtractModel, CategoryModel
from sqlalchemy.orm import sessionmaker

# create a session
Session = sessionmaker(bind=engine)
session = Session()
# configure global
extract_path = '/tmp/watermark-site'


def update_image(session, category_id, image_id):
    image = session.query(ImageModel).filter_by(id=image_id).first()
    image.watermark = 1  # Set to `1` , mean it's embed the watermark for now!
    category = session.query(CategoryModel).filter_by(id=category_id).first()
    tmp = category.watermark_count
    tmp += 1
    category.watermark_count = tmp
    session.add(category)
    session.add(image)
    session.commit()


def store_result(session, image_id, watermark):
    image = session.query(ExtractModel).filter_by(id=image_id).first()
    image.watermark = watermark  # store the watermark context
    session.add(image)
    session.commit()


@task
def embed_string(image_path, image_id, watermark_context, watermark_password):
    # Process source image
    img = Image.open(image_path)
    (width, height) = img.size
    conv = img.convert("RGBA").getdata()
    # image size show ...
    max_size = width * height * 3.0 / 8 / 1024
    # Usable payload size:
    size_string = len(watermark_context)
    # Cncrypt
    cipher = AESCipher(watermark_password)
    data_enc = cipher.encrypt(watermark_context)
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
    steg_img.save(image_path + '-steg', "PNG")
    # embedded successfully..
    update_image(session, image_id)
    return "embedded successfully"


# Extract data embedded into LSB of the input file
@task
def extract(image_id, watermark_password):
    # Process source image
    # Set the tmp file your self!
    image_path = extract_path + '/' + image_id
    img = Image.open(image_path)
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
    cipher = AESCipher(watermark_password)
    data_dec = cipher.decrypt(data_out)
    store_result(session, image_id, watermark=data_dec)
    return data_dec


if __name__ == '__main__':
    # embed_string(sys.argv[1])
    print extract(sys.argv[1])
