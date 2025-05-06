# Usage
First install the package from the project root directory:
"pip install -e ."

Then call the model in the cli:
pii-bert "Some Text in double quotes"
pii-bert "My name is John Doe and my email is john@example.com"

# Experiment Setup
Trained on Nvidia P100 using the AI4/Privacy dataset (https://huggingface.co/datasets/ai4privacy/pii-masking-300k)
Max. Length 128
Epochs: 20
Batch Size: 256
Learning Rate: 1e-04
