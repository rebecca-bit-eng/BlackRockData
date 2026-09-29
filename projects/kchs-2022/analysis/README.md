# Analysis Workflow

## Phase 1 — Data audit

Before analysis:

1. inventory every supplied file;
2. identify household, individual and module-level files;
3. inspect dimensions and variable labels;
4. identify household/individual identifiers;
5. inspect weights, strata and cluster variables;
6. catalogue missing-value codes;
7. verify categorical codebooks;
8. assess duplicate keys;
9. document joins between modules.

## Phase 2 — Data engineering

Create a clean analytical layer without altering the source files.

Expected outputs:

- household_clean
- individual_clean
- module-specific analytical tables
- harmonised county and residence labels
- documented derived variables

Every transformation should be recorded.

## Phase 3 — Descriptive analysis

Produce weighted estimates where the survey design requires them.

Core outputs:

- household profile
- labour-force profile
- employment structure
- expenditure distribution
- food/non-food expenditure
- urban/rural comparison
- county profiles
- socioeconomic distributions
- relevant WEE indicators

## Phase 4 — Statistical analysis

The exact model specification will be determined after inspecting the 2022 data dictionary.

Potential outcomes include:

- poverty/welfare status
- labour-force participation
- employment status
- earnings
- business/self-employment characteristics

Candidate predictors include demographic, education, household, geographic and employment variables where supported.

## Phase 5 — Validation

Every major result should undergo:

- missing-data sensitivity checks
- specification checks
- subgroup consistency checks
- survey-weight sensitivity checks where appropriate
- plausibility checks against KNBS published results

## Phase 6 — Client presentation

The final presentation should answer:

- What is happening?
- Where is it happening?
- Which groups differ?
- How large is the difference?
- What uncertainty surrounds the estimate?
- What can the evidence support?
- What can it not support?

The goal is decision-support, not dashboard decoration.
