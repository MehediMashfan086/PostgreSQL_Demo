import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'Pass@123'
port_id = 5432

conn = None

try:
    with psycopg2.connect(host=hostname, 
                            dbname=database, 
                            user=username, 
                            password=pwd, 
                            port=port_id) as conn:
    
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
            cur.execute("DROP TABLE IF EXISTS employee")
            
            create_script = """
            CREATE TABLE IF NOT EXISTS employee (
                id int PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                salary int,
                dept_id varchar(30)) """
                
            cur.execute(create_script)
            
            insert_script = " INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)"
            insert_values = [(1, 'Mehedi', 50000, 'SE'),
                            (2, 'Al-amin', 45000, 'SQA'),
                            (3, 'Sajib', 40000, 'IT'),
                            (4, 'Abir', 30000, 'HR')]
            
            for record in insert_values:
                cur.execute(insert_script, record)
                
            # update_script = "UPDATE employee SET salary = salary + (salary * 0.5)"
            # cur.execute(update_script)
            
            # delete_script = "DELETE FROM employee WHERE id = %s"
            # delete_record = (4,)
            # cur.execute(delete_script, delete_record)
                
            cur.execute("SELECT * FROM employee")
            for record in cur.fetchall():
                print(record['name'], record['salary'], record['dept_id'])
            
            print('Table created successfully')
            
            
except Exception as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()