steps = [
    [
        ## Employer table
        """
        CREATE TABLE employer_form(
            id SERIAL PRIMARY KEY NOT NULL,
            employee_name INT REFERENCES accounts(id),
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
            employer_name INT REFERENCES accounts(id),
            date DATE NOT NULL,
            description TEXT
        );
        """,
        """
        DROP TABLE employee_form;
        """,
    ],
]
