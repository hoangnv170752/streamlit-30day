# streamlit-30day
A repo to practice using streamlit to visualize web application in Python 

### Day 1
- Set up the environment with Miniconda . Link: https://docs.conda.io/en/latest/miniconda.html

```bash
conda create -n stenv python=3.11
conda activate stenv
pip install streamlit
streamlit hello
```

### Day 2
- Run first streamlit application
```bash
streamlit run streamlit_app.py
```
### Day 3
Display the button widget with st.button

### Day 4
Work with Ken Jee: https://www.youtube.com/watch?v=Yk-unX4KnV4
### Day 5
st.write
st.write allows writing text and arguments to the Streamlit app.

In addition to being able to display text, the following can also be displayed via the st.write() command:

Prints strings; works like st.markdown()
Displays a Python dict
Displays pandas DataFrame can be displayed as a table
Plots/graphs/figures from matplotlib, plotly, altair, graphviz, bokeh

### Day 6
Upload source code to GitHub (already had this repo)
### Day 7
Deploying your Streamlit app with Streamlit Community Cloud
- Sign in Github

- Pick a repo, branch and file | click 

### Day 8
Using St.slider allows the display of a slider input widget

A simple app that shows the various ways on how to accept user input by adjusting the slider widget. Flow of the app:

User selects value by adjusting the slider widget

App prints out the selected value
```python
st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
```

### Day 9
st.line_chart displays a line chart.


A simple app for displaying line chart
Flow of the app:

Create a Pandas DataFrame from numbers randomly generated via NumPy.
Create and display the line chart via st.line_chart() command.

### Day 10
st.selectbox allows the display off a select widget 
a simple app that asks the user what their favorite color is

Flow of the app:

User selects a color.
App prints out the selected color.

### Day 11
st.multiselect displays a multiselect widget.

### Day 12
st.checkbox displays a checkbox widget
For the toggle switch
```python
pip install streamlit-toggle-switch

import  streamlit_toggle as tog
```

### Day 13
Spin up a cloud development environment
GitPod: 
To spin up a development environment on the cloud, we can use GitPod and this can be done simply by clicking on the following link:

Try it 👉 https://gitpod.io/#/https://github.com/dataprofessor/streamlit101/

### Day 14
Streamlit Components

```bash
pip install streamlit_pandas_profiling
```

### Day 15
st.latex display mathematical expressions formatted as LaTeX.

```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

### Day 16 
Customizing the theme of Streamlit apps .
Customizing the hex code inside the .streamlit/config.html file 

### Day 17 
st.secrets allows you to store confidential information such as API keys, db passwords or other credentials.

### Day 18
st.file_uploader displays a file uploader widget

By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option

### Day 19
Layout Streamlit app

st.set_page_config(layout="wide") - Displays the contents of the app in wide mode (otherwise by default, the contents are encapsulated in a fixed width box.)

st.sidebar - Places the widgets or text/image displays in the sidebar.

st.expander - Places text/image displays inside a collapsible container box.

st.columns - Creates a tabular space (or column) within which contents can be placed inside.