
 data=df1
 high_low = data['High'] - data['Low']
 high_close = np.abs(data['High'] - data['Close'].shift())
 low_close = np.abs(data['Low'] - data['Close'].shift())
 ranges = pd.concat([high_low, high_close, low_close], axis=1)
 true_range = np.max(ranges, axis=1)

 atr = true_range.rolling(2).sum()/2


 