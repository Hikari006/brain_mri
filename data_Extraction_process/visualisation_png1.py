import os
import gzip
import shutil
import nibabel as nib
import matplotlib.pyplot as plt

def decompress_nii_gz(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.nii.gz'):
                gz_path = os.path.join(dirpath, filename)
                nii_path = os.path.join(dirpath, filename[:-3])  # Remove .gz
                # Only decompress if the .nii doesn't already exist
                if not os.path.exists(nii_path):
                    with gzip.open(gz_path, 'rb') as f_in:
                        with open(nii_path, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    print(f"Decompressed: {gz_path} -> {nii_path}")

# Example usage:
root_directory = '/path/to/local/download/dir/Outputs/cpac/nofilt_noglobal/reho'  # Change this to your base directory
decompress_nii_gz(root_directory)

# Path to your NIfTI file
datasets_dir = './datasets'  # Directory containing .nii files
nii_files = [f for f in os.listdir(datasets_dir) if f.endswith('.nii')]
if not nii_files:
    raise FileNotFoundError('No .nii files found in the datasets directory.')
nii_path = os.path.join(datasets_dir, nii_files[0])

# Load the NIfTI file
img = nib.load(nii_path)
data = img.get_fdata()

# Show the middle slice of the first axis (axial view)
slice_index = data.shape[2] // 2
plt.imshow(data[:, :, slice_index].T, cmap='gray', origin='lower')
plt.title(f'Slice {slice_index}')
plt.axis('off')
plt.show()


