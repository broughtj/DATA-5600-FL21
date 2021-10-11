##### <u><b>Example 1</b></u>

The observed lifetimes (in months) of 40 electrical parts are given below.

<br>

|        |        |        |        |        |        |        |        |
|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|   0.15 |   2.37 |   2.90 |   7.39 |   7.99 |  12.05 |  15.17 |  17.56 |
|  22.40 |  34.84 |  35.39 |  36.38 |  39.52 |  41.07 |  46.50 |  50.52 |
|  52.54 |  58.91 |  58.93 |  66.71 |  71.48 |  71.84 |  77.66 |  79.31 |
|  80.90 |  90.87 |  91.22 |  96.35 | 108.92 | 112.26 | 122.71 | 126.87 |
| 127.05 | 137.96 | 167.59 | 183.53 | 282.49 | 335.33 | 341.19 | 409.97 |

<br>

It is argued that an exponential distribution of lifetimes might be reasonable. We will assume that
the data are the observed values of a random sample of size $n = 40$ from an exponential distribution, 
$X \sim EXP(\theta)$, where $\theta$ is the mean lifetime.

<br>

We will use the arithmetic average as an estimator for $\theta$.

<br>

```python
x = np.array([0.15, 2.37, 2.90, 7.39, 7.99, 12.05, 15.17, 17.56,
              22.40, 34.84, 35.39, 36.38, 39.52, 41.07, 46.50, 50.52,
              52.54, 58.91, 58.93, 66.71, 71.48, 71.84, 77.66, 79.31,
              80.90, 90.87, 91.22, 96.35, 108.92, 112.26 ,122.71 ,126.87,
              127.05, 137.96, 167.59, 183.53 , 282.49, 335.33, 341.19, 409.97])
```


```python
xbar = np.mean(x)
print(f"\nThe average lifetime is: {xbar : 0.1f} months\n")
```


<br>

It can be shown that this estimator has optimal propertis (i.e. it is a universal minimum variance unbiased estimator). 

But a point estimate itself does not provide information about accuracy. 

Our solution to this problem will be to derive an interval whose endpoints are random variables that
include the true value of $\theta$ between them with probability near 1, for example, $0.95$.

<br>
