import os
import re
from tqdm import tqdm

def clean_scientific_text(text):
    """
    Clean scientific text for processing.
    """
    # Replace common Greek letters with their English names
    greek_letter_patterns = {
        r'\bα\b': ' alpha ', r'\bβ\b': ' beta ', r'\bγ\b': ' gamma ', r'\bδ\b': ' delta ', r'\bε\b': ' epsilon ',
        r'\bζ\b': ' zeta ', r'\bη\b': ' eta ', r'\bθ\b': ' theta ', r'\bι\b': ' iota ', r'\bκ\b': ' kappa ',
        r'\bλ\b': ' lambda ', r'\bμ\b': ' mu ', r'\bν\b': ' nu ', r'\bξ\b': ' xi ', r'\bο\b': ' omicron ',
        r'\bπ\b': ' pi ', r'\bρ\b': ' rho ', r'\bσ\b': ' sigma ', r'\bτ\b': ' tau ', r'\bυ\b': ' upsilon ',
        r'\bφ\b': ' phi ', r'\bχ\b': ' chi ', r'\bψ\b': ' psi ', r'\bω\b': ' omega ',
        # Capital Greek Letters (less likely to conflict but included for completeness)
        r'\bΑ\b': ' Alpha ', r'\bΒ\b': ' Beta ', r'\bΓ\b': ' Gamma ', r'\bΔ\b': ' Delta ', r'\bΕ\b': ' Epsilon ',
        r'\bΖ\b': ' Zeta ', r'\bΗ\b': ' Eta ', r'\bΘ\b': ' Theta ', r'\bΙ\b': ' Iota ', r'\bΚ\b': ' Kappa ',
        r'\bΛ\b': ' Lambda ', r'\bΜ\b': ' Mu ', r'\bΝ\b': ' Nu ', r'\bΞ\b': ' Xi ', r'\bΟ\b': ' Omicron ',
        r'\bΠ\b': ' Pi ', r'\bΡ\b': ' Rho ', r'\bΣ\b': ' Sigma ', r'\bΤ\b': ' Tau ', r'\bΥ\b': ' Upsilon ',
        r'\bΦ\b': ' Phi ', r'\bΧ\b': ' Chi ', r'\bΨ\b': ' Psi ', r'\bΩ\b': ' Omega '
    }

    for pattern, replacement in greek_letter_patterns.items():
        text = re.sub(pattern, replacement, text)

    # Remove common header/footer elements (e.g., page numbers, dates)
    text = re.sub(r'\bPage \d+\b', '', text)
    text = re.sub(r'\bDate: .+\b', '', text)

    # Remove lines that are too short - often headers or footers
    text = '\n'.join([line for line in text.split('\n') if len(line) > 30])

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def merge_and_clean_text_files(directory, output_base_path, files_per_merge):
    """
    Merges every 'files_per_merge' text files in the directory into separate output files.

    :param directory: The directory containing the text files to merge.
    :param output_base_path: The base path for the output files.
    :param files_per_merge: Number of files to merge into one output file.
    """
    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    file_count = 0
    merge_count = 1

    outfile = open(f'{output_base_path}_part{merge_count}.txt', 'w', encoding='utf-8')

    for filename in tqdm(text_files, desc="Processing files"):
        file_path = os.path.join(directory, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                cleaned_text = clean_scientific_text(infile.read())
                outfile.write(cleaned_text)
                outfile.write("\n")

            file_count += 1
            if file_count >= files_per_merge:
                outfile.close()
                merge_count += 1
                file_count = 0
                outfile = open(f'{output_base_path}_part{merge_count}.txt', 'w', encoding='utf-8')
        except UnicodeDecodeError:
            print(f"Warning: Could not read {file_path} due to encoding issues.")

    outfile.close()


# Example usage
directory = './mps_txt'  # Replace with your directory path
merged_file_path = './merged_files'  # Replace with your desired output file path
files_per_merge=100

merge_and_clean_text_files(directory, merged_file_path,files_per_merge)
