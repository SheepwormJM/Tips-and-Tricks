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


# Another way, if the header is different is the following.
# These headers were ">genename0001-RA" and I wanted them to be ">genename0001-RA    gene=genename0001"

from Bio import SeqIO
import re

def extract_gene_name(description):
    """Extracts the gene name using a regular expression."""
    # Pattern to find the string between ">" and the next space or end of line
    # Note that ">" is not included in the code as it will fail, producing 'unknown_gene' each time, yet it will not be included in the output for the gene_name.
    match = re.search(r"([^ -]+)", description)
    if match:
        return match.group(1)
    else:
        return "Unknown_gene"

def extract_transcript_name(description):
    """Extracts the transcript name using a regular expression."""
    # Pattern to find the string between "-" and the next space or end of line
    match = re.search(r"-([^ ]+)", description)
    if match:
        return match.group(1)
    else:
        return "Unknown_transcript"

# Open the input FASTA file and process each record
with open("TtTr.fasta", "r") as in_handle, open("TeTr.fasta", "w") as out_handle:
    for record in SeqIO.parse(in_handle, "fasta"):
        gene_name = extract_gene_name(record.description)
        transcript_name = extract_transcript_name(record.description)
        # Construct the new header (e.g., just the gene name)
        new_header = f">{gene_name}-{transcript_name} gene={gene_name}"
        
        # Write the new header and sequence to the output file
        out_handle.write(new_header + "\n" + str(record.seq) + "\n")
