# Machine Learning & Generative AI: A Hands-On Guide to Actuarial Practice

Companion code repository for the EAA seminar held on **8–9 June 2026 in Munich, Germany**, taught by **Dr. Simon Hatzesberger**.

**Seminar page:** <https://actuarial-academy.com/en/continuing-education/upcoming-trainings/detail/machine-learning-generative-ai-a-hands-on-guide-to-actuarial-practice-e0544/>

---

## About the Seminar

This two-day seminar gives actuaries a practical, code-first introduction to modern Machine Learning (ML) and Generative AI (GenAI). It is split into two acts and seven sections:

**Act I — Machine Learning**
1. Foundations and Traditional Machine Learning
2. Modern Machine Learning Techniques
3. Interpretable Machine Learning
4. Special Topics in Machine Learning

**Act II — Generative Artificial Intelligence**

5. Working with Generative AI: Basics and Best Practices
6. Advanced Concepts in Generative AI
7. Introduction to Agentic AI: Concepts and Applications

For every section there is one self-contained Jupyter notebook. A short additional notebook (`00_jupyter_intro`) introduces Jupyter for participants who are new to it.

Every notebook can be run in **two ways**:
- **Online on Google Colab** — no installation required, just click the badge.
- **Locally** — clone the repository and install the section's dependencies.

---

## Repository Structure

```
ml-genai-actuarial-seminar/
│
├── README.md                       ← you are here
├── LICENSE
├── .gitignore
├── requirements.txt                ← aggregated dependencies for local setup
│
└── notebooks/
    ├── 00_jupyter_intro/
    │   ├── 00_jupyter_intro.ipynb
    │   └── requirements.txt
    │
    ├── 01_foundations_traditional_ml/
    │   ├── 01_foundations_traditional_ml.ipynb
    │   ├── requirements.txt
    │   └── data/                   ← input datasets (when applicable)
    │
    ├── 02_modern_ml_techniques/
    │   ├── 02_modern_ml_techniques.ipynb
    │   ├── requirements.txt
    │   └── data/
    │
    ├── 03_interpretable_ml/
    │   ├── 03_interpretable_ml.ipynb
    │   ├── requirements.txt
    │   └── data/
    │
    ├── 04_special_topics_ml/
    │   ├── 04_special_topics_ml.ipynb
    │   ├── requirements.txt
    │   └── data/
    │
    ├── 05_genai_basics_best_practices/
    │   ├── 05_genai_basics_best_practices.ipynb
    │   ├── requirements.txt
    │   └── data/
    │
    ├── 06_genai_advanced_concepts/
    │   ├── 06_genai_advanced_concepts.ipynb
    │   ├── requirements.txt
    │   └── data/
    │
    └── 07_agentic_ai/
        ├── 07_agentic_ai.ipynb
        ├── requirements.txt
        └── data/
```

**Design notes**

- **One folder per notebook.** Each section is fully self-contained, so participants can jump directly into any topic without dragging along the rest of the repo.
- **Per-section `requirements.txt`.** Some sections (e.g. deep learning, GenAI) need heavy or unusual dependencies that should not be forced on lighter sections. The root-level `requirements.txt` aggregates all of them for a one-shot local install.
- **Per-section `data/`.** Small datasets (CSVs, JSON, a few images) live in the folder of the notebook that uses them. Larger datasets are downloaded on-the-fly from inside the notebook so the repository stays lightweight.

---

## Notebooks

| #  | Section | Notebook | Open in Colab |
|----|---------|----------|---------------|
| 00 | Jupyter & Colab — a 5-minute primer | [`00_jupyter_intro.ipynb`](notebooks/00_jupyter_intro/00_jupyter_intro.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/00_jupyter_intro/00_jupyter_intro.ipynb) |
| 01 | Foundations and Traditional Machine Learning | [`01_foundations_traditional_ml.ipynb`](notebooks/01_foundations_traditional_ml/01_foundations_traditional_ml.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/01_foundations_traditional_ml/01_foundations_traditional_ml.ipynb) |
| 02 | Modern Machine Learning Techniques | [`02_modern_ml_techniques.ipynb`](notebooks/02_modern_ml_techniques/02_modern_ml_techniques.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/02_modern_ml_techniques/02_modern_ml_techniques.ipynb) |
| 03 | Interpretable Machine Learning | [`03_interpretable_ml.ipynb`](notebooks/03_interpretable_ml/03_interpretable_ml.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/03_interpretable_ml/03_interpretable_ml.ipynb) |
| 04 | Special Topics in Machine Learning | [`04_special_topics_ml.ipynb`](notebooks/04_special_topics_ml/04_special_topics_ml.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/04_special_topics_ml/04_special_topics_ml.ipynb) |
| 05 | Working with Generative AI: Basics and Best Practices | [`05_genai_basics_best_practices.ipynb`](notebooks/05_genai_basics_best_practices/05_genai_basics_best_practices.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/05_genai_basics_best_practices/05_genai_basics_best_practices.ipynb) |
| 06 | Advanced Concepts in Generative AI | [`06_genai_advanced_concepts.ipynb`](notebooks/06_genai_advanced_concepts/06_genai_advanced_concepts.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/06_genai_advanced_concepts/06_genai_advanced_concepts.ipynb) |
| 07 | Introduction to Agentic AI: Concepts and Applications | [`07_agentic_ai.ipynb`](notebooks/07_agentic_ai/07_agentic_ai.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-github-username>/<repo-name>/blob/main/notebooks/07_agentic_ai/07_agentic_ai.ipynb) |

