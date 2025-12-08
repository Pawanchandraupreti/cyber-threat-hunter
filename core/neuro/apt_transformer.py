from transformers import AutoModelForSequenceClassification
import torch

class APTDetector(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "microsoft/codebert-base",
            num_labels=5,
            problem_type="multi_label_classification"
        )
        self.technique_map = {
            0: "T1059.003",  # Command-Line
            1: "T1134",      # Token Impersonation
            2: "T1558",      # Golden Ticket
            3: "T1027",      # Obfuscation
            4: "T1204.002"   # User Execution
        }

    def detect(self, log_sequence):
        outputs = self.model(**log_sequence)
        return [self.technique_map[i] for i in torch.argmax(outputs.logits, dim=1)]
    
    