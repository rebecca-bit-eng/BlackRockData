# KCHS 2022 Data Access

## Obtain the data

Use the official Kenya National Data Archive:

https://statistics.knbs.or.ke/nada/index.php/catalog/131

KeNADA provides user registration and login for its microdata catalogue.

Registration:
https://statistics.knbs.or.ke/nada/index.php/auth/register

## Local structure

After obtaining authorised access, place the downloaded files under:

~~~text
data/raw/
~~~

Do **not** commit the raw KNBS microdata to this repository.

## Access conditions

The KNBS catalogue identifies KCHS 2022 as public-use microdata. The World Bank's reproducibility documentation for a project using KCHS 2022 also records that the raw data are publicly available through KeNADA, require registration, and do not permit redistribution.

The KNBS terms require users to:
- use the data for statistical/scientific research;
- report aggregated information;
- avoid re-identification;
- avoid prohibited dataset linkage;
- cite the source appropriately.

## Reproducibility

Once authorised data are available locally, the analysis scripts in this project can be run against the local files.

The repository deliberately contains the methodology and code, not the restricted microdata.
