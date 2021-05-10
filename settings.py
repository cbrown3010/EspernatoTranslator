class config:
    def __init__(self):
        self.inputLang = "en-US"
        self.outputLang = "ko-KR"
        self.translation = "kr"
        self.gender = "male"
        self.inputText = "blank"
        self.outputText = "blank"

    def get_input_lang(self):
        return self.inputLang

    def get_output_lang(self):
        return self.outputLang

    def get_translation(self):
        return self.translation

    def get_gender(self):
        return self.gender

    def get_input_text(self):
        return self.inputText

    def get_output_text(self):
        return self.outputText

    def set_input_lang(self, input_lang):
        self.inputLang = input_lang

    def set_output_lang(self, output_lang):
        self.outputLang = output_lang

    def set_translation(self, translation):
        self.inputLang = translation

    def set_gender(self, gender):
        self.gender = gender

    def set_input_text(self, inputText):
        self.inputText = inputText

    def set_output_text(self, outputText):
        self.outputText = outputText


