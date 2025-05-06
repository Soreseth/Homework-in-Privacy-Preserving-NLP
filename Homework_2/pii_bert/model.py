from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import json
import argparse
import os

class PIIModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-cased")
        self.model = AutoModelForTokenClassification.from_pretrained(os.path.dirname(os.path.abspath(__file__)) + "/model")
        self.ner_pipeline = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")
    
    def predict(self, text):
        return self.ner_pipeline(text)

    def mapping(self, entity):
        # Map the entity to a more readable format
        entity_mapping = {
            "LABEL_0": "B-BOD",
            "LABEL_1": "B-BUILDING",
            "LABEL_2": "B-CARDISSUER",
            "LABEL_3": "B-CITY",
            "LABEL_4": "B-COUNTRY",
            "LABEL_5": "B-DATE",
            "LABEL_6": "B-DRIVERLICENSE",
            "LABEL_7": "B-EMAIL",
            "LABEL_8": "B-GEOCOORD",
            "LABEL_9": "B-GIVENNAME1",
            "LABEL_10": "B-GIVENNAME2",
            "LABEL_11": "B-IDCARD",
            "LABEL_12": "B-IP",
            "LABEL_13": "B-LASTNAME1",
            "LABEL_14": "B-LASTNAME2",
            "LABEL_15": "B-LASTNAME3",
            "LABEL_16": "B-PASS",
            "LABEL_17": "B-PASSPORT",
            "LABEL_18": "B-POSTCODE",
            "LABEL_19": "B-SECADDRESS",
            "LABEL_20": "B-SEX",
            "LABEL_21": "B-SOCIALNUMBER",
            "LABEL_22": "B-STATE",
            "LABEL_23": "B-STREET",
            "LABEL_24": "B-TEL",
            "LABEL_25": "B-TIME",
            "LABEL_26": "B-TITLE",
            "LABEL_27": "B-USERNAME",
            "LABEL_28": "I-BOD",
            "LABEL_29": "I-BUILDING",
            "LABEL_30": "I-CARDISSUER",
            "LABEL_31": "I-CITY",
            "LABEL_32": "I-COUNTRY",
            "LABEL_33": "I-DATE",
            "LABEL_34": "I-DRIVERLICENSE",
            "LABEL_35": "I-EMAIL",
            "LABEL_36": "I-GEOCOORD",
            "LABEL_37": "I-GIVENNAME1",
            "LABEL_38": "I-GIVENNAME2",
            "LABEL_39": "I-IDCARD",
            "LABEL_40": "I-IP",
            "LABEL_41": "I-LASTNAME1",
            "LABEL_42": "I-LASTNAME2",
            "LABEL_43": "I-LASTNAME3",
            "LABEL_44": "I-PASS",
            "LABEL_45": "I-PASSPORT",
            "LABEL_46": "I-POSTCODE",
            "LABEL_47": "I-SECADDRESS",
            "LABEL_48": "I-SEX",
            "LABEL_49": "I-SOCIALNUMBER",
            "LABEL_50": "I-STATE",
            "LABEL_51": "I-STREET",
            "LABEL_52": "I-TEL",
            "LABEL_53": "I-TIME",
            "LABEL_54": "I-TITLE",
            "LABEL_55": "I-USERNAME",
            "LABEL_56": "O"
        }
        return entity_mapping.get(entity, entity)


def main():
    model = PIIModel()

    # parse text from command line. Text must be in double quotes
    # e.g. python model.py "My name is John Doe and my email is..."
    parser = argparse.ArgumentParser(description="Run PII NER model")
    parser.add_argument('text', metavar="text" ,type=str, help='Text to analyze')
    args = parser.parse_args()

    # predict PII entities
    for preds in model.predict(args.text):
        print(f"{preds['word']:<30} -> {model.mapping(preds['entity_group']):<25} | Confidence: {preds['score']:.2%}")


if __name__ == "__main__":
    main()
