from dash import Dash, html

app = Dash(__name__)
server = app.server  # <- ESSENCIAL para o Render

app.layout = html.Div([
    html.H1("Olá, mundo!")
])

if __name__ == "__main__":
    app.run_server(debug=True)