> **Note.** Replace `<your-github-username>` and `<repo-name>` in the badge links with your actual GitHub username and repository name once the repo is created.

---

## Getting Started

### Option A — Run online (Google Colab, recommended)

If you have never used Python or Jupyter before, this is the easiest path:

1. Click the **Open in Colab** badge of the notebook you want to use (table above, or badge at the top of each notebook).
2. Sign in to Google when prompted.
3. Run cells with **Shift + Enter**. The first cell installs all required packages automatically.
4. *(Optional)* Choose **Runtime → Change runtime type → GPU** for notebooks that involve deep learning.

No local installation is needed. Your changes can be saved to your own Google Drive via **File → Save a copy in Drive**.

> **New to Jupyter?** Start with [`00_jupyter_intro.ipynb`](notebooks/00_jupyter_intro/00_jupyter_intro.ipynb) — it walks you through cells, kernels, shortcuts, and the Colab UI in five minutes.

### Option B — Run locally

Requires **Python ≥ 3.10** and `pip`. We recommend a fresh virtual environment.

```bash
# 1. Clone the repository
git clone https://github.com/<your-github-username>/<repo-name>.git
cd <repo-name>

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows (PowerShell)

# 3. Install dependencies (choose one)

# 3a. Everything at once
pip install -r requirements.txt

# 3b. Just one section
pip install -r notebooks/01_foundations_traditional_ml/requirements.txt

# 4. Launch Jupyter
jupyter lab
```

Then open the desired notebook from the JupyterLab file browser.

---

## Prerequisites

- **Python** ≥ 3.10 *(only for local execution; Colab handles this for you)*.
- **Basic Python familiarity** is helpful but not required — the notebooks introduce concepts as they go.
- **A Google account** if you want to use Colab.
- **API keys** for some GenAI notebooks (Sections 5–7). The relevant notebook explains which provider is used (e.g. OpenAI, Anthropic, or a free/open alternative) and how to set the key as an environment variable. **Never commit API keys to the repository.**

---

## Data & Datasets

- **Small datasets** (a few MB) are checked into the relevant `data/` folder.
- **Larger or third-party datasets** are downloaded at runtime from their original source (e.g. scikit-learn, OpenML, Keras, Hugging Face Hub) — this keeps the repository small and respects the licenses of the original data providers.
- All datasets are used for **educational purposes only**.

---

## Troubleshooting

- **A package fails to install on Colab.** Re-run the install cell; if it still fails, restart the runtime (**Runtime → Restart runtime**) and try again.
- **Out-of-memory errors.** On Colab, switch to a **High-RAM** or **GPU** runtime (**Runtime → Change runtime type**).
- **A notebook works on Colab but not locally.** Ensure you installed the *section-specific* `requirements.txt`, not just the aggregated one — version pins may differ.
- **Different results on different machines.** Some methods are stochastic. Look for a `random_state` / `seed` argument in the relevant cell.

---

## Instructor

**Dr. Simon Hatzesberger**
Seminar on behalf of the [European Actuarial Academy (EAA)](https://actuarial-academy.com).

---

## License

The **code** in this repository is released under the [MIT License](LICENSE).
The **seminar slides and accompanying text** remain © Dr. Simon Hatzesberger and the European Actuarial Academy; please do not redistribute them without permission.

Third-party datasets retain the licenses of their respective providers.

---

## Acknowledgments

This material was prepared for the European Actuarial Academy. Many of the examples build on the open-source Python ecosystem — in particular **scikit-learn**, **PyTorch**, **Hugging Face Transformers**, **SHAP**, and the many libraries that make modern ML and GenAI accessible to practitioners.
