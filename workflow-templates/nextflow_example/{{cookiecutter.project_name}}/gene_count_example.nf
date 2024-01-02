/* This script reads gene names and counts from a file (called gene_counts.tsv that is on S3) and writes the output to 
a file if the count is greater than 10. */

params.outdir = './nextflow_example'
params.gene_counts = null
MINIMUM_COUNT = 10

// Check if the gene_counts parameter is provided
if (params.gene_counts == null) {
    error "Please provide the --gene_counts parameter with the S3 path."
}

Channel
    .fromPath( params.gene_counts ) 
    .splitCsv( header: true, sep: '\t' )
    .map { row -> tuple( row.gene_id, row.gene_name, row.sample_id, row.count ) }
    .set { gene_counts_run_ch }
    
process filter_low_gene_counts {

    input:
    tuple val(gene_id), val(gene_name), val(sample_id), val(count)
    
    output:
    path "out.txt"
        
    shell:
    """
    if [[ ! -f out.txt ]]; then
        echo "gene_id\tgene_name\tsample_id\tcount" > out.txt
    fi
    
    echo "$gene_id\t$gene_name\t$sample_id\t$count" | awk -F '\\t' '\$4 >= $MINIMUM_COUNT {print \$0}' >> out.txt
    """
}


workflow {
    filter_low_gene_counts(gene_counts_run_ch)
    .collectFile(
        name: 'output.tsv',
        storeDir:params.outdir,
        keepHeader: true,
        )
}

