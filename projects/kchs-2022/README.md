# Kenya Household Welfare & Labour Intelligence

## Black Rock Data | Real-world Kenya case study

This project analyses the Kenya Continuous Household Survey Programme (KCHSP) 2022, an official survey produced by the Kenya National Bureau of Statistics (KNBS).

The objective is to demonstrate client-grade work in survey data management, statistical analysis, socioeconomic research, labour-market intelligence, household welfare analysis, county-level reporting, data quality assurance, reproducible analytics, and executive data visualization.

## Source

**Dataset:** Kenya Continuous Household Survey Programme 2022  
**Producer:** Kenya National Bureau of Statistics  
**Survey ID:** DDI-KEN-KNBS-KCHSP-2022-V001  
**Geographic coverage:** Kenya, including national, urban, rural and all 47 counties  
**Sample:** 1,500 clusters and 24,000 households  
**Collection mode:** Face-to-face CAPI

Official source: https://statistics.knbs.or.ke/nada/index.php/catalog/131

## Analytical scope

### 1. Data quality and preparation
- structural validation
- missingness assessment
- duplicate checks
- invalid-code detection
- variable-type validation
- survey-weight checks
- household/individual key integrity
- outlier and implausible-value review

### 2. Household welfare
- consumption and expenditure distributions
- food versus non-food expenditure
- household-size relationships
- urban/rural differences
- county-level welfare indicators
- poverty-related measures

### 3. Labour-market intelligence
- labour-force participation
- employment status
- occupation and economic activity
- earnings and employment characteristics
- demographic differences
- county and urban/rural patterns

### 4. Women's economic empowerment
The 2022 KCHS includes a Women Economic Empowerment module. Where the microdata support it, the project will examine participation, economic activity and relevant household/business characteristics.

### 5. Statistical modelling
Potential models will be selected only after inspecting the actual variable structure and survey design. Candidate methods include weighted descriptive estimation, logistic regression, linear/generalized linear models, inequality measures, subgroup analysis, and sensitivity analysis.

### 6. Business intelligence
The final outputs will translate statistical findings into decision-oriented visuals rather than producing charts without interpretation.

## Survey methodology matters

This is survey data, not ordinary transactional data. The analysis will therefore document the weighting, clustering and estimation structure before making population-level claims.

Results will not be presented as if the raw sample were a simple random sample.

## Data policy

The KNBS catalogue states that the microdata are public-use data but require registration and are subject to conditions including non-redistribution, research/statistical use, aggregation of reporting, non-reidentification and citation.

**Raw KCHS 2022 microdata will therefore NOT be committed to this public GitHub repository.**

Instead, this repository contains reproducible analytical code, documentation, data-access instructions, derived non-identifying outputs where permitted, visualizations, methodology, and final findings.

Users who wish to reproduce the analysis should obtain the data directly from KNBS/KeNADA and place the authorised files in the local data/raw directory.

## Planned deliverables

- data/ — access and data dictionary notes; no restricted raw microdata
- analysis/ — reproducible R/Python analysis
- outputs/figures/ — publication-quality figures
- outputs/tables/ — analytical tables
- report/ — client-facing findings
- dashboard/ — Power BI-ready outputs
- README.md — project methodology and interpretation

## Interpretation standard

Black Rock Data will distinguish descriptive findings directly supported by the survey, statistical associations, model-based estimates, and limitations/uncertainty.

No causal claim will be made unless the study design supports it.

## Attribution

Kenya National Bureau of Statistics (KNBS). *Kenya Continuous Household Survey Programme 2022*. Kenya National Data Archive (KeNADA), DDI-KEN-KNBS-KCHSP-2022-V001.

This project is an independent analytical case study by Black Rock Data and is not an official KNBS publication.
