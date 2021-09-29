# __DATA 5600__

## __Assignement 1b__


* Instructor: Tyler J. Brough
* Date Assigned: 09.20.MON
* Due Date: TBA
---

<br>


__Note:__ The purpose of these problems is to help refresh your understanding and use of basic probability theory. A twin goal is to help you use `Python` to solve such problems. 

For each problem write out a solution using Markdown and $\LaTeX$. And also give a `Python` implementation. The deliverable format is a Python Jupyter notebook containing all of your answers. 

__NB:__ I urge you to resist the urge to Google for solutions. Instead let's solve these problems together! 

---

<br>
<br>

__1.__ In a 10 question true-false test:

* (a) What is the probability of getting all answers correct by guessing?
* (b) What is the probability of getting eight correct by guessing?


<br>

__2.__ A basketball player shoots 10 shots and the probability of hitting ($\theta$) is 0.5 on each shot. 

* (a) What is the probability of hitting eight shots? 
* (b) What is the probability of hitting eight shots if the probability on each shot is 0.6?
* (c) What are the expected value and variance of the number of shots hit if $\theta = 0.5$?

<br>

__3.__ A four-engine plane can fly if at least two engines work.

* (a) If the engines operate independently and each malfunctions with probability $q = 1 - \theta$, what is the probability that the plane will fly safely?
* (b) A two-engine plan can fly if at least one engine works. If an engine malfunctions with probability $q = 1 - \theta$, what is the probability that the plane will fly safely?
* (c) Which plane is the safest?
* NB: Solve the above generically, but you may want to choose some specific probabilities to get started. Try something like the following values: $\theta = [0.5, 0.6, 0.75, 0.8]$

<br>

__4__. The Chevalier de Mere used to bet that he would get at least one 6 in four rolls of die. 

* (a) Was his bet a good one? 
* (b) He also bet that he would get at least one pair of 6's in 24 rolls of two dice. What was his probability of winning this bet? 
* (c) Compare the probability of at least one 6 when six dice are rolled with the probability of at least two 6's when 12 dice are rolled. 


<br>

__5__. If the probability of picking a winning horse in a race is $\theta = 0.2$, and if $X$ is the number of winning picks out of 20, give the values to the following:

* (a) $P[X = 4]$
* (b) $P[X \le 4]$ 
* (c) $E(X)$ and $Var(X)$

<br>

__6__. A jar contians 30 green jelly beans and 20 purple jelly beans. Suppose 10 jelly beans are selected at random from the jar. 

- (a) Find the probability of obtaining exactly five purple jelly beans if they are selected with replacement.
- (b) Find the probability of obtaining exactly five purple beans if they are selected withour replacement. 

<br>

__7__. An office has 10 employees, three men and four seven women. The manager chooses four at random to attend a short course on quality improvement. 

- (a) What is the probability that an equal number of men and women are chosen?
- (b) What is the probability that more women are chosen?

<br>

__8__. A shipment of 50 mechanical devices consists of 42 good ones and eight defective. An inspector selects five devices at random without replacement. 

- (a) What is the probability that exactly three are good? 
- (b) What is the probability that at most three are good? 


<br>

__9__. The probability that a patient recovers from a stomach disease is $0.8$. Suppose 20 people are known to have contracted this disease. 

- (a) What is the probability that exactly fourteen survive? 
- (b) What is the probability that at least ten survive?
- (c) What is the probability that at least fourteen but not more than eighteen survive?
- (d) What is the probability that at most sixteen survive?

<br>

__10__. Three Bayesians Anne, Beth, and Greg are flipping a coin that may or may not be biased. Anne has a prior of $\beta(2,8)$, Beth has a prior of $\beta(1,1)$, and Greg has a prior of $\beta(8,2)$. 

- (a) Write a simulation to demonstrate the convergence of their beliefs as they gather data by flipping the coin. 
- (b) Test your simulation with the following values for the probability of heads: $\theta = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]$

<br>

__11__. There are 3 candy machines in front of you that each dispense either chocolate or cherry flavored Tootsie Rolls. Each has a different probability of dispensing chocolate versus cherry flavors. Your absolute favorite flavor is cherry. You can draw one Tootsie Roll at a time from a single candy machine. The dispensing probabilities remain constant over time. 

- Outline a strategy to obtain as many cherry flavored Tootsie Rolls as possible for a fixed set of draws. 
- This is a tough problem. Use computational and statistical thinking to come up with a strategy. Use your imagination. Be adventurous. 
- ___Hint:___ Use Bayes's Rule! 
