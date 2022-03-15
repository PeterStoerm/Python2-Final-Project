#!/usr/bin/env python
# coding: utf-8

# # Final Project

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style


# In[2]:


#Importing the data and readingng it
data = pd.read_csv("covid_country_stats.csv")
data


# ### Statistical Summary

# In[3]:


# Sum of Deaths
data=data.astype({"Deaths":float})
data_deaths = data["Deaths"].sum()
print("The total number of recorded deaths by Covid is", data_deaths)


# In[4]:


# Average number of active cases
data = data.astype({"Active":float})
data_active = data["Active"].mean()
data_active = round(data_active, 2)
print("The average number of active cases in the overal period from January 2020 to July 2020 is", data_active)


# ### Relationships

# In[5]:


# Average number of deaths by country in Europe
data_europe_deaths = (data[data["WHO Region"] == "Europe"].groupby(["Country/Region"])["Deaths"].mean()/ 0.617021) * 100
print("This is the percentages of the average death from covid compared to the lowest values which is Liechtenstein")
print()
print(data_europe_deaths)


# In[6]:


#Top 10 confirmed cases Americas vs Africa
data_confrimed_americas = data[data["WHO Region"] == "Americas"].groupby(["Country/Region"])["New cases"].sum()
data_confrimed_asia = data[data["WHO Region"] == "Africa"].groupby(["Country/Region"])["New cases"].sum()
print(data_confrimed_asia.sort_values().tail(10), data_confrimed_americas.sort_values().tail(10))


# In[7]:



data_americas_confirmed = data[data["WHO Region"] == "Americas"].groupby(["Country/Region"])["Confirmed"].sum()
print(data_americas_confirmed)


# ### Visualizations

# In[8]:


# 1st visualization 

# Isolate the sum of death numbers by European Region
data_europe_deaths = data[data["WHO Region"] == "Europe"].groupby(["Country/Region"])["Deaths"].sum() 
# I ploted the tail(5) of the sorted values because the .sort_values function starts from low and ends high 
x = plt.pie(data_europe_deaths.sort_values().tail(5), labels = data_europe_deaths.sort_values().tail(5).index,autopct="%.2f %%", pctdistance=0.5)
fig = plt.gcf()
fig.set_size_inches(10,10) # Here I configured the plot to be bigger and read more easily
plt.title("Top Five European Countries by Death Percentage")
plt.style.use('ggplot')
plt.show()


# In[9]:


# 2nd Visualization

# Getting the confirmed cases and dates in its own section to islate
us = data[data["Country/Region"] == "US"].groupby(["Date"])["Confirmed"].sum()
uk = data[data["Country/Region"] == "United Kingdom"].groupby(["Date"])["Confirmed"].sum() 
ind = ger = data[data["Country/Region"] == "India"].groupby(["Date"])["Confirmed"].sum() 

# Plotting the 3 countries by the new datafram
plot1, = plt.plot(us.index, us.values)
plot2, = plt.plot(uk.index, uk.values)
plot3, = plt.plot(ind.index, ind.values)

# Formatting the graph properly
plt.xticks(np.linspace(0,187,8)[:-1], ('Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul")) # I broke down the x-axis to months instead of days
plt.legend(handles=[plot1, plot2, plot3],labels=["US", "UK", "India"])
plt.xlabel("Month (2020)")
plt.ylabel("Confirmed Cases (Millions)")
plt.title("Total Confirmed Cases in US, UK and India")
plt.style.use('ggplot')
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.show()


# ### Conclusion

# For the final project I decided to choose the covid 19 data set because I felt that it had the most real world applications due to the ongoing debate in the media about the “science and statistics” that govern the politics regarding the pandemic. The summary statistics that I chose to explore were the total number of deaths and the average number of active cases per country. The relationships that I chose for the exploratory section of the assignment was the association between the average number of deaths by country in Europe and the total number of confirmed cases by countries in Americas. I decided to break the relationships down via the $.groupby()$ function by WHO Region because I think it was the best way to show the relationship between the countries and the metrics that I chose to explore. Furthermore I chose to plot both the top five countries by death percentage in Europe by sorting the values of this group and taking the top five by using the $.tail(5)$ function. For the second visualization I chose to create a line graph of three countries having the dates sectioned by month on the x-axis and the total number of confirmed cases in millions. I believe that this is the best representation to show the evolution of the confirmed cases by country because it can be applied to show the change in cases by the month which could be used in different modeling applications. Overall, I think my analysis of the data set gives a comprehensive picture of the key points of the data and is easy to understand and follow when trying to visualize the information.
