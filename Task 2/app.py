import psycopg2

def main():
    try:
        conn = psycopg2.connect(
            dbname="testdb",
            user="testuser",
            password="testpass",
            host="db",  # Имя сервиса PostgreSQL в docker-compose.yml
            port="5432"
        )
        cursor = conn.cursor()
        
		cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT,
                department VARCHAR(50)
            );
        """)
        conn.commit()

        cursor.execute("""
            INSERT INTO employees (name, age, department)
            VALUES
                ('Alice', 30, 'HR'),
                ('Bob', 25, 'Engineering'),
                ('Charlie', 35, 'Sales')
            ON CONFLICT DO NOTHING;
        """)
        conn.commit()

        cursor.execute("SELECT * FROM employees;")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
