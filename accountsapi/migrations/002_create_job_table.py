steps = [
    [
        # Create the table
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
            applied_id INT REFERENCES accounts(id),
            account_id INT REFERENCES accounts(id)
        );
        """,
        # Drop the table
        """
        DROP TABLE jobs;
        """,
    ],
    [
        # Create the table
        """
        CREATE TABLE applied (
            id SERIAL PRIMARY KEY NOT NULL,
            account_id INT REFERENCES accounts(id),
            employer_id INT,
            full_name VARCHAR(255),
            education VARCHAR(255)
        );
        """,
        # Drop the table
        """
        DROP TABLE applied;
        """,
    ]
]
