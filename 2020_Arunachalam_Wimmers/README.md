
2 datasets:

RNAseq PBMC
17 COVID (from paper: 17 PBMC samples (15 patients) ); 17 Healthy
RNAseq analysis of PBMCs in a group of 17 COVID-19 subjects and 17 healthy controls

 GSE152418
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152418
GSE152418_p20047_Study1_RawCounts.txt.gz	

Preprocessing (aus supply info): 
- 
ENSEMBL IDs were filtered to remove low/non-expressed transcripts (0 reads in >50% of samples). Gene-level counts were created by averaging counts from all ENSEMBL IDs mapping to the same gene symbol (IDs mapping to multiple symbols were discarded), using the bioMart package. For hierarchical clustering of ISGs, genes were z-score normalized across subjects and then both genes and subjects were grouped by hierarchical clustering via the Ward algorithm, using Euclidean distance as a distance metric. Visualization was performed using the pheatmap package in R. For variance analysis of ISGs, principal variance components analysis (PVCA) was used (42). This approach performs a principal components analysis on the gene expression and then uses mixed linear modeling to assess the relative contribution to the variance in the first 5 principal components of parameters of interest (age, gender, severity, and days post onset of symptoms in this case).




CITE-seq Single Scell of 7 patients with COVID-19 and 5 healthy controls
GSE155673

preprocessing: 
Single-cell RNA seq processing and analysis
Raw count data was filtered to remove cells with a mitochondrial RNA fraction greater than 25% of total RNA counts per cell. The resultant count matrix was used to create a Seurat (v 3.1.4) object. Filtered read counts were scaled by a factor of 10,000 and log transformed. The antibody- derived tag matrix was normalized per feature using center log normalization. The top 2000 variable RNA features were used to perform PCA on the log-transformed counts. Using a scree plot, we chose the first 25 principle components (PCs) (98.5% of variance explained) to perform
7
further downstream analyses, including clustering and UMAP projections. Clusters were identified with Seurat SNN graph construction followed by Louvain community detection on the resultant graph with a resolution of 0.4, yielding 25 clusters. We removed one cluster that was composed of a majority of dead cells, as judged by the percentage of mitochondrial RNA (>80% before filtering) and exceptionally low unique features, resulting in 24 final clusters. We further removed samples from 4 patients with influenza A and RSV infection, as well as 2 convalescent subjects from the downstream analysis. The R package uwot (v.0.1.7) was used to produce UMAP projections with the previously selected 25 PCs. All codes used for the analysis are deposited at https://github.com/scottmk777/COVID.
