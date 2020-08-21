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

###### batch_convert_nex_to_fasta.py
- 使用方法
将需要转化的nexus格式文件放到input_nexus文件夹中，然后运行脚本
```
python .\batch_convert_nex_to_fasta.py .\input_nexus\ output_fasta
```
fasta结果文件将会保存在 output_fasta文件夹中

###### ROUSFinder2.py
这个脚本来源于论文Repeats of Unusual Size in Plant Mitochondrial
Genomes: Identification, Incidence and Evolution
使用方法 python2 ROUSFinder2.py MH645952.fna
脚本是使用python2写的
使用这个脚本的前提是blastn安装到了/user/bin目录下，
如果没有可以通过-b参数指定blastn的路径
这么说的话可能只能在linux系统下使用
默认最小长度是50,可以通过-m参数来修改


