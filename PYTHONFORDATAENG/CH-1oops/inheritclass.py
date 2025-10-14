from firstclass import llms

class chatbot(llms):

    def __init__(self,model,query):
        self.model = model
        llms.__init__(self,query)

    def showme(self):
        print(f'I am calling -> {self.model}')
        self.openai()

obj_inherit = chatbot('openai','say about my self..')
obj_inherit.openai() # this method i called from perent class
obj_inherit.showme() # this i call from current class method and that method calling one method from perent class

