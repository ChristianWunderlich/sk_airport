import sqlite3
import random
import os


class Database:
    def __init__(self):
        self.create_table ="CREATE TABLE IF NOT EXISTS airports (id INTEGER PRIMARY KEY, code text NOT NULL,name text NOT NULL, city text NOT NULL, country text NOT NULL, frequency double);"
        self.insert_statement = [
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EGLL', 'Heathrow', 'London', 'United Kingdom', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EGKK', 'Gatwick', 'London', 'United Kingdom', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDF', 'Frankfurt Airport', 'Frankfurt', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDM', 'Munich Airport', 'Munich', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDB', 'Berlin Brandenburg Airport', 'Berlin', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDL', 'Düsseldorf Airport', 'Düsseldorf', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDH', 'Hamburg Airport', 'Hamburg', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDS', 'Stuttgart Airport', 'Stuttgart', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDK', 'Cologne Bonn Airport', 'Cologne', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDV', 'Hanover Airport', 'Hanover', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDN', 'Nuremberg Airport', 'Nuremberg', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDP', 'Leipzig/Halle Airport', 'Leipzig', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDW', 'Bremen Airport', 'Bremen', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDC', 'Dresden Airport', 'Dresden', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDFH', 'Frankfurt-Hahn Airport', 'Frankfurt', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDSB', 'Karlsruhe/Baden-Baden Airport', 'Karlsruhe', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDG', 'Münster Osnabrück International Airport', 'Münster', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDLV', 'Weeze Airport', 'Weeze', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDJA', 'Memmingen Airport', 'Memmingen', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDR', 'Saarbrücken Airport', 'Saarbrücken', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDNY', 'Friedrichshafen Airport', 'Friedrichshafen', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDE', 'Erfurt-Weimar Airport', 'Erfurt', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDT', 'Berlin Tegel Airport', 'Berlin', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDDB', 'Berlin Schönefeld Airport', 'Berlin', 'Germany', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('LOWW', 'Vienna International Airport', 'Vienna', 'Austria', {random.uniform(100.0, 150.0):.3f});",
            f"INSERT INTO airports (code, name, city, country, frequency) VALUES ('EDMO', 'Oberpfaffenhofen Airport', 'Oberpfaffenhofen', 'Germany', {random.uniform(100.0, 150.0):.3f});"
        ]
    def create_database_add_example_data(self):
        try:
            os.remove("example.db")
            with sqlite3.connect('example.db') as conn:
                print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
                cursor = conn.cursor()
                cursor.execute(self.create_table)
                for statement in self.insert_statement:
                    cursor.execute(statement)
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)

    def get_airports(self):
        with sqlite3.connect("example.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM airports")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]