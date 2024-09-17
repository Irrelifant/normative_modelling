PPMI dataset from our application in the IDA portal 

IR1?

files: 
- IR2
- IR3

IR2: (from https://ida.loni.usc.edu/download/files/genetic/1c87f76d-50b8-4d59-b3d5-62e37593cb81/ppmi/PPMI_RNAseq_IR2_Release_20210402.pdf )
- whole blood
- whole transcriptome sequencing 
- HudsonAlpha (institute for biotech)
-  Illumina NovaSeq6000.
- HudsonAlpha on ribo- and globin depleted RNA
samples originally collected from PaxGene Tubes. Analysis was conducted jointly by TGen and the
Institute of Translational Genomics at USC.

 IR2 analysis release (no raw data) provided, combines Phase1 and Phase2 count and quant
data along with additional sample QC flags.

Phase 1:  1,932 samples
Phase 2:  2,823 (total 4,755)



IR3: from https://ida.loni.usc.edu/download/files/genetic/1c87f76d-50b8-4d59-b3d5-62e37593cb81/ppmi/PPMI_RNAseq_IR3_Release_20210402.pdf

- its not written how many IR3 contributes, but as the file is huge i assume plenty... 





Full text IR2:

Summary
The goal of this study is to develop a comprehensive RNA resource from whole blood samples that can
be easily accessed and utilized by the PD research community. The resource is intended to be thorough
enough for researchers to interrogate genes, pathways, and mechanisms that play a role in disease.
Whole transcriptome sequencing was conducted by HudsonAlpha on ribo- and globin depleted RNA
samples originally collected from PaxGene Tubes. Analysis was conducted jointly by TGen and the
Institute of Translational Genomics at USC. Phase1 includes 1,932 samples, while the addition of Phase2
to the IR1 release brings the total released samples to 4,755. Lab and analysis failures (<100) are
currently being processed for re-sequencing and will be made available in subsequent releases. In
addition, the IR2 analysis release (no raw data) provided, combines Phase1 and Phase2 count and quant
data along with additional sample QC flags.

Method
Whole-transcriptome RNA-seq was 1 ug aliquots of RNA isolated from PaxGene tubes. Data was
sequenced at Hudson Alpha's Genomic Services Lab on an Illumina NovaSeq6000. All samples went
through rRNA+globin reduction, followed by directional cDNA synthesis using the NEB kit. Following
second-strand synthesis, the samples were prepped using the NEB/Kapa (NEBKAP) based library prep.
BCL’s were converted to using bcltofastq v1.8.4, and FASTQ’s were merged and aligned to
GRCh37(hs37d5) by STAR (v2.4K) on GENCODE v19.
As an interim analysis, quality control steps were conducted and two types of primary results files were
created consisting of counts via FeatureCounts and abundance estimates (Transcripts per Million, TPM)
via Salmon. Transcript count data via FeatureCounts is a generic tool for read summarization and input to
a variety of downstream analysis programs. TPMs is a normalized abundance estimate often used
querying genes or transcripts. More extensive full analysis will be available following completion of
remaining samples. These are available as a single tar/gz file. Samples flagged in this tar.gz have failed
QC. BAM files were also created aligned with STAR. BAMs and FASTQs are ~100TB and only available via
hard-drive shipment.

Aligner:STAR_2.4.0k
Options: --runMode alignReads --outSAMtype SAM --outSAMmode Full
--outSAMstrandField intronMotif --outFilterType BySJout --outSAMunmapped Within
--outSAMmapqUnique 255 --outFilterMultimapNmax 10 --outFilterMismatchNmax 10
--outFilterMismatchNoverLmax 0.1 --alignMatesGapMax 1000000
--seedSearchStartLmax 30 --alignSJoverhangMin 8 --chimJunctionOverhangMin 1
--alignSJDBOverhangMin 1 --chimSegmentMin 15 --alignIntronMin 20
--alignIntronMax 1000000
Quantification: Salmon v0.7.2
Options: quant
--libType A
--threads 16
--numBootstraps 100
--seqBias
--gcBias
--dumpEq
--geneMap
Annotation used for salmon: gencode.v19.annotation.patched_contigs.gtf
Counts: featureCounts v1.6.2
Options:
-T 2
-p
-t exon
-g gene_id
-a gencode.v19.annotation.patched_contigs.gtf


Full Text IR3:

Summary
The goal of this study is to develop a comprehensive RNA resource from whole blood samples that can
be easily accessed and utilized by the PD research community. The resource is intended to be thorough
enough for researchers to interrogate genes, pathways, and mechanisms that play a role in disease.
Whole transcriptome sequencing was conducted by HudsonAlpha on ribo- and globin depleted RNA
samples originally collected from PaxGene Tubes. Analysis was conducted jointly by TGen and the
Institute of Translational Genomics at USC. Phase1 includes 1,932 samples, while the addition of Phase2
brings the total released samples to 4,756. Lab and analysis failures (<100) are currently being
processed for re-sequencing and will be made available in subsequent releases. The IR3 (B38) analysis
release (no raw data) provided, combines Phase1 and Phase2 count and quant data along with
additional sample QC flags. A meta data table is also provided that includes basic study and
demographic data along with alignment QC statistic

Method
Whole-transcriptome RNA-seq was 1 ug aliquots of RNA isolated from PaxGene tubes. Data was
sequenced at Hudson Alpha's Genomic Services Lab on an Illumina NovaSeq6000. All samples went
through rRNA+globin reduction, followed by directional cDNA synthesis using the NEB kit. Following
second-strand synthesis, the samples were prepped using the NEB/Kapa (NEBKAP) based library prep.
BCL’s were converted to using bcltofastq v1.8.4, and FASTQ’s were merged and aligned to GRCh38p12
by STAR (v2.6.1d) on GENCODE v29.
As an interim analysis, quality control steps were conducted and two types of primary results files were
created consisting of counts via FeatureCounts and abundance estimates (Transcripts per Million, TPM)
via Salmon. Transcript count data via FeatureCounts is a generic tool for read summarization and input
to a variety of downstream analysis programs. TPMs is a normalized abundance estimate often used
querying genes or transcripts. More extensive full analysis will be available following completion of
remaining samples. These are available as a single tar/gz file. Samples flagged in this tar.gz have failed
QC. BAM files were also created aligned with STAR. BAMs and FASTQs are ~100TB and only available via
hard-drive shipment. 

Command Options
Aligner:STAR_2.6.1d
 Options: ${STAR} --runMode alignReads --twopassMode Basic --outSAMtype SAM
 --outFilterType BySJout --outFilterMultimapNmax 20 --outFilterMismatchNmax 999
 --outFilterMismatchNoverLmax 0.1 --alignIntronMax 1000000
 --alignMatesGapMax 1000000 --alignSJoverhangMin 8 --alignSJDBoverhangMin 1
 --chimSegmentMin 15 --chimJunctionOverhangMin 15 –outSAMstrandField intronMotif
 --outSAMunmapped Within --outSAMattrRGline

Quantification: Salmon v0.11.3
 Options: quant
--libType A
--threads 16
--numBootstraps 100
--seqBias
--gcBias
--dumpEq
--geneMap
Annotation used for salmon: gencode.v29.primary_assembly.annotation.gtf
Counts: featureCounts v1.6.3
 Options:
-T 2
-p
-t exon
-g gene_id
-a gencode.v29.primary_assembly.annotation.gtf