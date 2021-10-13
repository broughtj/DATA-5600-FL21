## Standard library imports
from abc import ABC, abstractmethod

## Third party library imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


__all__ = ['BayesianAgent', 'BetaBinomialAgent']


## Constants
NOT_IMPLEMENTED = "This is an abstract method. Derived classes must implement it."


class BayesianAgent(ABC):
    @abstractmethod
    def update(self, observation: float):
        raise NotImplementedError(NOT_IMPLEMENTED)
    
    @abstractmethod
    def plot(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class BetaBinomialAgent(BayesianAgent):
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.num_obs = 0

    def update(self, data):
        self.alpha += np.sum(data) 
        self.beta += np.sum(1 - data) 
        self.num_obs += len(data)

    def plot(self):
        x = np.linspace(0, 1, 1000)
        y = stats.beta.pdf(x, self.alpha, self.beta)
        plt.plot(x, y, lw = 2.0, color='darkblue', alpha=1.0)
        plt.fill_between(x, y, facecolor='blue', alpha=0.3)
        plt.title(f"Beta({self.alpha},{self.beta}) Prior Distribution")
        plt.show()
        
        
class GammaPoisson(BayesianAgent):
    pass


if __name__ == "__main__":
    print("This is a module. It cannot be run directly, but rather must be imported to use it.")