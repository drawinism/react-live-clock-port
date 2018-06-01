import react_live_clock_port
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions']=True

app.layout = html.Div([
    react_live_clock_port._component(
        ticking='true',
        format='HH:mm:ss',
    ),
    html.Div(id='output')
])

@app.callback(
	dash.dependencies.Output('output', 'children'),
	[dash.dependencies.Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
