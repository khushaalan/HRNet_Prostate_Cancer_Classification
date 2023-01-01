import splitfolders
input = r"C:\Users\Khushaalan Arjunan\Desktop\ML_MODEL\prostateclass"
output = r"C:\Users\Khushaalan Arjunan\Desktop\ML_MODEL\HRNet-Image-Classification\data\imagenet"

splitfolders.ratio(input, output=output, seed=42, ratio=(.8, .1, .1))