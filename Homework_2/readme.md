# Usage
First install the package from the project root directory: <br/>
"pip install -e ." <br/>
 
Then call the model in the cli: <br/>
pii-bert "Some Text in double quotes" <br/>
pii-bert "My name is John Doe and my email is john@example.com" <br/>

# Experiment Setup
Model: Distilbert Base Cased (https://huggingface.co/distilbert/distilbert-base-cased) <br/>
Dataset: AI4/Privacy dataset, only the english sentences (https://huggingface.co/datasets/ai4privacy/pii-masking-300k) <br/>
GPU: Nvidia P100 <br/>
Max. Length: 128 <br/>
Epochs: 100 <br/>
Batch Size: 320 <br/>
Learning Rate: 1e-04 <br/>
MAX_GRAD_NORM = 10 (Gradient clipping) <br/>

# Evaluation
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

# Model 
You can download the model here for local usage: <br/>
https://ruhr-uni-bochum.sciebo.de/s/KPgvSHLyItgD6ZT
