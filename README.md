# Data Science & Machine Learning Repository

A comprehensive collection of machine learning, deep learning, and data science projects, including a production-ready FastAPI application for insurance data processing.

## Repository Structure

```
codebase/
├── Extra/                          # Jupyter Notebooks & Projects
│   ├── 3.6_logreg-part3-practice.ipynb
│   ├── 4.3-mlp-pytorch-part2-xor-practice.ipynb
│   ├── 9 (mlp_mnist).ipynb
│   ├── Profiling.ipynb
│   ├── Swin Transformer-Based Pneumonia Diagnosis Using RSNA Dataset.ipynb
│   └── Titanic.ipynb
├── FastAPI/                        # FastAPI Application
│   ├── main.py
│   ├── insurance.csv
│   └── patients.json
├── datasets/                       # Data Files
│   ├── placement.csv
│   ├── Teen_Mental_Health_Dataset.csv
│   └── train.csv
├── advanced/                       # Advanced Projects (placeholder)
├── beginner/                       # Beginner Projects (placeholder)
├── intermediate/                   # Intermediate Projects (placeholder)
└── README.md
```

### Jupyter Notebooks

#### Machine Learning & Neural Networks

- **3.6_logreg-part3-practice.ipynb** - Logistic regression implementation and analysis
- **4.3-mlp-pytorch-part2-xor-practice.ipynb** - Multi-layer perceptron implementation in PyTorch
- **9 (mlp_mnist).ipynb** - Neural network trained on MNIST digit classification
- **Titanic.ipynb** - Survival prediction analysis using the Titanic dataset

#### Specialized Projects

- **Swin Transformer-Based Pneumonia Diagnosis Using RSNA Dataset.ipynb** - Medical image classification using Swin Transformer architecture
- **Profiling.ipynb** - Performance profiling and optimization analysis

### FastAPI Application

Located in the `FastAPI/` directory:

The `FastAPI/` directory contains a production-ready application:

- **main.py** - Application entry point with RESTful endpoints
- **insurance.csv** - Insurance industry

### Datasets

Located in the `datasets/` directory:

- **placement.csv** - Campus placement data
  The `datasets/` directory includes:
- **placement.csv** - Campus recruitment and placement records
- **Teen_Mental_Health_Dataset.csv** - Mental health survey data
- **train.csv** - Training dataset for model developmen
- **Deep Learning**: PyTorch
- **Web Framework**: FastAPI
- \*Technology Stack

| Component        | Technology                             |
| ---------------- | -------------------------------------- |
| Deep Learning    | PyTorch                                |
| Web Framework    | FastAPI                                |
| Data Processing  | Pandas, NumPy                          |
| Machine Learning | Scikit-learn                           |
| Medical Imaging  | Vision Transformers (Swin Transformer) |
| Notebooks        | Jupyter                                |

## Project Categories

### 1. Educational Projects

- Logistic regression implementation
- Multi-layer perceptron for XOR problem
- MNIST digit classification
- Performance profiling and optimization

### 2. Application Development

- RESTful API for insurance data management
- Production-ready FastAPI application
- Data processing endpoints

### 3. Research & Analysis

- Medical image classification with Swin Transformers
- Survival prediction analysis (Titanic dataset)
- Mental health data analysis
- Campus placement analysis

## Getting Started

### FastAPI Application

```bash
cd FastAPI
python main.py
```

The application will be available at `http://localhost:8000`.

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Then select any `.ipynb` file from the `Extra/` directory to run interactively.

## Dataset Overview

| Dataset            | Purpose              | Format   |
| ------------------ | -------------------- | -------- |
| Titanic            | Survival prediction  | CSV      |
| Teen Mental Health | Survey analysis      | CSV      |
| Placement          | Recruitment analysis | CSV      |
| Insurance          | Risk assessment      | CSV/JSON |

## Project Structure

- **Extra/** - Collection of machine learning and deep learning notebooks
- **FastAPI/** - Production API application
- **datasets/** - Curated datasets for analysis and modeling
- **advanced/**, **beginner/**, **intermediate/** - Placeholder directories for future projects by skill level

## Requirements

- Python 3.8+
- PyTorch
- FastAPI
- Pandas & NumPy
- Jupyter Notebook

## Usage Notes

- All notebooks support interactive execution with cell-by-cell evaluation
- Datasets are self-contained within the repository for full reproducibility
- The FastAPI application is designed for development and demonstration purposes
- Directory structure supports future expansion with skill-level categorization
