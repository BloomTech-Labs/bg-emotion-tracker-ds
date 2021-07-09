# DS API for Boys & Girls Club

## Visualizations API
### Graphing Functions
- get_bar(df, col_1, col_2)
    - Produces a cross tabs bar chart of the two columns
    - Y-axis: col_1
    - X-axis: col_2
- get_pie(df, col)
    - Produces an aggregate pie chart of the column value counts 

### API Endpoints
- `/vis/pie/{col}` Get Pie Chart
    - `col` param options: [club, activity, sentiment]
- `/vis/bar/{col1}/{col2}` Get Bar Chart
    - `col1` & `col2` param options: [club, activity, sentiment]

## Data Base Operations
- `db_action(sql_action: str) -> None`
    - Performs an SQL action, returns None
- `db_query(sql_query: str) -> list`
    - Performs an SQL query and returns the result as a list
- `get_df() -> pd.DataFrame`
    - Gets the entire database as a pandas DataFrame

### Developers
- Robert Sharp
