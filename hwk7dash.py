import dash
import os
import dash_leaflet as dl
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import os
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import dash
import seaborn as sns
from dash.dependencies import Input, Output
import random
import pandas as pd
import plotly.graph_objs as go
app = dash.Dash()

# Step 3. Create a plotly figure
import random
B0= random.randrange(1,10)
B1= random.randrange(1,10)
B0
x=np.linspace(-2,2,1000)
y=np.exp(B0 + B1*x)/(1 + np.exp(B0 + B1*x))

fig=px.scatter(x,y)


trace_1 = go.Scatter(x=x,y=y)
layout=go.Layout(title="Logistic regression", hovermode="closest")
fig= go.Figure(data=[trace_1],layout=layout)

# Step 4. Create a Dash layout
app.layout = html.Div([
          dcc.Graph(id = 'plot', figure = fig),
                html.P([
                    html.H1("B0"),
                    dcc.Slider(min = -1, max = 1, step = 0.1, value = 0.5, id='B0'),
                    html.H2("B1"),
                    dcc.Slider(min = -1, max = 1, step = 0.1, value = 0.5, id='B1') 
                        ])
                      ])


# Step 5. Add callback functions
@app.callback(Output('plot', 'figure'),
             Input('B0', 'value'),
             Input('B1', 'value')
)

def update_figure(B0, B1):
    #updating the plot
    x=np.linspace(-2,2,1000)
    y=np.exp(B0 + B1*x)/(1 + np.exp(B0 + B1*x))
    fig=px.scatter(x,y)
    return fig

# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug=False, host = 'jupyter.biostat.jhsph.edu', port=os.getuid()+23)

    