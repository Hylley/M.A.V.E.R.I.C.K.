from random import choice
from .utils import *
import sqlite3

class AI():
    def __init__(self, name, special_char):
        self.name = name
        self.special_char = special_char

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
    
    def talk(self, input):
        if self.special_char in input: return False
        if not self.connection: self.open_session()

        match = {
            'id': 1,
            'text': '',
            'similarity': 0
        }

        for row in self.cursor.execute('SELECT * FROM sentences').fetchall():
            aprox = similarity_cosine(input, row[1])
            
            if aprox > match['similarity']:
                match['id'] = row[0]
                match['text'] = row[1]
                match['similarity'] = aprox
        
        possible_responses = self.cursor.execute('SELECT response FROM pairs WHERE sentence = ?', (str(match['id']))).fetchall()
        choosen_response = choice(possible_responses)

        return self.cursor.execute('SELECT text FROM sentences WHERE id = ?', (str(choosen_response[0]))) + f' [{match["similarity"]}]'
    
    def update(self, input_text, match, response):
        pass
