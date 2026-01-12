# 🧠 Neural Networks and Deep Learning — Study Notes

This repository contains **concise notes, mathematical proofs, experiments, and solved exercises** based on
📘 *Neural Networks and Deep Learning* by Michael Nielsen.

The focus is on **conceptual clarity**, **mathematical correctness**, and **bridging theory with implementation**, rather than framework-specific code.

🔗 Official book reference: [http://neuralnetworksanddeeplearning.com/](http://neuralnetworksanddeeplearning.com/)

---

## 📂 Chapter 1 — Neural Network Foundations

This chapter builds the intuition behind neural networks, starting from perceptrons and moving toward differentiable models and optimization.

### Covered Concepts

* 📊 Binary outputs and probabilistic interpretation
* 🔁 Online learning vs. mini-batch learning
* 🔀 Sigmoid neurons as smooth approximations to perceptrons
* 📉 One-dimensional gradient descent experiments

### Key Takeaway

Establishes why **differentiability and gradient-based learning** are central to neural networks.

---

## 📂 Chapter 2 — Backpropagation Theory

This chapter focuses exclusively on the **mathematical derivation of backpropagation**, independent of code.

### Covered Concepts

* 🧮 Vectorized backpropagation equations
* ✍️ Formal proofs of error propagation across layers

### Key Takeaway

Provides a rigorous understanding of **how and why gradients flow backward** in neural networks.

---

## 📂 Chapter 3 — Improving Learning (Solved Exercises)

This chapter contains fully solved theoretical exercises focused on optimization and cost functions.

### Solved Topics

* 📐 Analytical verification of the sigmoid derivative
* ⚠️ Common pitfalls in cross-entropy formulations
* 📉 Proof that cross-entropy is minimized when predictions match targets, including soft-label cases
* 🔢 Interpretation of the resulting minimum as binary entropy

### Key Takeaway

Clarifies why **cross-entropy is the preferred loss function** for probabilistic models.

---

## 🎯 Repository Goals

* 📘 Deepen understanding of neural network fundamentals
* ✍️ Practice mathematical reasoning behind learning algorithms
* 🧪 Validate theory through minimal experiments
* 🧠 Build strong foundations before using high-level frameworks
