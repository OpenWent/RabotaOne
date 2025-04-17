import numpy as np
import matplotlib.pyplot as plt
data = np.random.uniform(26.4, 26.9, size=100)  
bins = np.linspace(26.4, 26.9, 6)  
hist, _ = np.histogram(data, bins=bins)  

plt.figure(figsize=(12, 5))
labels = ['26.4-26.5', '26.5-26.6', '26.6-26.7', '26.7-26.8', '26.8-26.9']
plt.subplot(1, 2, 1)
plt.bar(labels, hist, width=0.7, edgecolor='black')
plt.title('Гистограмма частот')
plt.xlabel('Интервалы курса')
plt.ylabel('n_i')

plt.subplot(1, 2, 2)
relative_freq = hist / np.sum(hist) 
plt.bar(labels, relative_freq, width=0.7, edgecolor='black')
plt.title('Гистограмма относительных частот')
plt.xlabel('Интервалы курса')
plt.ylabel('W_i')
plt.tight_layout()  
plt.show()
