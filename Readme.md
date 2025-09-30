# End to End Data Science project



### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub



## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config   //⚙️Python helpers to load/parse config.yaml and schema.yaml.
6. Update the components
7. Update the pipeline 
8. Update the main.py




📂 Project Structure & Roles

Top-level files/folders

📁 config/
✨ config.yaml → Central configuration file for paths, model hyperparameters, database connections, etc.
✨ Keeps your pipeline flexible without hardcoding values.

📁 experiment/
✨ Stores experiment runs (metrics, artifacts, models, etc.).
✨ Helps in experiment tracking if you’re not using MLflow/W&B.

📁 Logs/
✨ Contains runtime logs (training, evaluation, error logs).
✨ Useful for debugging and monitoring pipeline runs.

📁 src/DataScience/ (main source code package)
✨ Core ML codebase. Let’s break it down:

   - 📁 components/ → 🧩 Reusable building blocks (e.g., data ingestion, preprocessing, training, evaluation). Each  script handles one major step.

   - 📁 config/ → ⚙️ Python helpers to load/parse config.yaml and schema.yaml.

   - 📁 constants/ → 📏 Store global constants (like file paths, feature names, column mappings).

   - 📁 entity/ → 🗂️ ONLY DEFINE data entities (e.g., input/output dataclasses, structured schemas).

   - 📁 pipeline/ → 🔗 Orchestration scripts that connect components (end-to-end ML pipeline).

   - 📁 utils/ → 🛠️ Helper functions (logging, file I/O, validation, metrics calculation).

📄 __init__.py → 📦 Makes DataScience a Python package.

📁 templates/
✨ 📑 Jinja2 or YAML/JSON templates for generating config files, reports, or metadata.

📄 .gitignore
✨ 🚫 Excludes unnecessary files (logs, models, venv, cache) from git commits.

📄 Dockerfile
✨ 🐳 Defines containerization setup. Ensures reproducibility across environments (same dependencies, system libs).

📄 main.py
✨ ▶️ Entry point for running the entire ML pipeline.
✨ Example: python main.py train could trigger data ingestion → preprocessing → training → evaluation.

📄 params.yaml
✨ 🎚️ Stores model-specific hyperparameters (learning rate, epochs, batch size).
✨ Often used with pipeline orchestrators like DVC.

📄 Readme.md
✨ 📖 Project documentation, setup instructions, workflow description.

📄 requirement.txt
✨ 📦 Python dependencies list for pip installation.

📄 schema.yaml
✨ 📝 Defines schema/validation rules for datasets (column names, types, ranges).
✨ Helps catch data drift and schema mismatches.