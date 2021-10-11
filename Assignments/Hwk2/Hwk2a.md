# __DATA 5600__

## __Assignement 2a__


* Instructor: Tyler J. Brough
* Date Assigned: 10.10.MON
* Due Date: TBA
---

<br>


__Note:__ These problems are to help you practice your understanding of the Central Limit Theorem and sampling theory in general. 

<br>

---

<br>
<br>

__1.__ Workers employed in a large serve industry have an average wage of $\$5.00$ per hour with a standard deviation of $\$0.50$. The industry has 64 workers of a certain ethnic group. These workers have an average wage of $\$4.90$ per hour. Is it reasonable to assume that the wage rate of the ethnic group is equivalent to that of a random sample of workers from those employed in the service industry? 


<br>

__2.__ The length of time required for the periodic maintenance of an automobile or other machine usually has a mound shaped distribution. Because some occassional long-service times will occur, the distribution tends to be skewed to the right. Suppose that the length of time required to run a 5000-mile check and to service a new automobile has mean 1.4 hours and standard deviation of 0.7 hours. Suppose also that the service department plans to service fifty automobils per 8-hour day and that, in order to do so, it can only spend a maximum average service time of 1.6 hours per automobile. On what proportion of all work days will the service department have to work overtime?

<br>

__3.__ Many bulk products, such as iron ore, coal, and raw sugar, are sampled for quality by a method that requires many small samples to be taken periodically as the material is moving along a conveyor belt. The small samples are then combined and mixed to form one composite sample. Let $Y_{i}$ denote the volume of the $i$th sample from a particular lot, and suppose that $Y_{1}, Y_{2}, \ldots, Y_{n}$ constitute a random sample, with each $Y_{i}$ value having mean $\mu$ (in cubic inches) and variance $\sigma^{2}$. The average volume $\mu$ of the samples can be set by adjusting the size of the sampling device. Suppose that the variance $\sigma^{2}$ of the volumes of the samples is known to be approximately 4. The total volume of the composite sample must exceed 200 cubic inches with probability $0.95$ when $n = 50$ small samples are selected. Determine a setting for $\mu$ that will allow the sampling requirements to be satisfied.

<br>

__4.__ Twenty-five heat lamps are connected in a greenhouse so that when one lamp fails, another takes over immediately. (Only one lamp is turned on at any time.) The lamps operate independently, and each has a mean life of 50 hours and standard deviation of 4 hours. If the greenhouse is not checked for 1300 hours after the lamp system is turned on, what is the probability that a lamp will be burning at the end of the 1300-hour period?

<br>

__5.__ The times that a cashier spends processing each person's order are independent random variables with mean 2.5 minutes and standard deviation 2 minutes. What is the approximate probability that it will take more than 4 hours to process the orders of 100 people? 

<br>

__6.__ Suppose that the number of customers served per hour at a certain checkout is a Poisson random variable with unknown arrival rate $\lambda$. A dataset containing 100 observations of this service checkout station are available in the file `service_counts.csv`. 

You can read these data into a `numpy.ndarray` with the following snippet of code: 

```python
counts = np.loadtxt("service_counts.csv")
```

* __a.__ Calcualte the mean and variance of the dataset. 

* __b.__ Imagine that you have been hired as a consulting data analyst to do some basic analysis for this client. The client has a standard that each checkout station serve an average of 30 customers per hour with a standard deviation of $\sqrt{30}$. What is the probability that this checkout station meets the minimum standard? Use the CLT to answer this question. Plot the sampling distribution obtained. 


* __c.__ Check the answer you get from the CLT approach above with the following simulation study.
    - Draw 100,000 samples each of size $n = 100$ by drawing from the observed data with replacement.
    - This is called the naive IID Bootstrap. 
    - Calculate and store the mean of each simulated sample. 
    - Plot a histogram of the sampled means. 
    - Calculate the mean and standard error of the bootstrapped sampling distribution. 
    - Calculate the same probability as above using the empirical CDF. 
    - Compare to the results from the CLT approach. 


<br>

__6.__ You are a data analysis consultant for a coin factory. You have been given the dataset contained in the file `coin_data.csv`. These data represent
100 binomial experiments each of sample size $n = 100$. (That is, the coin was flipped 100 times and the number of heads were counted and recorded. Then this
process was repeated 100 times). Devise a test to check if the data were produced from a coin biased towards heads. Construct a bootstrap study to test the 
results you get via the Central Limit Theorem. 

<br>

You can read these data into an `numpy.nadarry` as follows:

```python
coin_flips = np.loadtxt("coin_data.csv")
```

