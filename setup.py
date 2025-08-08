"""
Setup script for Deep Learning Projects
"""

from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="deep-learning-projects",
    version="1.0.0",
    author="Bipul Dobhal",
    author_email="your-email@example.com",
    description="A comprehensive collection of deep learning implementations using TensorFlow and Keras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dobhalbipul/deep-learning",
    project_urls={
        "Bug Tracker": "https://github.com/dobhalbipul/deep-learning/issues",
        "Documentation": "https://github.com/dobhalbipul/deep-learning#readme",
        "Source Code": "https://github.com/dobhalbipul/deep-learning",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "isort>=5.0",
            "mypy>=0.800",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.0.0",
            "ipywidgets>=7.0.0",
        ],
        "visualization": [
            "plotly>=5.0.0",
            "seaborn>=0.11.0",
            "matplotlib>=3.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            # Add any command-line scripts here
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.yml", "*.yaml"],
    },
    keywords=[
        "deep learning",
        "machine learning",
        "tensorflow",
        "keras",
        "neural networks",
        "cnn",
        "rnn",
        "lstm",
        "computer vision",
        "natural language processing",
        "artificial intelligence",
        "python",
        "jupyter",
        "education",
        "tutorial",
    ],
    zip_safe=False,
)
