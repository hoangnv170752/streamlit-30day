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

- Pick a repo, branch and file | click Deploy