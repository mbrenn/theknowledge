
import os
import subprocess

root_dir = '../docs'
base_output_dir = '../output'

# Walk through all subdirectories of the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Filter .adoc files in the current directory
    adoc_files = [os.path.join(dirpath, f) for f in filenames if f.endswith('.adoc')]

    print(dirpath)
    
    # If there are any .adoc files, run the asciidoctor command
    if adoc_files:

        # Compute relative path from root_dir
        rel_path = os.path.relpath(dirpath, root_dir)
        output_dir = os.path.join(base_output_dir, rel_path)

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Run asciidoctor with the specific output directory
        command = ['asciidoctor', '-a', 'docinfo=shared', '-D', output_dir] + adoc_files
        subprocess.run(command)


print("Asciidoctor processing completed for all subdirectories.")
