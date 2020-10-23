import pandas as pd 
import os

csv_file = os.path.join("Resources", "mobility_cases_by_area.csv")
df = pd.read_csv(csv_file)
html = df.to_html() 
# write html to file 
text_file = open("data.html", "w") 
text_file.write(html) 
text_file.close() 