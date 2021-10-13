## Standard library imports 
from abc import ABC, abstractclassmethod, abstractmethod

## Third party library imports
import numpy as np
from scipy import stats


__all__= []


## Constants
NOT_IMPLEMENTED = "This is an abstract method. It must be implemented in the subclass."


## Custom exceptions
class InvalidBanditSelectionError(Exception):
    def __init__(self, choice):
        message = f"{choice} is not a valid selection."
        super().__init__(message)


class SimulationEnvironment:
    def __init__(self, bandits, agent, rounds=1_000):
        self.bandits = bandits
        self.agent = agent
        self.__rounds = rounds

    @property
    def rounds(self):
        return self.__rounds

    @rounds.setter 
    def rounds(self, new_rounds):
        self.__rounds = new_rounds

    def execute(self):
        print(self.bandits.thetas)
        virtual_cherries = np.sum(self.agent.alpha)
        for i in range(self.__rounds):
            ## Thompson Sampling step
            choice = self.agent.action()

            ## Observation step
            reward = self.bandits.pull(choice)

            ## Update step
            self.agent.update(reward)

            if i == self.__rounds - 1:
                print(self.agent.trials, self.agent.alpha, self.agent.beta)
                print(np.sum(self.agent.alpha)- virtual_cherries)
        


class BernoulliBandits:
    def __init__(self, thetas: np.ndarray):
        self.thetas = thetas

    def pull(self, choice: int):
        try:
            reward = np.random.binomial(n=1, p=self.thetas[choice], size=1)
        except:
            raise InvalidBanditSelectionError(choice) 

        return reward

    def __len__(self):
        return len(self.thetas)



class SelectionHeuristic(ABC):
    @abstractmethod
    def select(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class SimpleGreedy(SelectionHeuristic):
    def select(self, a, b):
        if (np.min(a) == np.max(a)) and (np.min(b) == np.max(b)):
            result = np.random.randint(len(a))
        else:
            result = np.argmax(stats.beta(a, b).mean())
        return result
        

class ThompsonSampler(SelectionHeuristic):
    def select(self, a, b):
        return np.argmax(np.random.beta(a, b))


class BayesianUCB(SelectionHeuristic):
    def __init__(self, alpha = 0.975):
        self.alpha = alpha

    def select(self, a, b):
        if (np.min(a) == np.max(a)) and (np.min(b) == np.max(b)):
            result = np.random.randint(len(a))
            #print(result, "random")
        else:
            result = np.argmax(stats.beta(a, b).ppf(self.alpha))
            #print(result, "UCB")

        return result


class BayesianAgent(ABC):
    @abstractmethod
    def action(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def update(self, reward):
        raise NotImplementedError(NOT_IMPLEMENTED)


class BetaBinomialAgent(BayesianAgent):
    def __init__(self, alpha: np.ndarray, beta: np.ndarray, selector: SelectionHeuristic):
        assert len(alpha) == len(beta)
        self.alpha = alpha
        self.beta = beta
        self.selector = selector
        self.choice = None
        self.trials = np.zeros(len(alpha))

    def action(self):
        self.choice = self.selector.select(self.alpha, self.beta)
        return self.choice

    def update(self, reward):
        self.alpha[self.choice] += np.sum(reward)
        self.beta[self.choice] += np.sum(1 - reward)
        self.trials[self.choice] += len(reward)


if __name__ == "__main__":
    ## Set the number of rounds
    m = 1_000

    ## Set up the stochastic environment
    #thetas = np.array([0.55, 0.6, 0.65])
    thetas = np.random.uniform(size=3)
    bandits = BernoulliBandits(thetas)

    the_seed = np.random.randint(10_000)
    print(f"The seed value is: {the_seed}")

    ####### Thompson Sampling ######
    np.random.seed(the_seed)
    alpha = np.ones(len(bandits))
    beta = np.ones(len(bandits))
    ts_sampler = ThompsonSampler()
    jake = BetaBinomialAgent(alpha, beta, ts_sampler)

    sim1 = SimulationEnvironment(bandits, jake, rounds=m)
    sim1.execute()

    print("\n")

    ###### Bayes UCB ######
    np.random.seed(the_seed)
    bucb = BayesianUCB(0.975)
    alpha = np.ones(len(bandits))
    beta = np.ones(len(bandits))
    jick = BetaBinomialAgent(alpha, beta, bucb)

    sim2 = SimulationEnvironment(bandits, jick, rounds=m)
    sim2.execute()

    print("\n")

    ###### Greedy ######
    np.random.seed(the_seed)
    greedy = SimpleGreedy()
    alpha = np.ones(len(bandits))
    beta = np.ones(len(bandits))
    jike = BetaBinomialAgent(alpha, beta, greedy)

    sim3 = SimulationEnvironment(bandits, jike, rounds=m)
    sim3.execute()