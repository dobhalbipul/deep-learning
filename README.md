# Deep Learning Projects 🧠

A comprehensive collection of deep learning implementations using TensorFlow and Keras, covering fundamental concepts to advanced neural network architectures.

## 📚 Project Overview

This repository contains practical implementations of various deep learning concepts, from basic neural networks to advanced architectures like CNNs, RNNs, and LSTMs. Each project includes detailed Jupyter notebooks with explanations, code, and visualizations.

## 🗂️ Repository Structure

```
deep-learning/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── notebooks/
    ├── Testing.ipynb
    ├── edureka/                    # Edureka course materials
    │   ├── m3_Image_Classification.ipynb
    │   ├── m4_CNN_using_MNIST_dataset.ipynb
    │   ├── m5_Single_Layered_Perceptron.ipynb
    │   ├── m6_tensorboard.ipynb
    │   ├── m8_text_generation_using_RNNs_and_LSTM.ipynb
    │   ├── sonnets.txt
    │   ├── logs/                   # TensorBoard logs
    │   └── training_checkpoints_LSTM/  # Model checkpoints
    └── tensorflow/                 # TensorFlow implementations
        ├── first_model.ipynb
        ├── 1_digits_recognition/
        ├── 1_keras_fashion_mnist_neural_net/
        ├── 16_cnn_cifar10_small_image_classification/
        ├── 17_data_augmentation/
        ├── 18_transfer_learning/
        ├── 19_vectorstore/
        ├── 2_activation_functions/
        ├── 22_word_embedding/
        ├── 3_derivatives/
        ├── 4_matrix_math/
        ├── 5_loss/
        ├── 6_gradient_descent/
        ├── 7_nn_from_scratch/
        └── 8_sgd_vs_gd/
```

## 🚀 Key Features

### Neural Network Fundamentals
- **Basic Neural Networks**: Simple neural networks with no hidden layers
- **Multi-layer Perceptrons**: Networks with hidden layers for improved performance
- **Activation Functions**: Implementation and comparison of different activation functions
- **Gradient Descent**: Understanding optimization algorithms (SGD vs GD)
- **Loss Functions**: Various loss function implementations
- **Neural Networks from Scratch**: Pure Python implementation without high-level libraries

### Computer Vision
- **MNIST Digit Recognition**: Handwritten digit classification
- **Fashion MNIST**: Clothing item classification
- **CIFAR-10 Classification**: Small image classification with CNNs
- **Image Data Augmentation**: Techniques to improve model generalization
- **Transfer Learning**: Using pre-trained models for new tasks

### Advanced Architectures
- **Convolutional Neural Networks (CNNs)**: For image processing tasks
- **Recurrent Neural Networks (RNNs)**: For sequence data
- **Long Short-Term Memory (LSTM)**: For text generation and sequence modeling
- **Text Generation**: Shakespeare sonnet generation using RNNs/LSTMs

### Tools & Visualization
- **TensorBoard Integration**: Model monitoring and visualization
- **Word Embeddings**: Natural language processing techniques
- **Vector Stores**: Efficient similarity search implementations

## 🛠️ Technologies Used

- **Python 3.x**
- **TensorFlow 2.x**: Primary deep learning framework
- **Keras**: High-level neural networks API
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning utilities
- **OpenCV**: Computer vision tasks
- **Jupyter Notebooks**: Interactive development environment

## 📋 Prerequisites

- Python 3.7 or higher
- CUDA-compatible GPU (optional but recommended for faster training)
- 8GB+ RAM recommended

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dobhalbipul/deep-learning.git
   cd deep-learning
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

## 🎯 Getting Started

### For Beginners
1. Start with `tensorflow/1_digits_recognition/` for basic neural network concepts
2. Move to `tensorflow/2_activation_functions/` to understand activation functions
3. Explore `tensorflow/7_nn_from_scratch/` to build networks from scratch

### For Intermediate Users
1. Dive into `tensorflow/16_cnn_cifar10_small_image_classification/` for CNN implementation
2. Explore `edureka/m4_CNN_using_MNIST_dataset.ipynb` for detailed CNN explanations
3. Check out `tensorflow/17_data_augmentation/` for advanced preprocessing

### For Advanced Users
1. Implement text generation with `edureka/m8_text_generation_using_RNNs_and_LSTM.ipynb`
2. Explore transfer learning in `tensorflow/18_transfer_learning/`
3. Work with vector stores in `tensorflow/19_vectorstore/`

## 📊 Project Highlights

### 1. MNIST Digit Recognition
- Simple neural network vs. hidden layer comparison
- Achieves ~98% accuracy on test set
- Includes confusion matrix visualization

### 2. CIFAR-10 CNN Implementation
- Convolutional layers with max pooling
- Achieves ~86% accuracy (significant improvement over ANN)
- Demonstrates the power of CNNs for image classification

### 3. Text Generation with LSTM
- Shakespeare sonnet generation
- Character-level language modeling
- Model checkpointing for training continuation

### 4. Neural Network from Scratch
- Pure Python implementation
- Gradient descent algorithm implementation
- Weight and bias initialization strategies

## 🔍 Key Learning Outcomes

- Understanding of neural network fundamentals
- Hands-on experience with TensorFlow and Keras
- Implementation of various deep learning architectures
- Experience with real-world datasets (MNIST, CIFAR-10, Fashion-MNIST)
- Understanding of optimization techniques and hyperparameter tuning
- Visualization and monitoring of model training
- Text processing and natural language understanding

## 📈 Model Performance

| Model | Dataset | Accuracy | Notes |
|-------|---------|----------|-------|
| Simple NN | MNIST | ~92% | No hidden layers |
| MLP | MNIST | ~98% | With hidden layer |
| CNN | CIFAR-10 | ~86% | Convolutional architecture |
| ANN | CIFAR-10 | ~52% | Fully connected |
| LSTM | Text Generation | N/A | Shakespeare sonnets |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Edureka**: For comprehensive deep learning course materials
- **TensorFlow Team**: For the excellent deep learning framework
- **Keras Team**: For the user-friendly high-level API
- **OpenAI**: For inspiration in AI/ML education

## 📞 Contact

**Bipul Dobhal**
- GitHub: [@dobhalbipul](https://github.com/dobhalbipul)
- Email: [your-email@example.com]

## 🔗 Useful Resources

- [TensorFlow Documentation](https://www.tensorflow.org/guide)
- [Keras Documentation](https://keras.io/guides/)
- [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)

---

⭐ **Star this repository if you found it helpful!** ⭐