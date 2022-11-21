steps = [
    [
        ## Create the table
        """
        CREATE TABLE employer_form(
            id SERIAL PRIMARY KEY NOT NULL,
            employee_name varchar(1000) NOT NULL,
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
        """
        CREATE TABLE employee_form(
            id SERIAL PRIMARY KEY NOT NULL,
            employer_name varchar(1000) NOT NULL,
            description TEXT
        );
        """,
        ## Drop the table
        """
        DROP TABLE employee_form;
        """,
    ],
]
