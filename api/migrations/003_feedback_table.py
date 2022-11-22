steps = [
    [
        ## Create the table
        ## Employer table
        """
        CREATE TABLE employer_form(
            id SERIAL PRIMARY KEY NOT NULL,
            employee_name VARCHAR(1000) NOT NULL,
            date DATE NOT NULL,
            description TEXT
        );
        """,
        ## Drop the table
        """
        DROP TABLE employer_form;
        """,
    ],
    [
        ## Create the table
        ## Employee table
        """
        CREATE TABLE employee_form(
            id SERIAL PRIMARY KEY NOT NULL,
            employer_name VARCHAR(1000) NOT NULL,
            date DATE NOT NULL,
            description TEXT
        );
        """,
        ## Drop the table
        """
        DROP TABLE employee_form;
        """,
    ],
    [
        ## Junction table
        ## Create the table
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
