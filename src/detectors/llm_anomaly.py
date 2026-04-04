import transformers
from torch import nn

class LLMDetector(nn.Module):
    """Uses DistilBERT to detect novel attack patterns"""
    
    def __init__(self, model_name="distilbert-base-uncased"):
        super().__init__()
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
        self.model = transformers.AutoModelForSequenceClassification.from_pretrained(
            model_name, 
            num_labels=2
        )
        
    def forward(self, log_batch: list[str]):
        inputs = self.tokenizer(
            log_batch, 
            padding=True, 
            truncation=True, 
            return_tensors="pt"
        )
        return self.model(**inputs).logits
    
    

    