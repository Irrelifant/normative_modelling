Paper: https://www.nature.com/articles/s41598-023-41443-4?fromPaywallRec=false 

The o-connell count matrices were produces by us
for that we donloaded the provided accession numbers with the sra-toolkit (3.1.1) like this
We referred to the Run Selector files uploaded by the Author of the paper. 

        $output_dir/../fasterq-dump --split-files --threads $threads -O $output_dir $acc & 
    

Then we produced count matrices like this:
         STAR --runThreadN $threads \
         --genomeDir $REF_GENOME_DIR \
         --readFilesIn $FASTQ1 $FASTQ2 \
         --outFileNamePrefix $OUTPUT_DIR/${BASENAME}_ \
         --outSAMtype BAM SortedByCoordinate \
         --quantMode GeneCounts \
         >> $LOG_FILE 2>&1


Also it is to mention that i tried to first perform a Quality control and trimming of the received fastq reads, but it resulted in many missing subjects as an output, (added the mechanism to the folder)

