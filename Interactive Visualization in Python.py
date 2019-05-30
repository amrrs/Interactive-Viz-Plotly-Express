#!/usr/bin/env python
# coding: utf-8

# # Interactive Visualization in Python
# ### AbdulMajedRaja RS

# ### Outline
# 
# + Why Interactive Visualization?
# + Plotly Express - Intro
# + Basic Visualizations
# + Improving a Plot - One Component at a time
# + Building a Story - with one line of Code
# 

# ### Why Interactive Visualization?

# In[190]:


#import seaborn as sns
#import matplotlib.pyplot as plt
#crashes = sns.load_dataset("car_crashes")
#sns.set(rc={'figure.figsize':(11.7,8.27)})


# ### Static Visualization - Find the Values

# In[191]:


sns.barplot(x = 'speeding', y = 'abbrev', data = crashes);


# ### Interactive Visualization - Just, Hover over! 

# In[192]:


import plotly_express as px
px.bar(data_frame = crashes, x = 'speeding', y = 'abbrev', color = 'abbrev', orientation= "h")


# # Interactive over Static
# 
# + Intuitive - More Readable 
# + Less Code, More Stories/Insights
# + Customizable - Pan, Zoom, Select 
# + **This is 2019!!!**

# ### Plotly Express <img src="https://avatars3.githubusercontent.com/u/5997976?s=280&v=4" width="50"></img>

# ### Plotly Express
# 
# + High-level Python visualization library 
# + Wrapper around `plotly.py`
# + Plotly Express is totally free 
# + Right now, Only available for **Python**
# 
# 

# 
# + A simple syntax for complex charts
# + Inspired by `Seaborn` and `ggplot2` (R)
# + Consisten & Easy-to-learn API
# + Offline-mode by Default

# ### Installation

# In[193]:


# !! pip3 install plotly_express # Python3


# ### Loading

# In[194]:


import plotly_express as px


# ### Dataset

# In[195]:


gapminder = px.data.gapminder()

gapminder.tail(4)


# ### Simple Visualizations

# ### Bar

# In[196]:


px.bar(data_frame= gapminder[gapminder.year==2007], x = 'country', y = 'pop')


# ### Histogram

# In[197]:


px.histogram(data_frame= gapminder, x = 'pop')


# ### Box plot - Normal

# In[198]:


px.box(data_frame= gapminder, y = 'lifeExp')


# ### Box Plot - Colored / Grouped

# In[199]:


px.box(data_frame= gapminder, y = 'lifeExp', color = 'continent')


# ### Violin plot

# In[200]:


px.violin(data_frame= gapminder, y = 'lifeExp', color = 'continent', box=True)


# ### Line Graph

# In[201]:


px.line(gapminder.query("country == ['India','China','United States']"), 'year','pop', color = 'country')


# # Improving a Plot - One Component at a Time

# ### Scatter Plot

# In[202]:


px.scatter(data_frame= gapminder, x = 'gdpPercap', y = 'lifeExp')


# ### Scatter Plot with Box and Histogram

# In[203]:


px.scatter(data_frame= gapminder, x = 'gdpPercap', y = 'lifeExp', marginal_y='box', marginal_x='histogram')


# ### Scatter Plot with Trend Line

# In[204]:


px.scatter(data_frame= gapminder, x = 'gdpPercap', y = 'lifeExp', trendline='ols')


# ### Scatter Plot with Country Values (Hover)

# In[205]:


px.scatter(data_frame= gapminder, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', trendline= 'ols')


# ### Scatter Plot with Country Values (Hover) & Color - Transformed Axis

# In[206]:


px.scatter(data_frame= gapminder, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', color = 'country', log_x=True)


# # Building a Story for 2017
# ### With Just one Line of Code

# In[207]:


gapminder7 = gapminder[gapminder.year==2007]


# ### Scatter Plot 

# In[208]:


px.scatter(data_frame= gapminder7, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', 
           log_x=True)


# ### Scatter Plot - Transformed Axis & Facet - with Trendline

# In[209]:


px.scatter(data_frame= gapminder7, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', 
           log_x=True, facet_col="continent", trendline = 'ols')


# ### Bubble Chart 

# In[210]:


px.scatter(data_frame= gapminder7, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', 
           log_x=True, #facet_col="continent", 
           color = 'continent', size = 'pop')


# ### Bubble Chart with Facet by Continent

# In[211]:


px.scatter(data_frame= gapminder7, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', 
           log_x=True, facet_col="continent", 
           color = 'continent', size = 'pop')


# ### Scatter Plot with Country Values (Hover) & Color 

# In[212]:


px.scatter(data_frame= gapminder7, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', color = 'country')


# In[213]:


px.scatter(data_frame= gapminder7, x = 'gdpPercap', y = 'lifeExp', hover_name = 'country', color = 'country', 
           size = 'pop')


# ### The Big Picture - Timeline Animation

# In[214]:


px.scatter(px.data.gapminder(), x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="country", hover_name="country", 
           log_x = True, 
           size_max=45, range_x=[100,100000], range_y=[25,90])


# # Thank you
