# DATA 5600: Introduction to Regression and Machine Learning for Analytics

## __Some Brief Notes on Basic Probability Concepts__ <br>

Author:  Tyler J. Brough <br>
Updated: October 4, 2021 <br>

---

<br>


## __Probability Distributions__

These notes are based upon readings from the book _"Doing Bayesian Data Analysis_ by John Kruschke.

<br>

A ___probability distribution___ is the list of all possible outcomes and their corresponding probabilities. 

<br>

Notes:
* In class I said that this was a _"mapping from the event space to the probability space"_

* The distribution can be represented by a graph, a table, or a formula. 

* Sometimes a distinction is made been the probability _density_ and the probability _distribution_, the latter being when the random variable falls at or below some particular value. 

* We will use the terms interchangably and explicitly refer to the latter as the ___cumulative distribution function___ or simply the ___CDF___.


<br>

### __The Discrete Probability Density Function (Probability Mass Function)__

---

If the set of all possible values of a random variable, $X$, is a countable set,
$x_{1}, x_{2}, \ldots, x_{n}$, or $x_{1}, x_{2}, \ldots$, then $X$ is called a
__discrete random variable__. The function

$$
f(x) = P[X = x] \quad x = x_{1}, x_{2}, \ldots
$$

that assigns the probability to each possible value of $x$ will be called the 
__discrete probability density function__ (discrete PDF).

---


<br>
<br>

#### __Some Common Examples__

<br>

<u>__Example 1.__</u> The values of the discrete pdf of a roll of a fair die.

| x      | 1   | 2   | 3   | 4   | 5   | 6   |
|:-------|-----|-----|-----|-----|-----|-----|
| $f(x)$ | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |


<br>
<br>
<br>

<u>__Example 2.__</u> When tossing a coin with unknown probability of heads (success). The pdf is given by the ___Bernoulli distribution function___. 

$$
f(x; \theta) = \theta^{x} (1 - \theta)^{1-x} \quad x = \{0, 1\}
$$

__Note:__ 

* $P(X = 0) = 1 - \theta$

* $P(X = 1) = \theta$

<br>

A jar contains 30 green jelly beans and 20 purple jelly beans. What is the probability of
drawing a single green? A single purple?

$$
\begin{align}
P(\mbox{drawing a single green}) &= 30/50 = 0.6\\
& \\
P(\mbox{drawing a single purple}) &= 20/50 = 0.4
\end{align}
$$

<br>

We can confirm this in `Python` as follows:

```python
from scipy import stats
stats.binom(1, 0.6).pmf(1)
```

and 

```python
stats.binom(1, 0.6).pmf(0)
```

<br>
<br>


<u>__Example 3.__</u> When tossing a coin $n$ times and counting the number of heads the
pdf is given by the ___Binomial distribution function___.

$$
f(x; n, \theta) = \binom{n}{x} \theta^{x} (1 - \theta)^{n-x}
$$

<br>

A jar contians 30 green jelly beans and 20 purple jelly beans. Suppose 10 jelly beans are
selected at random from the jar. Find the probability of obtaining exactly five purple jelly
beans if they are selected with replacement.

```python
stats.binom(10, 0.4).pmf(5)
```

__Note:__ often the definitions of 'success' and 'failure' are arbitrary. In this case they
should be symmetric.

```python
stats.binom(10, 0.6).pmf(5)
```

<br>
<br>
<br>

### __The Cumulative Distribution Function (CDF)__

---

The __cumulative distribution function__ (CDF) of a random variable $X$ is defined for 
any real $x$ by

$$
F(x) = P[X \le x]
$$

---

<br>
<br>

<u>__Example 4.__</u> A jar contians 30 green jelly beans and 20 purple jelly beans. Suppose
10 jelly beans are selected at random from the jar. What is the probability of getting 4 or
fewer green jelly beans?

```python
stats.binom(10, 0.6).cdf(4)
```

Check this against the following and make sure it makes sense to you based on the definitions
of a discrete random variable and the CDF given above:

```python
p = 0
for i in range(5):
    p += stats.binom(10, 0.6).pmf(i)
print(p)
```

__Q:__ did you get the same answer? Why or why not?

<br>
<br>
<br>



### __The Continuous Probability Density Function__

---

A random variable $X$ is called a __conintuous random variable__ if there is a function
$f(x)$ called the __probability density function__ (pdf) of $X$, such that the CDF can be 
represented as

$$
F(X) = \int\limits_{-\infty}^{x} f(t) dt
$$

---

<br>
<br>

Examples go here...


<br>
<br>
<br>

### __The Central Limit Theorem__

---

Let $X_{1}, X_{2}, \ldots X_{n}$ be independent and identically 
distributed (_iid_) random variables with $E(X_{i}) = \mu$ and
$V(X_{i}) = \sigma^{2} < \infty$. Define

$$
U_{n} = \sqrt{n} \left( \frac{\bar{X} - \mu}{\sigma} \right) \quad \mbox{where} \quad \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_{i}
$$

Then the distribution function of $U_{n}$ converges to a standard
normal distribution as $n \rightarrow \infty$.

---

<br>
<br>

Examples go here...
