import numpy as np

#? ---------------- Activation Functions ---------------- #

def binaryStep(x, theta=0):
    return np.where(x >= theta, 1, 0)

def bipolarStep(x, theta=0):
    return np.where(x >= theta, 1, -1)

def binarySigmoid(x):
    return 1 / (1 + np.exp(-x))

def bipolarSigmoid(x):
    return (2 / (1 + np.exp(-x))) - 1

def identity(x):
    return x

def ramp(x):
    return np.maximum(0, x)

#? ---------------- Activation Dictionary ---------------- #

activation_functions = {
    "binarysigmoid": binarySigmoid,
    "bipolarsigmoid": bipolarSigmoid,
    "binarystep": binaryStep,
    "bipolarstep": bipolarStep,
    "identity": identity,
    "ramp": ramp
}

#todo ---------------- ANN Class ---------------- #

class ANN:
    def __init__(self, layers, activation="binarysigmoid", weights=None, biases=None):
        self.layers = layers
        self.activation_name = activation
        self.activation = activation_functions[activation]
        self.weights = weights
        self.biases = biases
    
    def forward(self, X):
        a = X
        for i, (w, b) in enumerate(zip(self.weights, self.biases)):
            print(f"\n--- Layer {i+1} ---")
            print("Input:", a)

            z = np.dot(a, w) + b
            print("Weighted sum (z):", z)

            # لو step function → نمرر theta
            if "step" in self.activation_name:
                a = self.activation(z, 0)
            else:
                a = self.activation(z)

            print("Output:", a)

        return a

#! ---------------- Main Program ---------------- #

if __name__ == "__main__":
    num_inputs = int(input("Enter number of inputs: "))
    
    inputs = np.array(
        [float(x) for x in input(f"Enter {num_inputs} input values: ").split()]
    ).reshape(1, -1)

    num_layers = int(input("Enter number of layers: "))
    
    layers = []
    for i in range(num_layers):
        neurons = int(input(f"Enter number of neurons in layer {i+1}: "))
        layers.append(neurons)

    activation = input(
        "Choose activation (binarysigmoid / bipolarsigmoid / binarystep / bipolarstep / identity / ramp): "
    ).lower()

    weights = []
    biases = []
    prev_size = num_inputs

    for i, layer_size in enumerate(layers):
        print(f"\nLayer {i+1}")
        print(f"Enter weights matrix ({prev_size} x {layer_size}):")

        w = []
        for r in range(prev_size):
            row = [float(x) for x in input(f"Row {r+1}: ").split()]
            w.append(row)

        weights.append(np.array(w))

        print(f"Enter biases ({layer_size} values):")
        b = np.array([float(x) for x in input().split()]).reshape(1, -1)

        biases.append(b)
        prev_size = layer_size

    ann = ANN([num_inputs] + layers, activation, weights, biases)

    output = ann.forward(inputs)

    print("\nFinal Output:", output)