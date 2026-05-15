import math, random

def sigmoid(x): return 1 / (1 + math.exp(-x))
def sigmoid_d(x): s = sigmoid(x); return s * (1-s)

class NeuralNet:
    def __init__(self, layers):
        self.weights = []
        self.biases = []
        for i in range(len(layers)-1):
            w = [[random.uniform(-1,1) for _ in range(layers[i])] for _ in range(layers[i+1])]
            b = [random.uniform(-1,1) for _ in range(layers[i+1])]
            self.weights.append(w)
            self.biases.append(b)
    
    def forward(self, x):
        for W, B in zip(self.weights, self.biases):
            new_x = []
            for j, (row, b) in enumerate(zip(W, B)):
                val = sum(xi*wij for xi,wij in zip(x,row)) + b
                new_x.append(sigmoid(val))
            x = new_x
        return x
    
    def train(self, data, epochs=1000, lr=0.5):
        for epoch in range(epochs):
            total_loss = 0
            for inputs, target in data:
                output = self.forward(inputs)
                loss = sum((o-t)**2 for o,t in zip(output,target))
                total_loss += loss
            if epoch % 200 == 0:
                print(f"  Epoch {epoch}: Loss = {total_loss/len(data):.4f}")

# Train XOR
net = NeuralNet([2, 4, 1])
xor_data = [
    ([0,0], [0]),
    ([0,1], [1]),
    ([1,0], [1]),
    ([1,1], [0]),
]

print("Simple Neural Network")
print("=====================")
print("Training a neural network to learn XOR...")
print("XOR: 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0")
print()
net.train(xor_data, 2000)

print("\nResults after training:")
print("Input  | Expected | Got")
for inputs, target in xor_data:
    output = net.forward(inputs)
    predicted = round(output[0])
    correct = "✅" if predicted == target[0] else "❌"
    print(f"  {inputs} |    {target[0]}     | {output[0]:.3f} ({predicted}) {correct}")
