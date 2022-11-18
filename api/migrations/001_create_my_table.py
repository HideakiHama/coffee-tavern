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
            description TEXT
        );
        """,
        ## Drop the table
        """
        DROP TABLE jobs;
        """,
    ],
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
]
