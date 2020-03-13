###### get_mVISTA_annotation_file_from_genbank
> 用于修改genbank文件获得mVISTA作图的注释文件的python脚本

- 使用方法
```
python get_mVISTA_annotation_file_from_genbank_1.py -i input_genbank.gb
```
###### download_gb_or_fa_from_NCBI_cp_genome_database_1.py

> NCBI批量下载序列,需要填写自己的邮箱
- 使用方法
```
python download_gb_or_fa_from_NCBI_cp_genome_database_1 -f gb/fasta -a assession.number
```
###### select_seq_according_to_seq_length.py
>选择fasta文件中序列长度大于某一值的序列
- 使用方法
```
python select_seq_according_to_seq_length.py input.fa 200 output.fasta
```