# DS API for Boys & Girls Club

## Visualizations API `/app/vis.py`
### Graphing Functions
- `get_bar(df: pd.DataFrame, col_1: str, col_2: str) -> go.Figure`
    - Produces a cross tabs bar chart of two columns
    - Y-axis: col_1
    - X-axis: col_2
- `get_pie(df: pd.DataFrame, col: str) -> go.Figure`
    - Produces an aggregate pie chart of column value counts 

### API Endpoints
- `/vis/pie/{col}` Get Pie Chart
    - `col` param options: [club, activity, sentiment]
- `/vis/bar/{col1}/{col2}` Get Bar Chart
    - `col1` & `col2` param options: [club, activity, sentiment]

## Data Base Operations `/app/db.py`
- `db_action(sql_action: str) -> None`
    - Performs an SQL action, returns None
- `db_query(sql_query: str) -> list`
    - Performs an SQL query and returns the result as a list
- `get_df() -> pd.DataFrame`
    - Gets the entire database as a pandas DataFrame

## Developers
- Robert Sharp
