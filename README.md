# DS API for Boys & Girls Club

## Visualizations API `/app/vis.py`
### Graphing Functions
- `get_pie_detail(df: pd.DataFrame, col: str) -> go.Figure`
    - Produces an aggregate pie chart of column value counts

### API Endpoints
- `/vis/pie/{club}/{activity}/{start}/{stop}`
  Produces a pie graph detailing the sentiment of a given activity for a given
  club over an inclusive date range.
    - `club` Club name
    - `activity` Activity name
    - `start` Start date "2021-07-27"
    - `stop` Stop date "2021-07-28"
- `/daily/` Produces a bar chart of average daily sentiment change over the last 24 hours.

## Data Base Operations `/app/db.py`
- `db_action(sql_action: str) -> None`
    - Performs an SQL action, returns None
- `db_query(sql_query: str) -> list`
    - Performs an SQL query and returns the result as a list
- `get_df() -> pd.DataFrame`
    - Gets the database as a pandas DataFrame
- `emoji_lookup(s: str) -> str`
    - Emoji lookup table. "1F603" -> "😃"
- `get_club_df_by_date_range(start, stop) -> pd.DataFrame`
    - `start` Date format: "2021-07-27"
    - `stop` Date format: "2021-07-27"
- `get_club_activity_df_by_date_range(club, activity, start, stop) -> pd.DataFrame`
    - `club` Club Name: "Anderson"
    - `activity` Activity Name: "Basketball"
    - `start` Date format: "2021-07-27"
    - `stop` Date format: "2021-07-27"
