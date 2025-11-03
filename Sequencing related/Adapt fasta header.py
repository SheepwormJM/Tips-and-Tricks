from Bio import SeqIO
import re

def extract_gene_name(description):
    """Extracts the gene name using a regular expression."""
    # Pattern to find the string between "GN=" and the next space or end of line
    match = re.search(r"GN=([^ ]+)", description)
    if match:
        return match.group(1)
    else:
        return "Unknown_gene"

# Open the input FASTA file and process each record
with open("input.fasta", "r") as in_handle, open("output.fasta", "w") as out_handle:
    for record in SeqIO.parse(in_handle, "fasta"):
        gene_name = extract_gene_name(record.description)
        # Construct the new header (e.g., just the gene name)
        new_header = f">{gene_name}"
        
        # Write the new header and sequence to the output file
        out_handle.write(new_header + "\n" + str(record.seq) + "\n")
