<<<<<<<< HEAD:api/migrations/002_create_job_table.py
steps = [
    [
        ## Create the table
        """
        CREATE TABLE jobs (
            id SERIAL PRIMARY KEY NOT NULL,
            employer varchar(1000) NOT NULL,
            position varchar(1000) NOT NULL,
            location varchar(1000) NOT NULL,
            from_date DATE NOT NULL,
            to_date DATE NOT NULL,
            tag varchar(1000) NOT NULL,
            description TEXT NOT NULL,
            account_id INT REFERENCES accounts(id)
        );
        """,
        ## Drop the table
        """
        DROP TABLE jobs;
        """,
    ],
]
========
steps = [
    [
        ## Create the table
        """
        CREATE TABLE jobs (
            id SERIAL PRIMARY KEY NOT NULL,
            employer varchar(1000) NOT NULL,
            position varchar(1000) NOT NULL,
            location varchar(1000) NOT NULL,
            from_date DATE NOT NULL,
            to_date DATE NOT NULL,
            tag varchar(1000) NOT NULL,
            description TEXT NOT NULL,
            account_id INT REFERENCES accounts(id)
        );
        """,
        ## Drop the table
        """
        DROP TABLE jobs;
        """,
    ],
]
>>>>>>>> main:api/migrations/002_create_my_table.py
