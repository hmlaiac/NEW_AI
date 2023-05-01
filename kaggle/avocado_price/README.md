# Avocado Price
## Original Data & Challenge
- Resource: https://www.kaggle.com/datasets/neuromusic/avocado-prices
## Column Meanings
- Date - The date of the observation
- AveragePrice - the average price of a single avocado
- type - conventional or organic
- year - the year
- Region - the city or region of the observation
- Total Volume - Total number of avocados sold
- 4046 - Total number of avocados with PLU 4046 sold
- 4225 - Total number of avocados with PLU 4225 sold
- 4770 - Total number of avocados with PLU 4770 sold

## Inspiration // what we can do for this data set
1. In which cities can millenials have their avocado toast AND buy a home?
2. Was the Avocadopocalypse of 2017 real?

## Data Analysis
1. Use P-value
2. Use FFT to analyze pattern

## Modeling
### Part A. Model target
1. Find predicted price of avacado. If we can find the price of avacado, we can set a suitable price for avacado.
2. Find volume of avacado. If we can find the volume of avacado, we can decide how many acavade needed in our store.

### Part B. Solutions
1. Use current data to predict current data (easy)
- Find potential problems
2. Use current data to predict one lable in future (Medium)
- Functional, but expecting bad result
3. Use time series prediction to find some outsomes (Hard)
- Try

### Part C. Technical issues


## References
- [Kaggle Project link](https://www.kaggle.com/datasets/neuromusic/avocado-prices)
- [Explaination of p-value and t-test](https://chih-sheng-huang821.medium.com/%E7%B5%B1%E8%A8%88%E5%AD%B8-%E5%A4%A7%E5%AE%B6%E9%83%BD%E5%96%9C%E6%AD%A1%E5%95%8F%E7%9A%84%E7%B3%BB%E5%88%97-p%E5%80%BC%E6%98%AF%E4%BB%80%E9%BA%BC-2c03dbe8fddf)
- [Time series forecasting with tensorflow](https://www.tensorflow.org/tutorials/structured_data/time_series)

## Interesting Discussion
- [Meaning of Data](https://www.kaggle.com/datasets/neuromusic/avocado-prices/discussion/340388)
- [Predction with Random Forest](https://www.kaggle.com/code/muhammadanas0716/avocaodos-price-prediction-dealing-with-outliers)
