import os
import re

png_dir = "file_path"
txt_dir = "file_path"

emotions = ["AN", "CO", "DI", "FE", "HA", "SA", "SU"]
regex_filter = re.compile(r'\.(txt)')
empty_dirs = []
count = 0
for path, dir_names, file_names in os.walk(txt_dir):
    if not os.listdir(path):
        empty_dirs.append(path + "\n")
        continue
    for txt_file in file_names:
        if regex_filter.search(txt_file):
            file = os.path.join(path, txt_file)
            with open(file, 'r') as f:
                num = f.readline().strip()
                num = int(float(num)) - 1
                emotion = emotions[num]
                new_png_name = '{:03}'.format(count) + emotion + ".png"

                png_path = path.split('\\')
                png_path = "\\" + png_path[-2] + "\\" + png_path[-1]
                old_png_name = txt_file.replace("txt", "png")
                old_png_name = old_png_name.replace("_emotion", "")
                old_png = os.path.join(png_dir + png_path, old_png_name)
                new_png = os.path.join(png_dir + png_path, new_png_name)
                os.rename(old_png, new_png)
                count += 1
with open("empty_dirs.txt", 'w') as f:
    f.writelines(empty_dirs)