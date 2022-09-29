#taken from: https://datatofish.com/copy-file-python/
import shutil

original = './Input/0.png'
target = './Output/0_copy.png'

shutil.copyfile(original, target)