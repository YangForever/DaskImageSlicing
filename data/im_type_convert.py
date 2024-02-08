import skimage.io as skio 
import glob

def convert(in_type, out_type):
    ims = glob.glob(f"*.{in_type}")
    print(ims)
    for im in ims:
        print(im)
        img = skio.imread(im)
        skio.imsave(im.replace(in_type, out_type), img)

if __name__ == "__main__":
    in_type = 'png'
    out_type = 'jp2'
    convert(in_type, out_type)
