# Here we are using sqlite you may change your db_utils according to your database

from sqlalchemy import create_engine
from sqlalchemy import text

# This is the database connection string

def dataframe_to_datebase(df , table_name):
    """ Convert datafram to database table
    Arg: df and tablename
    Returns: sql alchmey engine
    """

    engine = create_engine('sqlite:///:memory:',echo=True) # creating a temporary database in our memory
    df.to_sql(name='Sales',con=engine) # converting our pandas df to sql with connection to temp_db with name sales
    return engine

def handle_response(response):
    """ This function handles the response from openai
        Arg: response from openai
        Returns: query
    """
    query = response['choices'][0]['text']
    if query.startswith(" "):
        query = "SELECT" + query
    return query

def excecute_query(engine,query):
    """
    This function excecutes the query and returns the result
        Arg: engine and query
        Returns: result
    """
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()