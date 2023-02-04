from app.database import get_db


def output_formatter(results): # it gonna convert those tuples of tupples to lists of dictionaries 
    out = []                   # creating an empty list  
    for result in results:     # for each result in results 
        formatted = {          # creating dictionary called formatted 
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "is_active": result[3]
        }
        out.append(formatted)  
    return out


def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE is_active=1", ()) #implying soft delete only showing active
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk): # pk = primary key  
    conn = get_db()
    cursor = conn.execute ("SELECT * FROM task WHERE id=?", (pk,)) 
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(raw_data):
    task_data = (
        raw_data.get("summary"), # extracting data from dictionary by calling get and specifying key 
        raw_data.get("descriptions") 
    )
    statement = """  
        INSERT INTO task (
            summary,
            description
        ) VALUES (?, ?)
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def update(raw_data,pk):
    task_data = (
        raw_data.get("summary"),
        raw_data.get("descriptions"),
        raw_data.get("is_active"),
        pk
    )
    statement = """
        UPDATE task
        SET summary=?,
            description=?,
            is_active=?
        WHERE id=?
    """
    conn = get_db()
    conn = conn.execute(statement, task_data)
    conn.commit()
    conn.close()

def delete(pk):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (pk))
    conn.commit()
    conn.closed()











