import psycopg2
import pandas as pd
import asyncio
import time
import timeit

class Banco:
    def connect(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="root", host="127.0.0.1", database="transactions")
            self.connection.autocommit = False
            self.cursor = self.connection.cursor()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Deu caca\n")
            print(error)

    async def runTransaction(self):
        inicio = timeit.default_timer()
        await asyncio.gather(self.executeExplicit())
        fim = timeit.default_timer()
        print ('duracao explicita = : %f' % (fim - inicio))
        inicio = timeit.default_timer()
        await asyncio.gather(self.executeImplicit())
        fim = timeit.default_timer()
        print ('duracao implicita = : %f' % (fim - inicio))

    async def executeExplicit(self):
        print('hello')

    async def executeImplicit(self):
        print('hello 1')

    async def showRows(self):
        pass

bd = Banco()
bd.connect()
asyncio.run(bd.runTransaction())