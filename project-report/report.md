# Utilizing Machine Learning and Visualization Tools to Analyze Breast Tumor Measurements :hand: fa18-523-80

Evan Beall
Indiana University
Bloomington, IN 46408, USA 
ebbeall@iu.edu 

:o: format not followed

| github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-80/blob/master/project-report/report.md)



## Abstract

Cancer is a life altering disease that affects people all over the world.  In the United States alone it is estimated that throughtout a person's lifetime they have around a 39.66% chance of developing cancer and a 22.03% chance of dying from cancer at all invasive sites [@fa18-523-80-www-acs].  This disease can be classified as a human problem that no one can really escape from.  With the odds of developing this disease being over one in three, nearly every person knows someone that has been diagnosed or will no someone that is diagnosed at some point in their lives.  The public has high visibility on this disease and therefore lots of funding is placed on research to find a cure.

Oncology research is an ever expanding field.  While there have been huge advancements in how we treat cancer, a stop to the disease has yet to be found.  The funding for research into a cure has been ever expanding.  It is very hard to get an accurate estimate of how much is spent on cancer research each year due to the amount of players in the industry.  This industry spands accross all nations and is being researched in all corners of the global.  Funding for cancer research comes from governments, foundations, pharmaceutical companies, private investors, and much more.  The fact that there are so many different parties involved across the world make is impossible to come up with an actual figure of the cost of this research.  In the United States, there is branch known as the Nationa Cancer Institute that helps to organize governmentally funded research into Cancer.  The current budget that has been allocated to the NCI for the 2019 fiscal year is $5.74 billion [@fa18-523-80-222-nci].  This budget represents an increase of 79 million dollars from 2018.

In the past, cancer treatment and research has been mainly focused on a casting a wide net by attempting to treat all individuals with a generalized treatment regiment. The focus of most of the large pharmaceutical companies that are involved in the creation and research of the main cancer fighting drugs has been on a one drug fits all methodology. In recent years this mindset has been beginning to change. Many of the large pharmaceutical companies are moving to a more tailored approach in combating cancer. This involves utilizing data analysis in tailoring treatments and analysis of data to predict outcomes of future trials. To further explore this idea the present study explores fine needle aspirate data from breast cancer research performed at University of Wisconsin. This study will utilize machine learning techniques to analyze and create visual representations of this data set.

## Keywords

Breast Cancer, Python, big data, random forest

## Introduction

Cancer is one of the most devestating conditions financially, emotionally, and physically to the person who is diagnosed and those around them.  In the United States alone "he Agency for Healthcare research and Quality estimates that the direct medical costs (total of all health care costs) for cancer in the US in 2015 were $80.2 billion."  This figure includes all heath care costs that are associated with cancer.  There are several aspects that go into the total cost of health care for cancer patients, but one of the main oness is the cost of cancer treatment.

Breast cancer has high visability in the public eye and has some of the highest funding of any other types of cancer out there. Several large pharmaceutical companies and researchers get large grants to research new compounds and molecules to fight of these diseases. The oncology pharmaceutical industry is over a trillion dollar industry and each year their are thousands of clinical trials that are ongoing.

Oncology clinical trials function by exposing patient populations to new types of therapies and recording the results.  Clinical trials are setup to collect data throughout the time that the patient is on trial.  Some clinical trials are set up to run for decades at a time with hundreds of visits per patient.  These trials can includes tens of thousands of patients.  All of this together means that there is an enormous amount of data collected during each of these trials.  This data is stored in electronic data capture systems or EDCs.  The amount of data that needs to be worked on an analyzed for each of these trials means that there is a need for better ways to accomplish this task.

This report will delve into the possible implementation of machine learning techniques to analyze one aspect of an Oncology clinical trial.  The goal will be to determine how accurate the algorithm can predict tumor diagnosis in breast cancer patients.  This report will also run further analysis of other tumor characteristics that are present in the dataset.  If an angorithm like this can be proven to be accurate enough, its implementation in clinical trial research and oncology treatment in general could be life saving.  It could also help to eliminate the human error that is seen when a physician alone is making a diagnosis.

## Medical Costs of Cancer

## Requirements

## Dataset

The dataset used in this analysis is the Breast Cancer Wisconsin Data set.  This dataset was created by Dr. William H. Wolberg.  Dr. Wolberg is a physician at the University of Wisconsin Hospital.  The dataset utilized for this analysis is a collection of fine needle aspirate breast cancer tumor.  Fine needle aspirate biopsies are biopsies that are taken by inserting a fine needle into the affected site.  The extracted tissue is then suspended into an aqueous solution and mounted on a slide.  Dr. Wolberg then used a graphic program called Xcyt to analyze the features of each of these biopsies.  This program  The datset was complied from the features seen on digitized images of these fine nedle aspirate biopsies.  This dataset includes 569 unique patients with 32 attributes per patient. The attributes provided by this dataset includes de-identified patient identifiers, pathological diagnosis, and tumor characteristics. The characterisitcs that are included in the data are of the cell nuclei that was present in the digitized images.  The dataset is publicly available for analysis.

## Python Architecture

To perform our analysis and visualization we will utilize a Python 3 environment. On top of this we will be utilizing numpy, pandas, and matplotlib to load our dataset, perform analysis, and create visual representations of the data. 
This dataset provides us with a large amount of data on different characteristics of each tumor. This dataset also provides us with a diagnosis of the individual with breast cancer. By using both the characteristics of the analyzed tumor along with the patients diagnosis we might be able to look for tumor characteristics that are be indicative of a cancer diagnosis. This would be able to inform future clinical trial research in how to identify patients with metastatic versus benign tumor diagnosis. This could also allow for specialized treatment of specific type of breast cancer lesions. Depending on tumor density, radius, etc. might indicate that cancer was more likely to metastisize more quickly. 

## Benchmark

## Conclusion

## Bibliography

## Work Breakdown

