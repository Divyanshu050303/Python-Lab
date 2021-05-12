import pandas as pd
data={"calories": [420, 380, 390], "duration in min": [50, 40, 45]}
m=pd.DataFrame(data)
print(m.loc[0])