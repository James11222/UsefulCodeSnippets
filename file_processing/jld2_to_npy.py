import h5py
import numpy as np
import os

def jld2_to_npy(jld2_filename, npy_filename_prefix="output_data"):
    # Open the JLD2 file in read mode
    with h5py.File(jld2_filename, 'r') as f:
        print(f"Keys available in the JLD2 file: {list(f.keys())}")

        # Iterate through all keys (variables) in the file
        for key in f.keys():
            data = f[key][()] # Load the data for the key

            # Note: Julia uses column-major order, NumPy uses row-major.
            # Transpose the data if it's a matrix to match NumPy's expected layout.
            if data.ndim >= 2:
                data = data.T

            # Create a specific NPY filename for each variable
            current_npy_filename = f"{npy_filename_prefix}_{key}.npy"
            np.save(current_npy_filename, data)
            print(f"Saved variable '{key}' to {current_npy_filename}")
