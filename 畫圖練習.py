import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
randomSequence = pd.DataFrame(np.random.normal(1.0, 0.08, (100,8)))
accunulate = randomSequence.cumprod()
accunulate.plot()
plt.title('behavior')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend(loc=0)
plt.show()