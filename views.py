from flask import Flask, render_template
import plotly
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
import json

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('../Oil_pipeline/database.csv')
    causes = df['Cause Category'].value_counts()
    causes = go.Bar(
    y = causes.values, 
    x = causes.index.values, 
    name = 'Causes Category Count', 
        marker=dict(
            color=causes.values,
            colorscale = 'Viridis',
            reversescale = True
            )
    )

    data = [causes]

    layout = go.Layout (
    title = 'Cause category', 
    width = 700, 
    margin=go.Margin(b=140, r=150)
    )

    fig1 = go.Figure(data=data, layout=layout)
    py.iplot(fig1, filename='basic-bar')
    graph1 = json.dumps(fig1,cls=plotly.utils.PlotlyJOSONEncorder)
    return render_template('index.html',graph1=graph1)


if __name__ == '__main__':
    app.run(debug=True)