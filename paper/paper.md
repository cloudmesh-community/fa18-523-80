# Utilizing Python Matplotlib Package for Data Visualization of In Cancer Clinical Trials :hand: fa18-523-80

* :o: format incorrect
* :o: incomplete 

| Evan Beall
| ebbeall@iu.edu
| Indiana University
| hid: fa18-523-80
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-80/edit/master/paper/paper.md)

---

Keywords: Python, Visualization, Matplotlib, Cancer, Oncology

---

## Abstract

Cancer research is an ever evolving field.  This research requires a combination of business units with backgrounds ranging from scientific, sales, operationals, etc.  In order for this research to function at the highest level, the business units involved in this pursuit will need to be able to quickly communicate.  Due to the difference in background specializations between groups this communication is best handled through visualizations.  This provides a method that allows all business units involved to understand and communicate progress effectively.  In the last several years, cancer research data has been ported into Electronic Data Capture (EDC) systems.  These systems function only as databases to hold research data and have no native way of creating visualizations.  Due to the lack of native vizualization capability, data needs to be extracted and run through software that can quickly and effectively create visualizations of large data sets.  One such tool is the Matplotlib package that is available via Python programming.  This tool is a powerful program that enables visualizations to be created for large data sets.

## Introduction

Cancer research is an ever evolving field that is beginning to utilize big data technology to help to analyze, standardize, and communicate results.  Visualization is a powerful tool for researchers, company executives, and the general public.  Matplotlib is a open source library within the Python environment.  This environment provides simple but extremely powerful 2D and 3D visualizations of large amounts of data.  The types of visualizations available within this library range from plots to scatterplots with very little code required.  This could become a very simple to teach, but powerful tool within the research community.  This would be especially helpful for scientists to be able to display their data to those that are not well versed in data.

## Architecture of Electronic Data Capture Systems

Database structure of an electronic data capture system can vary widely accross industry pharmaceutical companies.  The data present in each of these systems will vary based on several factors.  These factors include:  phase of trial, therapy being investigated, type of lesion being research, etc.  While a trial is actively accruing and treating patients, the data within the EDC system is unstructured and impossible to create comparisions between other trials.  The goal of this research is to prove that these new drugs provide benefit to the general public and allow patients to glean those benefits.  In the United States the FDA is an organization in place to guard the general public from harmful and useless new treatments.  Every new treatment resulting from a clinical trial needs to submit it data to the FDA to gain approval.  To do this, the clinical trial research community has created a structure that standardizes data once it has been extracted from these electronic data capture systems.  This standardization structure is called Study Data Tabulation Model or SDTM.  SDTM provides a standard structure for both human clinical and nonclinical studies to be submitted to the FDA for approval.  In 2004, SDTM was chosen by the FDA as the starndard that would be utilized for all submissions for drug approval.

Clinical trials can vary widely regarding what observations are collected throughout the life of the trial.  SDTM provides a set of defined variables that each of these observations will need to fit into.  Each of these observations are broken down by topic, timing, qualifiers, and identifiers depending on the type of oberservation that is being assessed.  Each observation is then sorted into a domain.  Domains are groups of variables or observations that are related by a topic-specific commonality or scientific commonality.  In general, each domain correlates to a corresponding dataset, however, some domains can be spread across multiple datasets.  Examples of datasets that are used in Oncology clinical trials are:  DM (Demographics), AE (Adverse Events), etc.  Utilizing SDTM coded databases allows for data coming out of electronic data capture systems to be compared.  In turn this allows for the FDA to compare accross clinical trials to assess the scientific background of each submission to the FDA.  The FDA is then able to better analyze the efficacy of the research and if the general public would benefit from having this product available in the American healthcare marketplace. This standardization also allows for comparisions to be drawn between research done all over the world. 

## Python Architecture

## Matplotlib Features

Matplotlib is a massive library that allows for very easy creation of basic plots, while also providing the functionality to create very intricate and powerful visualizations depending on your skill with the library.  The most utilized package within the library is pyplot.  

## Matplotlib use case for clinical trials visualizations

Oncology clinical trial research and clinical trial research in general generates an enormous amount of data.  Clinical trials can include thousands of patients with health data for multiple years at a time.  Managing this massive amount of data is not a small task.  Thousands of individuals are involved in the procurement, entry, cleaning, and manipulation of these databases before a clinical trial can be called a success or failure.  The cost to bring a drug to market is currently estimated to be about 2.6 million dollars.  Along with this, it is estimated that the cost to run one clinical trial depending on its phase could be anywhere between 10 million to 40 million dollars.   

Most of the current electronic data capture systems are built in SQL relational databases and these databases do not provide great tracking or visualization tools for people of all backgrounds to be able to understand how the progress of research is going.  Most of the people involved in clinical trials research are not well versed in data manipulation, statistical analysis, or even have scientific mindset.  Accessibility of visualization tools are extremely important within large industry pharmaceutical companies for business units to be able to communicate with each other during the clinical trial process.

## Conclusion
