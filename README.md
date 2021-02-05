# Glaucoma-Phenotype-ML-estimation

This code is used in to generate the results presented in [Automated AI labelling of optic nerve head enables new insights into cross-ancestry glaucoma risk and genetic discovery in over 280,000 images from the UK Biobank and Canadian Longitudinal Study on Aging](https://www.biorxiv.org/content/10.1101/2020.11.03.367623v1) paper.


## Abstract:

Cupping of the optic nerve head, a highly heritable trait, is a hallmark of glaucomatous optic neuropathy. 

Two key parameters are vertical cup-to-disc ratio (VCDR) and vertical disc diameter (VDD). However, manual assessment often suffers from poor accuracy and is time-intensive. Here, we show convolutional neural network models can accurately estimate VCDR and VDD for 282,100 images from both UK Biobank and an independent study (Canadian Longitudinal Study on Aging), enabling cross-ancestry epidemiological studies and new genetic discovery for these optic nerve head parameters. 

Using the AI approach we perform a systematic comparison of the distribution of VCDR and VDD, and compare these with intraocular pressure and glaucoma diagnoses across various genetically determined ancestries, which provides an explanation for the high rates of normal tension glaucoma in East Asia. We then used the large number of AI gradings to conduct a more powerful genome-wide association study (GWAS) of optic nerve head parameters. 

Using the AI based gradings increased estimates of heritability by ~50% for VCDR and VDD. Our GWAS identified more than 200 loci for both VCDR and VDD (double the number of loci from previous studies), uncovers dozens of novel biological pathways, with many of the novel loci also conferring risk for glaucoma.


Installation
------------
With pip:
```
$ pip install -e .
```

Or with conda:
```
$ conda install conda-build
$ conda build . -c conda-forge
$ conda install --use-local {package_name}
```

## Notebook Pipeline

Follow the notebook pipeline to run train models and preprocess. 

## Contact
For contact of follow up please enquire at
hello@maxkelsen.com 

## Max Kelsen Research Lab
Max Kelsen is an Australian artificial intelligence and software engineering agency, delivering solutions across a wide range of industries, including medical, government, retail, financial services and insurance.

However, our research laboratory focuses on three areas critical to the advancement of human health, technology and Artificial Intelligence (AI) itself: 
+ algorithmic safety, 
+ genomics, 
+ and quantum computing. 

With long academic traditions, we carry a rigour and a deep understanding of hypothesis testing to deliver research projects with the highest scientific integrity, evident by the growing number of peer-reviewed scientific publications.  

We see scientific rigour and algorithmic safety of paramount importance, because careless deployment of AI in critical sectors, such as healthcare can negatively affect lives.

[Max Kelsen](https://maxkelsen.com)