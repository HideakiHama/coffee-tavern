steps = [
    [
        ## Create the table
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            hashed_password VARCHAR (255) NOT NULL,
            user_name VARCHAR(255) NOT NULL,
            role VARCHAR(10) NOT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE accounts;
        """,
    ],
    [
        ## Create the table
        ## Add profile_picture
        """
        CREATE TABLE employee_info (
            career_title VARCHAR(255),
            location VARCHAR(255),
            education VARCHAR(255),
            about TEXT,
            account_id INTEGER
        );
        """,
        ## Drop the table
        """
        DROP TABLE employee_info;
        """,
    ],
    [
        ## Create the table
        """
        CREATE TABLE employee_work_history (
            company VARCHAR(255),
            from_year SMALLINT,
            to_year SMALLINT,
            position VARCHAR(255),
            position_description TEXT,
            account_id INTEGER REFERENCES accounts(id)
        );
        """,
        ## Drop the table
        """
        DROP TABLE employee_work_history;
        """,
    ],
]
