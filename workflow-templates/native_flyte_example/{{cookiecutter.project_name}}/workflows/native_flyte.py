"""
This module defines a Flyte workflow for filtering genes based on a minimum count threshold (MINIMUM_COUNT).
"""
import os
from typing import NamedTuple

import flytekit
import pandas as pd
from flytekit import task, workflow
from flytekit.types.file import FlyteFile

MINIMUM_COUNT = 10


@task
def filter_low_gene_counts(gene_counts_file: FlyteFile) -> FlyteFile:
    """
    Task for filtering gene counts based on a minimum count threshold (MINIMUM_COUNT).

    Parameters:
    - gene_counts_file (FlyteFile): Input gene counts file in FlyteFile format (S3).

    Returns:
    - FlyteFile: Output gene counts file containing rows with counts greater than or equal to MINIMUM_COUNT.
    """
    working_dir = flytekit.current_context().working_directory
    output_path = os.path.join(working_dir, "output.tsv")
    gene_counts = pd.read_csv(gene_counts_file, sep="\t")
    gene_counts = gene_counts[gene_counts["count"] >= MINIMUM_COUNT]
    gene_counts.to_csv(output_path, sep="\t", index=False)

    return FlyteFile(path=output_path)


output = NamedTuple(
    "output",
    output=FlyteFile,
)


@workflow
def gene_count(gene_counts_file: FlyteFile) -> output:
    """Ingests s3 file path with gene counts (tsv) and returns a subset of a dataframe if count>=MINIMUM_COUNT

    Args:
        gene_counts_dir (FlyteFile): S3 path where gene_counts.tsv file can be found. (see s3 location in resources)

    Returns:
        output (FlyteFile): subset of original dataframe
    """
    return output(output=filter_low_gene_counts(gene_counts_file=gene_counts_file))
