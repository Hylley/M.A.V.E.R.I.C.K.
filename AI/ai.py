from random import choice
from .utils import *
import sqlite3

ACCEPTABLE_RESEMBLANCE = 0.8

class AI():
    def __init__(self, name, special_char, commit_changes = True):
        self.name = name
        self.special_char = special_char
        self.commit_changes = commit_changes

        self.connection = None
        self.cursor = None

        self.open_session()
    
    def open_session(self):
        if self.connection:
            return

        self.connection = sqlite3.connect('AI\database.db')
        self.cursor = self.connection.cursor()
    
    def close_session(self):
        self.cursor.close()
        self.connection.close()

        self.cursor = None
        self.connection = None
    
    def find(self, input):
        match = {
            'id': 1,
            'text': '',
            'similarity': 0
        }

        for row in self.cursor.execute('SELECT * FROM sentences').fetchall():
            aprox = similarity_cosine(input, row[1])

            if aprox == 110: return 110
            
            if aprox > match['similarity']:
                match['id'] = row[0]
                match['text'] = row[1]
                match['similarity'] = aprox
        
        return match

    def talk(self, input, response_statement):
        if self.special_char in input: return False
        if not self.connection: self.open_session()

        match = self.find(input)

        if match == 110: return match
        possible_responses = self.cursor.execute('SELECT response FROM pairs WHERE sentence = ?', (str(match['id']))).fetchall() or self.cursor.execute('SELECT response FROM pairs ORDER BY RANDOM() LIMIT 1').fetchall()
        choosen_response = choice(possible_responses)

        updated = self.update(
            response_statement,
            input
        )

        return self.cursor.execute('SELECT text FROM sentences WHERE id = ?', (str(choosen_response[0]))).fetchone()[0]# + f' [{match["similarity"]}] [{updated}]'
    
    def update(self, response_statement, input):
        if not self.commit_changes: return
        if not self.connection: self.open_session()
        if not response_statement: return

        updated = False
        sentence = self.find(response_statement)

        if sentence['similarity'] < ACCEPTABLE_RESEMBLANCE: return

        similar_input = self.find(input)
        if similar_input['similarity'] < ACCEPTABLE_RESEMBLANCE:
            input_id = self.cursor.execute('INSERT INTO sentences(text) VALUES(?) RETURNING id', (input,)).fetchone()[0]
        else:
            input_id = similar_input['id']

        if not self.cursor.execute('SELECT * FROM pairs WHERE sentence = ? AND response = ?', (sentence['id'], input_id)).fetchall():
            self.cursor.execute('INSERT INTO pairs VALUES(?, ?)', (sentence['id'], input_id))
            updated = True

        self.connection.commit()

        return updated