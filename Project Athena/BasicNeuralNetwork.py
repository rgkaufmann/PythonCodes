from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        random.seed(2)
        self.synaptic_weights = 2 * random.random((2,1)) - 1
        
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    
    def __sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment
            
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))
    
neural_network = NeuralNetwork()
print("Random starting synaptic weights: ")
print(neural_network.synaptic_weights)

training_set_inputs = array([[2, 9], [1, 5], [3, 6]])
training_set_outputs = array([[92/100, 86/100, 89/100]]).T

neural_network.train(training_set_inputs, training_set_outputs, 10000)

print("New synaptic weights after training: ")
print(neural_network.synaptic_weights)
print("Considering new situation: ")
print(neural_network.think(array([2, 9])))