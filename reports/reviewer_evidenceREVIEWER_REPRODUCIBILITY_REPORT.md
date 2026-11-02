Reviewer Reproducibility Report


Project: Patient-Safety Concept Extraction with LoRA-tuned LLaMA, Knowledge Graphs, GNN and Causal Modeling

Evidence snapshot: November 2, 2026

Document purpose: Computational evidence inventory, reproducibility documentation, and methodological transparency for manuscript revision.



1. Overview and Scope


This report documents the computational evidence currently available for the patient-safety concept extraction project. It summarizes the dataset audit, annotation statistics, focused ontology inspection, report-level data split preparation, validation workbook overlap analysis, and dictionary-based baseline evaluation.


The associated notebook is intended to provide an organized entry point for inspecting and reproducing these analyses.


Important scope clarification: The evidence summarized in this report concerns a Japanese medication-incident report dataset. It does not, by itself, demonstrate completion of the MIMIC-III/MIMIC-IV experiments, LLaMA 3 8B Instruct fine-tuning using LoRA, ClinicalBERT comparisons, or the RAG, GNN, and causal-model experiments described in the broader project and manuscript.


Only experiments supported by executed code, available inputs, predictions, evaluation procedures, and inspectable outputs should be reported as completed.


2. Dataset and Annotation Audit


The supplied computational evidence records the following dataset characteristics:




Dataset characteristic
Reported value




Total entity-annotation rows
478,176


Unique report IDs
58,389


Number of entity categories
13


Dataset domain
Japanese medication-incident reports




2.1 Entity category distribution


The annotation report contains the following category counts:




Entity category
Annotation rows
Unique reports




Drug
168,633
53,703


Timing
90,986
35,374


Strength_amount
59,493
23,537


Date
40,617
20,907


Route
36,496
17,551


Form_form
22,859
12,252


Dosage
22,731
11,804


Duration
15,127
10,316


Strength_rate
8,084
3,988


Frequency
7,289
4,889


Strength_concentration
4,041
2,494


Form_mode
1,806
1,257


Wrong_patient
14
12




These statistics describe the annotation records and report IDs in the supplied dataset. They should not be interpreted as patient counts or as statistics from MIMIC-III or MIMIC-IV.


3. Ontology Inspection and Structural Extraction


A focused computational inspection was performed on the ontology file MSCDO.owl.


The supplied report records the following extraction results:




Ontology component
Extracted value




Parsed triples
488


Seed concepts/classes
4


Selected object properties
14


Hierarchy relationships
7


Explicit domain–property–range relationship rows
70


OWL restrictions extracted
0




3.1 Seed concepts/classes


The four seed concepts/classes identified in the extraction report are:




Patient Context


Patient Safety and Prevention


Medication-Related Risk


Medication Entity




3.2 Interpretation and limitations


The extraction represents a focused structural inspection of the supplied ontology file. It should not be interpreted as evidence of:




Successful ontology reasoning or inference.


Executed semantic rules.


Completed ontology-based prediction.


Expert-validated mappings between all dataset categories and ontology concepts.


Clinical validation of ontology relationships.




The supplied evidence also indicates that the ontology namespace and provenance require verification. Suggested mappings remain pending expert review.


Accordingly, the current ontology results should be described as computational extraction and structural inspection rather than completed semantic validation.


4. Data Split Preparation


A report-level data split was prepared using normalized report text as the grouping basis.


The reported distribution is:




Split
Number of reports




Training
46,705


Validation
5,842


Test
5,842


Total
58,389




The split was designed to keep reports with matching normalized text within the same partition.


4.1 Important qualification


The split is based on normalized report text. It does not establish patient-level or institution-level independence.


Therefore, it should be described as a report-text-level split, not as a patient-independent or institution-independent evaluation design.


Further validation would be necessary to establish generalization across independent patients, institutions, or datasets.


5. Validation Workbook Overlap Audit


The supplied validation workbook audit records the following overlap findings:




Validation workbook sheet
Unique reports
Overlap with main dataset




ExternalValid_JQ2021_20
20
0


Error_analysis_10
10
0


InternalValid_JQ2010-20_40
40
39


CrossValid_IFMIR_522
517
514




For CrossValid_IFMIR_522, the audit additionally reports 471 exact-text overlaps with the main dataset.


5.1 Interpretation


These results provide an initial record-level overlap assessment.


However, absence of exact or identified overlap does not independently establish that a validation sample is representative, clinically appropriate, or sufficiently independent for external validation.


The validation datasets and their intended roles should therefore be described carefully in any manuscript.


6. Evaluated Dictionary-Based Baseline


The supplied evidence package reports one evaluated prediction system: a training-only Japanese surface-form dictionary baseline.


The evaluation was performed on 5,764 reports.


6.1 Reported performance




Evaluation metric
Reported result




Precision
0.4183


Recall
0.2013


Micro-F1
0.2718


95% report-bootstrap confidence interval for F1
0.2655–0.2777


Number of bootstrap resamples
1,000




6.2 Interpretation


The reported results characterize the dictionary-based baseline under the evaluation procedure documented in the supplied evidence package.


They should not be attributed to:




LLaMA 3 8B Instruct.


LoRA fine-tuning.


ClinicalBERT.


Retrieval-Augmented Generation (RAG).


