# Data Science & Machine Learning Repository

This repository contains a collection of machine learning, deep learning, and data science projects, along with a FastAPI-based application for insurance data processing.

## 📁 Repository Structure

### Jupyter Notebooks

#### Machine Learning & Neural Networks
- **3.6_logreg-part3-practice.ipynb** - Logistic regression practice exercises (Part 3)
- **4.3-mlp-pytorch-part2-xor-practice.ipynb** - Multi-layer perceptron (MLP) implementation in PyTorch for XOR problem (Part 2)
- **9 (mlp_mnist).ipynb** - MLP neural network trained on MNIST dataset
- **Titanic.ipynb** - Titanic dataset analysis and survival prediction

#### Specialized Projects
- **Swin Transformer-Based Pneumonia Diagnosis Using RSNA Dataset.ipynb** - Deep learning project using Swin Transformer architecture for medical image classification
- **Profiling.ipynb** - Performance profiling and optimization notebook
- **test.ipynb** - Testing and experimentation notebook

### FastAPI Application

Located in the `FastAPI/` directory:
- **main.py** - FastAPI application entry point
- **insurance.csv** - Insurance dataset for the application
- **patients.json** - Sample patient data
- **myenv/** - Python virtual environment with dependencies installed
  - FastAPI, Pydantic, Starlette, and other required packages

### Plagiarism Detection System

Located in the `Plagiarism Detection System/` directory:
- **plagiarism_detection.ipynb** - Main plagiarism detection implementation
- **ai.ipynb** - AI-related analysis and research
- **create_presentation.py** - Script to generate presentation materials
- **plagiarism_detection_report.txt** - Detailed report on plagiarism detection
- **trending_ai_papers.csv** - Dataset of trending AI research papers

#### IEEE Report
- Located in `IEEE_Report/` subdirectory
- **main.tex** - Main LaTeX document
- **references.bib** - Bibliography file
- **sections/** - Individual LaTeX sections:
  - introduction.tex
  - problem_statement.tex
  - related_work.tex
  - proposed_methodology.tex
  - methodology.tex
  - experimental_setup.tex
  - implementation.tex
  - results.tex
  - discussion.tex
  - conclusion.tex
  - conclusion_updated.tex
  - future_work.tex
  - dataset_description.tex

### Datasets

Located in the `datasets/` directory:
- **placement.csv** - Campus placement data
- **Teen_Mental_Health_Dataset.csv** - Mental health survey data
- **train.csv** - Training dataset (format depends on specific project)

## 🔧 Technologies & Libraries

- **Deep Learning**: PyTorch
- **Web Framework**: FastAPI
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (assumed)
- **Medical Imaging**: Vision Transformers (Swin Transformer)
- **Documentation**: LaTeX, Jupyter Notebooks

## 📊 Project Categories

### 1. Educational Projects
- Logistic regression exercises
- MLP/XOR problem implementation
- MNIST digit classification

### 2. Application Development
- FastAPI insurance data API
- RESTful endpoints for patient data

### 3. Research Projects
- Pneumonia diagnosis using Swin Transformers
- Plagiarism detection system
- AI paper analysis

### 4. Documentation
- IEEE format research paper with comprehensive sections

## 🚀 Getting Started

### FastAPI Setup
```bash
cd FastAPI
source myenv/bin/activate
python main.py
```

### Jupyter Notebooks
```bash
# Ensure Jupyter is installed
jupyter notebook

# Open any .ipynb file to run
```

## 📝 Dataset Descriptions

- **Titanic Dataset**: Passenger survival prediction
- **RSNA Dataset**: Pneumonia X-ray images for medical diagnosis
- **Teen Mental Health Dataset**: Survey responses on mental health
- **Placement Dataset**: Campus recruitment and placement data
- **Insurance Dataset**: Insurance customer and claims data

## 🎯 Project Highlights

- **Advanced Deep Learning**: Swin Transformer architecture for medical imaging
- **RESTful API**: FastAPI application for data management
- **Academic Research**: Full IEEE format research paper on plagiarism detection
- **Machine Learning Fundamentals**: Core ML algorithms and neural networks
- **Data Analysis**: Multiple datasets with analysis and visualization

## 📚 Notes

- All notebooks are interactive and can be run cell-by-cell
- The FastAPI application requires the virtual environment in `FastAPI/myenv/`
- Datasets are included in the repository for reproducibility
- The plagiarism detection project includes both Jupyter notebooks and formal academic documentation

## 🤝 Contributing

This repository contains educational, research, and project materials. Feel free to extend, modify, or improve any of the projects.

---

**Last Updated**: April 2026
