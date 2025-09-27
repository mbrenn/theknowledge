
import os
import subprocess
import shutil

root_dir = '../docs'
base_output_dir = '../output'

# Walk through all subdirectories of the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Filter .adoc files in the current directory
    adoc_files = [os.path.join(dirpath, f) for f in filenames if f.endswith('.adoc')]
    png_files = [os.path.join(dirpath, f) for f in filenames if f.endswith('.png')]

    print(dirpath)

    # Compute relative path from root_dir
    rel_path = os.path.relpath(dirpath, root_dir)
    output_dir = os.path.join(base_output_dir, rel_path)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # If there are any .adoc files, run the asciidoctor command
    if adoc_files:

        # Run asciidoctor with the specific output directory
        command = ['asciidoctor', '-a', 'docinfo=shared', '-D', output_dir] + adoc_files
        subprocess.run(command)

    if png_files:
        # Copy all found png files to target directry
        
        for png_file in png_files:
            filename = os.path.join(output_dir, os.path.basename(png_file))
            if os.path.exists(filename):
                os.remove(filename)
            shutil.copyfile(png_file, filename)

        


print("Asciidoctor processing completed for all subdirectories.")
