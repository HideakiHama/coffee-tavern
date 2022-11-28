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
    [
        ## Junction table
        """
        CREATE TABLE employer_employee(
            employer_id INT REFERENCES employer_form(id),
            employee_id INT REFERENCES employee_form(id),
            PRIMARY KEY (employer_id, employee_id)
        );
        """,
        ## Drop the table
        """
        DROP TABLE employer_employee;
        """,
    ],
]
