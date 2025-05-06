# Usage
First install the package from the project root directory:
"pip install -e ."

Then call the model in the cli:
pii-bert "Some Text in double quotes"
pii-bert "My name is John Doe and my email is john@example.com"

# Experiment Setup
Trained on Nvidia P100 using the AI4/Privacy dataset (https://huggingface.co/datasets/ai4privacy/pii-masking-300k)
Max. Length 128
Epochs: (Up to) 100
Batch Size: 320
Learning Rate: 1e-04
MAX_GRAD_NORM = 10 (Gradient clipping)

| Epoch | Val. Loss | Token-Acc | Micro F1 | Macro F1 | Weighted F1 |
|------:|---------:|----------:|---------:|---------:|------------:|
| 10   | 0.1085 | 0.9742 | 0.76 | 0.70 | 0.76 |
| 20   | 0.1528 | 0.9710 | 0.77 | 0.72 | 0.77 |
| 30   | 0.1704 | 0.9763 | 0.77 | 0.72 | 0.77 |
| 40   | 0.1857 | 0.9663 | 0.77 | 0.72 | 0.77 |
| 50   | 0.1966 | 0.9691 | 0.77 | 0.72 | 0.77 |
| 60   | 0.2128 | 0.9708 | 0.78 | 0.73 | 0.78 |
| 70   | 0.2144 | 0.9782 | 0.78 | 0.73 | 0.78 |
| 80   | 0.2056 | 0.9758 | 0.77 | 0.72 | 0.77 |
| 90   | 0.2265 | 0.9766 | 0.77 | 0.73 | 0.78 |
| 100  | 0.2173 | 0.9771 | 0.78 | 0.73 | 0.78 |
