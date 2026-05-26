# Data for Section 4 — Special Topics in Machine Learning

This folder hosts the datasets used by `04_special_topics_ml.ipynb`. All datasets are downloaded **at notebook runtime** from their original providers; nothing large is checked into git.

## Datasets used

### 1. freMTPL2 (French motor third-party liability)
Used in Section 4.1 (imbalanced classification) and Section 4.3 (fairness sidebar).

- **Source**: `OpenML` — dataset id `41214`, mirror of the `CASdatasets` R package.
- **Loader**: `sklearn.datasets.fetch_openml("freMTPL2freq", version=1, as_frame=True, parser="auto")`.
- **License**: same as the CASdatasets package — distributed for research and teaching.
- **Size**: 678,013 policies × 12 columns. We downsample to ~50k rows for CPU-friendly examples and binarize `ClaimNb` as the imbalanced target.

### 2. CIFAR-10
Used in Section 4.2 (CNNs).

- **Source**: `torchvision.datasets.CIFAR10` — auto-downloaded to `data/cifar10/`.
- **License**: MIT-style, free for research and teaching.
- **Size**: 60,000 32×32 colour images in 10 classes. We use a stratified subset (~6,000 images) for CPU-friendly training.

> **Why CIFAR-10 in the notebook?** The slides illustrate Section 4.2 with images from the **Roboflow Universe car-damage dataset (CC BY 4.0)** — see "Optional override" below. CIFAR-10 is the default in the notebook so that it runs end-to-end on any laptop with no authentication required. The CNN architecture, training loop, evaluation code, and pedagogical narrative are identical regardless of which dataset you swap in.

### 3. MNIST
Used in Section 4.2's Grad-CAM exercise.

- **Source**: `torchvision.datasets.MNIST` — auto-downloaded to `data/mnist/`.
- **License**: public domain (Yann LeCun's site).
- **Size**: 60,000 28×28 grayscale digits. We use a 5,000-image subset for sub-minute training.

### 4. Folktables ACSIncome
Used in Section 4.3 (fairness, main hands-on).

- **Source**: `folktables.ACSDataSource(survey_year='2018', horizon='1-Year', survey='person')` — pulls the American Community Survey microdata from the US Census API.
- **License**: CC0 / US public domain (US Census public-use microdata).
- **Size**: ~200k rows for California state, 10 features.

## Optional override — Roboflow car-damage dataset

If you want to teach with the actual car-damage images shown on the slides, download the **Roboflow Universe `car-damage-detection-cpccb`** dataset (CC BY 4.0, ~4k images, 6 classes: `crack`, `dent`, `scratch`, `glass shatter`, `lamp broken`, `tire flat`):

1. Sign up for a free Roboflow account at <https://app.roboflow.com>.
2. Open the dataset page: <https://universe.roboflow.com/btp-w9pyz/car-damage-detection-cpccb>.
3. Download in **"Folder Structure"** format (PyTorch ImageFolder layout).
4. Unzip into this folder so the layout is:
   ```
   data/
     car_damage/
       train/
         crack/   *.jpg
         dent/    *.jpg
         glass_shatter/  *.jpg
         lamp_broken/    *.jpg
         scratch/        *.jpg
         tire_flat/      *.jpg
       valid/
         …
       test/
         …
   ```
5. The notebook's data-loading cell detects `data/car_damage/` automatically and switches over with no further configuration.

Attribution: Roboflow Universe — *Car Damage Detection* (workspace `btp-w9pyz`, project `car-damage-detection-cpccb`), licensed under **CC BY 4.0**.

---

Part of the EAA seminar *Machine Learning & Generative AI: A Hands-On Guide to Actuarial Practice* by Dr. Simon Hatzesberger. Code under the MIT License.
