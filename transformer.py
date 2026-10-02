class TransformerEngine:
    def __init__(self, model_name, enabled=True):
        self.pipe=None
        if not enabled:
            return
        try:
            from transformers import pipeline
            self.pipe=pipeline("text-classification",model=model_name)
        except Exception:
            pass

    def classify(self,text):
        if not self.pipe:
            return {"available":False,"result":[]}
        try:
            return {"available":True,"result":self.pipe(text[:4000],truncation=True)}
        except Exception as e:
            return {"available":False,"result":[],"error":str(e)}
