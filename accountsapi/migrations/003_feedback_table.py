steps = [
    [
        ## Employer table
        """
        CREATE TABLE employer_form(
            id SERIAL PRIMARY KEY NOT NULL,
            account_id INT REFERENCES accounts(id),
            employee_name VARCHAR(255),
            date DATE NOT NULL,
            description TEXT
        );
        """,
        """
        DROP TABLE employer_form;
        """,
    ],
    [
        ## Employee table
        """
        CREATE TABLE employee_form(
            id SERIAL PRIMARY KEY NOT NULL,
            account_id INT REFERENCES accounts(id),
            employer_name VARCHAR(255),
            date DATE NOT NULL,
            description TEXT
        );
        """,
        """
        DROP TABLE employee_form;
        """,
    ]
]
