# AI Coding Agent Instructions

## Project Overview
**SalesCustomersAnalysis** is a data analysis project that processes and analyzes superstore sales and customer data using Jupyter notebooks. The primary workflow involves data preprocessing, exploration, and analysis using Python data science tools.

## Architecture & Key Components

### Notebook Structure
- **`01_superstore_prep.ipynb`** – Primary entry point for data preparation and cleaning. This is where raw data is loaded, transformed, and prepared for downstream analysis.
- Notebooks follow a sequential naming convention (01_, 02_, etc.) for pipeline stages.

### Data Flow
1. Raw data → Preparation/Cleaning (01_superstore_prep.ipynb) → Further analysis notebooks
2. Focus on reproducible analysis within Jupyter environment

## Development Workflows

### Setting Up the Environment
```bash
# Install core dependencies
pip install numpy pandas matplotlib seaborn
pip install jupyter  # if not already installed
```

### Running Analysis
- Open and execute notebooks in order (01_, 02_, etc.)
- Each notebook should be self-contained with clear inputs and outputs
- Use notebook cells to structure logical analysis steps

## Project Conventions

### Notebook Patterns
- **First cell**: Import all required libraries at the top
- **Data Loading**: Clearly mark data source and loading path
- **Exploratory sections**: Use Markdown cells to describe analysis purpose
- **Output**: Save intermediate results as CSV/pickle for reproducibility

### Naming Conventions
- Notebooks: `{number:02d}_{purpose}.ipynb` (e.g., `02_customer_segmentation.ipynb`)
- Variables: Use descriptive names (`customer_data` not `cd`)
- Data files: Use lowercase with underscores (`superstore_sales.csv`)

## Integration Points & Dependencies

### External Data Sources
- Superstore dataset (CSV format expected)
- Location/path: To be documented in notebooks as it's established

### Key Libraries
- **Data manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Analysis**: scikit-learn (for modeling, if needed)

## Quick Reference

| Task | Approach |
|------|----------|
| Data cleaning | Use pandas in 01_superstore_prep.ipynb |
| Add new analysis | Create new notebook with sequential naming |
| Dependencies | Update pip install command and document in README |
| Sharing results | Export analysis notebooks as HTML or save data artifacts |

---
*Last updated: 2026-01-22*
