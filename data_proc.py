import os, shutil
import glob

root = 'Harmonizer/src/train/harmonizer/dataset/HCCOCO/train'

folder_path = os.path.join(root, 'comp')
mask_path = os.path.join(root, 'mask')
real_path = os.path.join(root, 'image')

jpg_files = glob.glob(os.path.join(folder_path, "*.jpg"))

real_image = []

# Loop 
for jpg_file in jpg_files:
    path_filename, extension = os.path.splitext(jpg_file)           # output: '/dataset/HCCOCO/c100132_689781_2', '.jpg'
    filename = os.path.split(path_filename)[1]                      # output: 'c100132_689781_2'
    
    prefix_file_mask = '_'.join(filename.split('_')[:-1])           # output: 'c100132_689781'
    prefix_file_real = '_'.join(prefix_file_mask.split('_')[:-1])   # output: 'c100132'
    # prefix_num = '_'.join(filename.split('_')[-1:])                 # output: '2'
    # print(int(prefix_num))
    
    # path_comp = os.path.join(folder_path, filename + extension)
    path_mask = os.path.join(mask_path, prefix_file_mask + '.png')    # output: '/dataset/HCCOCO/c100132_689781.png'
    path_img = os.path.join(real_path, prefix_file_real + extension)  # output: '/dataset/HCCOCO/c100132.jpg'

    # new_comp = os.path.join(folder_path, filename + extension)
    new_mask = os.path.join(mask_path, prefix_file_mask + extension)  # output: '/dataset/HCCOCO/c100132_689781.jpg'
    new_img = os.path.join(real_path, prefix_file_mask + extension)   # output: '/dataset/HCCOCO/c100132_689781.jpg'

    if os.path.exists(path_mask):
        # print(path_mask, new_mask)  # 
        os.rename(path_mask, new_mask)
        # print(path_img, new_img)  # 
        shutil.copyfile(path_img, new_img)
        if not real_image.count(path_img) > 0: 
            real_image.append(path_img)

for real in real_image:
    if os.path.exists(real):
        # print(real)  # 
        os.remove(real)

print("Complete")