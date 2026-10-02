class SpacyEngine:
    def __init__(self, model="en_core_web_sm"):
        self.nlp=None
        try:
            import spacy
            self.nlp=spacy.load(model)
        except Exception:
            pass

    def analyze(self,text):
        if not self.nlp:
            return []
        doc=self.nlp(text[:50000])
        return [{"text":e.text,"label":e.label_} for e in doc.ents]
