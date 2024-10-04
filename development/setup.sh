#!/bin/bash

# Create the directory structure
mkdir -p fastAPIOrchestration/{app/{models,routers,data},tests}

# Create __init__.py files
touch fastAPIOrchestration/app/__init__.py
touch fastAPIOrchestration/app/models/__init__.py
touch fastAPIOrchestration/app/routers/__init__.py
touch fastAPIOrchestration/tests/__init__.py

# Create main.py
touch fastAPIOrchestration/app/main.py

# Create model files
touch fastAPIOrchestration/app/models/product.py
touch fastAPIOrchestration/app/models/category.py
touch fastAPIOrchestration/app/models/review.py

# Create router files
touch fastAPIOrchestration/app/routers/products.py
touch fastAPIOrchestration/app/routers/categories.py
touch fastAPIOrchestration/app/routers/reviews.py

# Create sample data file
touch fastAPIOrchestration/app/data/sample_data.py

# Create test files
touch fastAPIOrchestration/tests/test_products.py
touch fastAPIOrchestration/tests/test_categories.py
touch fastAPIOrchestration/tests/test_reviews.py

# Create project root files
touch fastAPIOrchestration/requirements.txt
touch fastAPIOrchestration/README.md
touch fastAPIOrchestration/.gitignore