Graph Neural Networks (GNNs).


Causal modeling.


An ontology-guided neural model.




These approaches require their own executed experiments and evaluation outputs before comparative performance claims can be made.


7. Experiment and Evidence Status


The following table summarizes the status of the major project components based on the supplied computational evidence.




Component
Evidence status




Dataset and annotation audit
Completed computationally


Entity category distribution analysis
Completed computationally


Focused ontology parsing and extraction
Completed computationally


Ontology provenance and namespace verification
Pending


Expert-approved ontology mappings
Pending


Report-text-level split preparation
Completed computationally


Validation workbook overlap audit
Completed computationally


Japanese dictionary-based baseline evaluation
Evaluated; metrics reported in Section 6


LLaMA/LoRA model training and evaluation
Not demonstrated in the supplied evidence


ClinicalBERT or other neural baseline evaluation
Not demonstrated in the supplied evidence


RAG experiments and retrieval comparisons
Not demonstrated in the supplied evidence


GNN and causal-model experiments
Not demonstrated in the supplied evidence


Ontology/knowledge-graph ablation experiments
Not demonstrated in the supplied evidence


Statistical comparisons between multiple trained models
Not demonstrated in the supplied evidence


Inter-annotator agreement (IAA)
Not completed; a template is not an IAA result


Clinical expert evaluation
Not completed; a template is not an expert evaluation


Independent patient-level validation
Not established


Independent institution-level validation
Not established




The presence of evaluation functions, analysis templates, configuration files, or experiment launchers does not establish that the corresponding experiments were executed.


8. Reproduction Instructions


The following procedure is intended for users who have authorized access to the underlying input files.


8.1 Environment


The analysis notebook is designed to be opened in Google Colab or a compatible Jupyter environment.


Notebook:


medication_error_dataset_with_cells_19_to_26.ipynb


8.2 Input requirements


The underlying Japanese medication-incident report dataset and ontology file must be obtained separately through the appropriate authorized channels.


The original restricted or access-controlled source data are not distributed through this public repository.


The notebook input paths should be configured to point to the authorized local or mounted files.


8.3 Execution procedure




Open the notebook in Google Colab or Jupyter.


Review the initial configuration and dependency installation cells.


Configure the input paths for the authorized dataset and ontology.


Execute the notebook cells sequentially.


Inspect the dataset audit and entity distribution outputs.


Inspect the ontology extraction outputs.


Review the report-level split and validation overlap audit.


Inspect the dictionary baseline evaluation outputs.


Save the generated aggregate tables and non-sensitive outputs for documentation.




8.4 Reproducibility requirements


An independent rerun requires access to the same authorized input files and compatible software dependencies.


For stronger computational reproducibility, the following information should also be recorded and maintained:




Dataset version and source information.


Ontology version and provenance.


Python version.


Package and dependency versions.


Random seeds, where applicable.


Input file checksums, where permitted.


Notebook execution date.


Generated output files and evaluation configurations.




A fully reproducible execution should be claimed only after these details and the corresponding execution outputs have been verified.


9. Data Governance and Responsible Sharing


The project repository is intended to share code, documentation, reproducibility information, and permitted aggregate results.


Restricted, confidential, identifiable, or access-controlled patient and incident-level records must not be uploaded to the public GitHub repository.


Before publishing any derived dataset or output, verify:




Dataset licensing and redistribution restrictions.


Institutional data governance requirements.


Privacy and confidentiality obligations.


Whether the output contains record-level information.


Whether the derived information is permitted for public release.




Only appropriately authorized and non-sensitive materials should be included in the public repository.


10. Methodological Limitations and Manuscript Alignment


The current computational evidence package concerns Japanese medication-incident reports and documents a focused set of data, ontology, split, and dictionary-baseline analyses.


It does not substantiate the full experimental claims currently associated with the broader MIMIC-based LLaMA/LoRA manuscript.


In particular, the evidence summarized here does not establish:




Training and evaluation of LLaMA 3 8B Instruct using LoRA on MIMIC-III/MIMIC-IV.


Comparative evaluation against ClinicalBERT or other clinical language models.


Performance improvements attributable to ontology constraints or knowledge graphs.


RAG, GNN, or causal-model experimental results.


Ablation-based evidence for individual architectural components.


Completed inter-annotator agreement analysis.


Completed blinded clinical expert evaluation.


Independent patient-level or institution-level validation.




Consequently, the manuscript's dataset description, methodology, experimental results, tables, figures, and conclusions must be reconciled with the experiments that have actually been performed.


Any future experiments should be documented with their input datasets, model configurations, training logs, predictions, evaluation procedures, and results.


11. Conclusion


This reproducibility evidence documents the computational analyses currently available for inspection: dataset and annotation auditing, focused ontology extraction, report-text-level split preparation, validation workbook overlap assessment, and a Japanese dictionary-based baseline evaluation.


It provides a transparent record of completed work and identifies the analyses that remain pending or are not demonstrated by the supplied evidence.


The report is intended to support methodological transparency, reproducibility, and accurate alignment between the public repository and the associated scientific manuscript.


Reproducibility principle: Only executed experiments supported by inspectable inputs, procedures, predictions, and outputs should be presented as empirical findings. Planned experiments, code templates, proposed architectures, and unexecuted analysis pipelines must be clearly identified as such.



End of report


