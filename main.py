from Bio import Entrez

Entrez.email = "your_email@example.com"  # replace with your actual email

def fetch_gene(gene_name):
    handle = Entrez.esearch(db="gene", term=gene_name + "[Gene]", retmode="xml")
    record = Entrez.read(handle)
    handle.close()

    if record["IdList"]:
        gene_id = record["IdList"][0]
        summary = Entrez.efetch(db="gene", id=gene_id, retmode="xml")
        result = Entrez.read(summary)
        print(result[0]["Entrezgene_gene"]["Gene-ref"]["Gene-ref_locus"])
        print(result[0]["Entrezgene_summary"])
    else:
        print("Gene not found.")

fetch_gene("BRCA1")
