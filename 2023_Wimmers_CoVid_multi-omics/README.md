2 datasets:

Blood transcriptomics dataset 
GSE239787_Raw.counts.txt.gz	 

RNAseq blood samples

GEO accession: GSE239787
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE239787

	Blood from COVID-19 infected infants and young children (Omciron and pre-omicron, n=37) and healthy controls (n=53) 


Preprocessing:
counts: htseq-count 
Filter: ENSEMBL IDs were filtered to remove low/ non-expressed transcripts (<5 reads in >50% of samples)
Gene-level counts: averaging counts from all ENSEMBL IDs mapping to the same gene symbol (IDs mapping to multiple symbols were discarded), using the bioMart package
- ENSEMBLE_ID != Gene level (mehrere expressions in nem gene... )
Normalized: estimateSizeFactors function of DESeq2 

(Evaluate monocyte signatures expression during infection (for paper)): 



"Alignment was performed using STAR version 2.7.3a99 and transcripts were annotated using a composite genome reference which included GRCh38 Ensembl release 100 and SARS-CoV-2 (GCF_009858895.2,ASM985889v3). Transcript abundance estimates were calculated internal to the STAR aligner using the algorithm of htseq-count.100 ENSEMBL IDs were filtered to remove low/ non-expressed transcripts (<5 reads in >50% of samples). Gene-level counts were created by averaging counts from all ENSEMBL IDs mapping to the same gene symbol (IDs mapping to multiple symbols were discarded), using the bioMart package. Gene counts were normalized using the estimateSizeFactors function of DESeq2.62 To evaluate monocyte signatures expression during infection, scores for each signature were computed as the average of all genes within the signature. For comparison with adult cohorts, gene expression data from GEO dataset GSE152641 (Inflammatix cohort) were used. BTM fold changes were computed as the average fold change of all genes within each BTM between COVID-19 subjects and healthy controls."



scMultiome dataset GEO: GSE239799 and processed data
-> Single cell will maybe added later on ... 
RNAseq single-cell trascriptomics PBMC sample



before (n=9), during (n=18), and after (n=9) COVID-19 infection (omicron and pre-omicron) as well as age- and sex-matched healthy controls (n=7) 

 Pre, acute, and convalescent samples from non-omicron infection are longitudinally collected from the same subjects.






