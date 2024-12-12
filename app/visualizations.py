import plotly.express as px

def create_bar_chart(dataframe, x_col, y_col, title):
    return px.bar(dataframe, x=x_col, y=y_col, title=title)

def create_line_chart(data, title="Line Chart"):
    return px.line(data, title=title)
