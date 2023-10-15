# import pandas as pd
# from datetime import datetime

# test = pd.Series([1, 2, 3, 4, 5])

# test.to_list()
# test.to_numpy()


# ora = datetime.now()
# natale = datetime.strptime("2023/12/25, 12:00:00", "%Y/%m/%d, %H:%M:%S")
# delta = natale - ora
# print(delta)

import matplotlib.pyplot as plt
import numpy as np

plt.bar([0.25,2.25,3.25,5.25,7.25],[300,400,200,600,700], label="Carpenter",color='b',width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[50,30,20,50,60], label="Plumber", color='g',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Wage')
plt.title('Details')

plt.savefig("output.png", format='png')

