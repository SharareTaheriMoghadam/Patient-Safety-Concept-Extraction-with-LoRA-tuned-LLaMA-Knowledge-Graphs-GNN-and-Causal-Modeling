# Patient-Safety-Concept-Extraction-with-LoRA-tuned-LLaMA-Knowledge-Graphs-GNN-and-Causal-Modeling
SafeGraph-RAG-Temporal is a next-generation ontology-driven patient safety intelligence framework integrating: Instruction-tuned LLaMA with LoRA fine-tuning, ontologies,  Knowledge graph reasoning, RAG, Temporal event prediction and Multi-agent clinical reasoning.
___
Associated Research Manuscript

This project is associated with pre-published research manuscripts.

Authors

- Sharare Taheri Moghadam, PhD
- Md Shafiqur Rahman Jabin, PhD

Corresponding author:
Md Shafiqur Rahman Jabin
Department of Medicine and Optometry
Linnaeus University, Kalmar, Sweden
Email: mdshafiqur.rahmanjabin@lnu.se

The associated manuscripts are currently pre-published / under peer review.
___
# SafeGraph-RAG-Temporal

Ontology-driven, retrieval-augmented, multi-agent patient safety intelligence framework.

## Core Features

- LLaMA-3 + LoRA fine-tuning
- Weak supervision auto-annotation
- Knowledge Graph (Neo4j)
- Retrieval-Augmented Generation (FAISS)
- Temporal Transformer prediction
- Multi-agent reasoning engine

## Training LoRA

python training/lora_finetune.py

## Run Full System

python pipeline/full_pipeline.py

## Research Impact

- Zero manually labeled EHR required
- Evidence-grounded AI
- Temporal safety risk forecasting
- Publishable hybrid architecture
- ## Advanced Modules

### Evaluation Framework
- Micro/Macro F1
- AUROC, AUPRC
- Ontology-aware semantic similarity

### Causal Inference
- Propensity Score Modeling
- Inverse Probability Weighting
- ATE estimation

### Temporal Modeling
- Dynamic Graph Neural Networks
- Attention-based temporal risk forecasting

## Research Contribution

This framework integrates:

- Ontology-driven weak supervision
- Retrieval-augmented LLM reasoning
- Graph neural temporal modeling
- Causal safety effect estimation
- Multi-agent hybrid AI architecture

Designed for publication in top-tier medical AI journals.
Reviewer Revision and Reproducibility Evidence (2026)


This repository includes a reviewer-evidence notebook documenting the computational analyses currently available for inspection.


Notebook and report
*******************
*******************


medication_error_dataset_with_cells_19_to_26.ipynb — data and annotation audit, focused ontology inspection, report-text-level split preparation, validation-workbook overlap checks, and Japanese dictionary-baseline evaluation.


REVIEWER_REPRODUCIBILITY_REPORT.md — evidence inventory, reported metrics, reproduction guidance, and methodological limitations.




Evidence currently documented


The supplied evidence package records:




Dataset audit: 478,176 entity-annotation rows, 58,389 unique report IDs, and 13 entity categories from Japanese medication-incident reports.


Ontology inspection: 488 parsed triples, four seed concepts/classes, 14 selected object properties, seven hierarchy relationships, and 70 explicit domain–property–range rows. No OWL restrictions were extracted.


Split preparation: 46,705 training, 5,842 validation, and 5,842 test reports, grouped by normalized report text.


Dictionary baseline: evaluated on 5,764 reports, with precision 0.4183, recall 0.2013, and micro-F1 0.2718. The reported 95% report-bootstrap confidence interval for F1 is 0.2655–0.2777 (1,000 resamples).




Scope and limitations


These results document the analyses represented in the supplied evidence package. They must not be interpreted as results from LLaMA/LoRA, ClinicalBERT, RAG, GNN, causal-model, or ontology-ablation experiments.


The current evidence does not demonstrate completed neural-model training or comparative evaluation, inter-annotator agreement, clinical-expert validation, or independent patient-/institution-level validation. Ontology provenance and expert-approved mappings remain to be verified.


The split is report-text-level, not patient-level or institution-level. Validation workbook overlap checks do not by themselves establish independent external validation.


Reproducing the evidence




Open the notebook in Google Colab or Jupyter.


Obtain the authorized input dataset and ontology separately; restricted source data are not distributed in this public repository.


Configure the input paths as described in the notebook.


Run the notebook cells in order.


Review the generated aggregate audit tables and outputs.




A reproducible rerun requires access to the same authorized input files and compatible dependencies. Do not upload restricted or identifiable record-level data to this public repository.


For the full evidence inventory and methodological qualifications, see REVIEWER_REPRODUCIBILITY_REPORT.md.


