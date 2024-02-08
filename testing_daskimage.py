import dask_image.imread
import dask.array as da
import numpy as np

def import_im(path, file_type):
    img_array_dask = dask_image.imread.imread(f"{path}/*.{file_type}")
    print(img_array_dask)
    # img_array = img_array_dask[0:1, :, :].compute() # working with extra dimension
    img_array = img_array_dask[0:2, :, :].compute()
    print(img_array.shape)
    return img_array

def test_func():
    dask_array = da.random.random((3770, 1898, 1898), chunks=(1, 1898, 1898))
    print(dask_array)
    img_array = dask_array[100:102, :, :].compute()
    print(img_array.shape)

if __name__ == "__main__":
    path = "data"
    file_type = "jp2"
    img_array = import_im(path, file_type)
    print(img_array.shape)

    #test_func()

