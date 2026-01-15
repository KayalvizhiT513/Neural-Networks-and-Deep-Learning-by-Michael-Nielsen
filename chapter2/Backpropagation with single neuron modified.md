# Backpropagation with a Single Modified Neuron

## Question

**Backpropagation with a single modified neuron**  
Suppose we modify a single neuron in a feedforward network so that the output from the neuron is given by  
\( f\!\left(\sum_j w_j x_j + b\right) \), where \( f \) is some function other than the sigmoid.  
How should we modify the backpropagation algorithm in this case?

---

## Answer

Let  
\[
z = \sum_j w_j x_j + b, \quad a = f(z)
\]
for the modified neuron, while all other neurons continue to use the sigmoid activation \( \sigma \).

### Key Idea
Backpropagation relies on the chain rule. The activation function appears **only through its derivative**.  
Therefore, the algorithm is modified **only locally** by replacing \( \sigma'(z) \) with \( f'(z) \) for the modified neuron.

---

### Case 1: Modified Neuron in the Output Layer

The output error term becomes:
\[
\delta^L = \nabla_a C \odot f'(z^L)
\]
instead of:
\[
\delta^L = \nabla_a C \odot \sigma'(z^L)
\]

---

### Case 2: Modified Neuron in a Hidden Layer \( l \)

For the modified neuron \( j \) in layer \( l \):
\[
\delta^l_j = \left((w^{l+1})^T \delta^{l+1}\right)_j \, f'(z^l_j)
\]

All other neurons \( k \) in the same layer use:
\[
\delta^l_k = \left((w^{l+1})^T \delta^{l+1}\right)_k \, \sigma'(z^l_k)
\]

---

### Gradients for Weights and Biases (Unchanged)

Once the correct error term \( \delta^l \) is computed:
\[
\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \, \delta^l_j
\quad \text{and} \quad
\frac{\partial C}{\partial b^l_j} = \delta^l_j
\]

---

This works because backpropagation is a direct application of the chain rule, and each neuron contributes only a local derivative to the global gradient.
