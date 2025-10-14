class llms:

    def __init__(self,query):
        self.query = query

    def openai(self):
        print(f'Hey I am open ai. your query. {self.query}')

    def claude(self):
        print(f'Hey I am claude. your query. {self.query}')

    def llama(self):
        print(f'Hey I am llama. your query. {self.query}')


if __name__ == "__main__":

    obj = llms('Hey I am Ravi')
    obj.openai()
