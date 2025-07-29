import os
import shutil
import random

src_dir = 'datasets'
output_dir = 'data_split'
train_ratio = 0.8  # 80% train, 20% test

# Create output directories
for split in ['train', 'test']:
    for cls in ['autism_yes_ext', 'autism_no_new']:
        os.makedirs(os.path.join(output_dir, split, cls), exist_ok=True)

for cls in ['autism_yes_ext', 'autism_no_new']:
    class_dir = os.path.join(src_dir, cls)
    images = [f for f in os.listdir(class_dir) if f.endswith('.png')]
    random.shuffle(images)
    split_idx = int(len(images) * train_ratio)
    train_imgs = images[:split_idx]
    test_imgs = images[split_idx:]

    # Copy files
    for img in train_imgs:
        shutil.copy(os.path.join(class_dir, img), os.path.join(output_dir, 'train', cls, img))
    for img in test_imgs:
        shutil.copy(os.path.join(class_dir, img), os.path.join(output_dir, 'test', cls, img))

print("Dataset split into training and testing sets.")