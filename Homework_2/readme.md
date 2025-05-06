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

############################## EPOCHS: 10 ##############################
Validation Loss: 0.1085
Token-level Accuracy: 0.9742
/opt/miniconda3/envs/llmcourse/lib/python3.9/site-packages/seqeval/metrics/v1.py:57: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
               precision    recall  f1-score   support

          BOD       0.81      0.81      0.81      2062
     BUILDING       0.86      0.83      0.85      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.76      0.79      0.77      1717
      COUNTRY       0.86      0.86      0.86      1285
         DATE       0.76      0.79      0.77      1415
DRIVERLICENSE       0.69      0.76      0.72      2110
        EMAIL       0.78      0.81      0.79      2234
     GEOCOORD       0.76      0.77      0.76       163
   GIVENNAME1       0.63      0.68      0.66      1662
   GIVENNAME2       0.50      0.51      0.51       434
       IDCARD       0.74      0.73      0.73      2404
           IP       0.77      0.79      0.78      1782
    LASTNAME1       0.55      0.61      0.58      2008
    LASTNAME2       0.34      0.46      0.39       505
    LASTNAME3       0.33      0.28      0.30       158
         PASS       0.70      0.71      0.70      1292
     PASSPORT       0.69      0.73      0.71      2083
     POSTCODE       0.79      0.78      0.78      1588
   SECADDRESS       0.77      0.77      0.77       719
          SEX       0.87      0.86      0.86      1652
 SOCIALNUMBER       0.79      0.77      0.78      2242
        STATE       0.86      0.82      0.84      1628
       STREET       0.77      0.80      0.79      1670
          TEL       0.75      0.77      0.76      1718
         TIME       0.80      0.81      0.80      2946
        TITLE       0.83      0.83      0.83      1694
     USERNAME       0.78      0.79      0.79      2459

    micro avg       0.75      0.77      0.76     43216
    macro avg       0.70      0.71      0.70     43216
 weighted avg       0.75      0.77      0.76     43216

############################## EPOCHS: 20 ##############################
Validation Loss: 0.1528
Token-level Accuracy: 0.9710
/opt/miniconda3/envs/llmcourse/lib/python3.9/site-packages/seqeval/metrics/v1.py:57: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
               precision    recall  f1-score   support

          BOD       0.80      0.82      0.81      2062
     BUILDING       0.85      0.85      0.85      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.77      0.80      0.78      1717
      COUNTRY       0.86      0.89      0.88      1285
         DATE       0.79      0.80      0.79      1415
DRIVERLICENSE       0.75      0.77      0.76      2110
        EMAIL       0.81      0.83      0.82      2234
     GEOCOORD       0.77      0.82      0.80       163
   GIVENNAME1       0.63      0.71      0.67      1662
   GIVENNAME2       0.48      0.57      0.52       434
       IDCARD       0.73      0.74      0.73      2404
           IP       0.79      0.80      0.80      1782
    LASTNAME1       0.56      0.62      0.59      2008
    LASTNAME2       0.43      0.46      0.44       505
    LASTNAME3       0.43      0.31      0.36       158
         PASS       0.68      0.72      0.70      1292
     PASSPORT       0.70      0.76      0.73      2083
     POSTCODE       0.79      0.80      0.80      1588
   SECADDRESS       0.78      0.79      0.78       719
          SEX       0.86      0.87      0.87      1652
 SOCIALNUMBER       0.76      0.80      0.78      2242
        STATE       0.83      0.83      0.83      1628
       STREET       0.78      0.81      0.79      1670
          TEL       0.77      0.79      0.78      1718
         TIME       0.79      0.81      0.80      2946
        TITLE       0.80      0.85      0.83      1694
     USERNAME       0.81      0.81      0.81      2459

    micro avg       0.76      0.78      0.77     43216
    macro avg       0.71      0.73      0.72     43216
 weighted avg       0.76      0.78      0.77     43216

############################## EPOCHS: 30 ##############################
Validation Loss: 0.1704
Token-level Accuracy: 0.9763
/opt/miniconda3/envs/llmcourse/lib/python3.9/site-packages/seqeval/metrics/v1.py:57: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
               precision    recall  f1-score   support

          BOD       0.79      0.81      0.80      2062
     BUILDING       0.87      0.86      0.86      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.76      0.82      0.79      1717
      COUNTRY       0.88      0.90      0.89      1285
         DATE       0.77      0.81      0.79      1415
DRIVERLICENSE       0.75      0.75      0.75      2110
        EMAIL       0.80      0.83      0.82      2234
     GEOCOORD       0.77      0.79      0.78       163
   GIVENNAME1       0.67      0.67      0.67      1662
   GIVENNAME2       0.52      0.53      0.53       434
       IDCARD       0.71      0.76      0.73      2404
           IP       0.79      0.82      0.80      1782
    LASTNAME1       0.56      0.64      0.60      2008
    LASTNAME2       0.39      0.54      0.46       505
    LASTNAME3       0.45      0.41      0.43       158
         PASS       0.69      0.73      0.71      1292
     PASSPORT       0.70      0.76      0.73      2083
     POSTCODE       0.80      0.80      0.80      1588
   SECADDRESS       0.78      0.79      0.79       719
          SEX       0.86      0.88      0.87      1652
 SOCIALNUMBER       0.77      0.77      0.77      2242
        STATE       0.85      0.84      0.85      1628
       STREET       0.80      0.82      0.81      1670
          TEL       0.74      0.80      0.77      1718
         TIME       0.79      0.83      0.81      2946
        TITLE       0.81      0.85      0.83      1694
     USERNAME       0.82      0.80      0.81      2459

    micro avg       0.76      0.79      0.77     43216
    macro avg       0.71      0.74      0.72     43216
 weighted avg       0.76      0.79      0.77     43216

############################## EPOCHS: 40 ##############################
Validation Loss: 0.1857
Token-level Accuracy: 0.9663
/opt/miniconda3/envs/llmcourse/lib/python3.9/site-packages/seqeval/metrics/v1.py:57: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
               precision    recall  f1-score   support

          BOD       0.79      0.80      0.80      2062
     BUILDING       0.85      0.87      0.86      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.77      0.80      0.79      1717
      COUNTRY       0.86      0.89      0.88      1285
         DATE       0.78      0.82      0.80      1415
DRIVERLICENSE       0.72      0.76      0.74      2110
        EMAIL       0.79      0.84      0.81      2234
     GEOCOORD       0.79      0.81      0.80       163
   GIVENNAME1       0.62      0.73      0.67      1662
   GIVENNAME2       0.48      0.65      0.55       434
       IDCARD       0.72      0.75      0.73      2404
           IP       0.78      0.81      0.79      1782
    LASTNAME1       0.56      0.62      0.59      2008
    LASTNAME2       0.39      0.49      0.44       505
    LASTNAME3       0.41      0.38      0.40       158
         PASS       0.67      0.72      0.69      1292
     PASSPORT       0.67      0.74      0.70      2083
     POSTCODE       0.77      0.80      0.79      1588
   SECADDRESS       0.80      0.81      0.80       719
          SEX       0.85      0.88      0.87      1652
 SOCIALNUMBER       0.78      0.78      0.78      2242
        STATE       0.83      0.84      0.83      1628
       STREET       0.79      0.81      0.80      1670
          TEL       0.76      0.80      0.78      1718
         TIME       0.79      0.83      0.81      2946
        TITLE       0.79      0.86      0.82      1694
     USERNAME       0.80      0.81      0.80      2459

    micro avg       0.75      0.79      0.77     43216
    macro avg       0.70      0.74      0.72     43216
 weighted avg       0.75      0.79      0.77     43216

############################## EPOCHS: 50 ##############################
Validation Loss: 0.1966
Token-level Accuracy: 0.9691
               precision    recall  f1-score   support

          BOD       0.80      0.81      0.81      2062
     BUILDING       0.85      0.87      0.86      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.78      0.81      0.79      1717
      COUNTRY       0.86      0.90      0.88      1285
         DATE       0.79      0.82      0.80      1415
DRIVERLICENSE       0.70      0.77      0.73      2110
        EMAIL       0.80      0.83      0.82      2234
     GEOCOORD       0.75      0.79      0.77       163
   GIVENNAME1       0.63      0.69      0.66      1662
   GIVENNAME2       0.52      0.59      0.56       434
       IDCARD       0.74      0.70      0.72      2404
           IP       0.79      0.81      0.80      1782
    LASTNAME1       0.57      0.66      0.61      2008
    LASTNAME2       0.42      0.54      0.47       505
    LASTNAME3       0.46      0.40      0.43       158
         PASS       0.68      0.74      0.71      1292
     PASSPORT       0.70      0.73      0.72      2083
     POSTCODE       0.78      0.81      0.79      1588
   SECADDRESS       0.81      0.82      0.81       719
          SEX       0.83      0.87      0.85      1652
 SOCIALNUMBER       0.73      0.81      0.77      2242
        STATE       0.85      0.85      0.85      1628
       STREET       0.79      0.83      0.81      1670
          TEL       0.78      0.78      0.78      1718
         TIME       0.80      0.83      0.82      2946
        TITLE       0.78      0.85      0.82      1694
     USERNAME       0.81      0.81      0.81      2459

    micro avg       0.75      0.79      0.77     43216
    macro avg       0.71      0.74      0.72     43216
 weighted avg       0.76      0.79      0.77     43216

############################## EPOCHS: 60 ##############################
Validation Loss: 0.2128
Token-level Accuracy: 0.9708
               precision    recall  f1-score   support

          BOD       0.80      0.80      0.80      2062
     BUILDING       0.87      0.85      0.86      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.76      0.81      0.79      1717
      COUNTRY       0.85      0.89      0.87      1285
         DATE       0.78      0.82      0.80      1415
DRIVERLICENSE       0.76      0.76      0.76      2110
        EMAIL       0.81      0.84      0.83      2234
     GEOCOORD       0.78      0.80      0.79       163
   GIVENNAME1       0.65      0.71      0.68      1662
   GIVENNAME2       0.54      0.57      0.56       434
       IDCARD       0.73      0.76      0.74      2404
           IP       0.78      0.81      0.80      1782
    LASTNAME1       0.58      0.65      0.61      2008
    LASTNAME2       0.42      0.52      0.47       505
    LASTNAME3       0.43      0.38      0.41       158
         PASS       0.69      0.73      0.71      1292
     PASSPORT       0.69      0.77      0.73      2083
     POSTCODE       0.78      0.81      0.79      1588
   SECADDRESS       0.78      0.81      0.79       719
          SEX       0.85      0.87      0.86      1652
 SOCIALNUMBER       0.76      0.79      0.78      2242
        STATE       0.84      0.84      0.84      1628
       STREET       0.79      0.82      0.81      1670
          TEL       0.76      0.79      0.78      1718
         TIME       0.80      0.83      0.82      2946
        TITLE       0.83      0.86      0.84      1694
     USERNAME       0.82      0.81      0.82      2459

    micro avg       0.76      0.79      0.78     43216
    macro avg       0.71      0.74      0.73     43216
 weighted avg       0.76      0.79      0.78     43216

############################## EPOCHS: 70 ##############################
Validation Loss: 0.2144
Token-level Accuracy: 0.9782
               precision    recall  f1-score   support

          BOD       0.79      0.81      0.80      2062
     BUILDING       0.85      0.85      0.85      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.77      0.80      0.79      1717
      COUNTRY       0.85      0.88      0.87      1285
         DATE       0.80      0.81      0.80      1415
DRIVERLICENSE       0.71      0.78      0.75      2110
        EMAIL       0.82      0.83      0.83      2234
     GEOCOORD       0.77      0.79      0.78       163
   GIVENNAME1       0.64      0.72      0.68      1662
   GIVENNAME2       0.50      0.59      0.54       434
       IDCARD       0.74      0.75      0.74      2404
           IP       0.79      0.81      0.80      1782
    LASTNAME1       0.59      0.64      0.61      2008
    LASTNAME2       0.45      0.52      0.48       505
    LASTNAME3       0.53      0.36      0.43       158
         PASS       0.67      0.73      0.70      1292
     PASSPORT       0.73      0.76      0.74      2083
     POSTCODE       0.77      0.81      0.79      1588
   SECADDRESS       0.79      0.80      0.80       719
          SEX       0.86      0.88      0.87      1652
 SOCIALNUMBER       0.78      0.79      0.79      2242
        STATE       0.85      0.84      0.85      1628
       STREET       0.80      0.82      0.81      1670
          TEL       0.78      0.80      0.79      1718
         TIME       0.80      0.83      0.81      2946
        TITLE       0.82      0.84      0.83      1694
     USERNAME       0.81      0.82      0.82      2459

    micro avg       0.76      0.79      0.78     43216
    macro avg       0.72      0.74      0.73     43216
 weighted avg       0.77      0.79      0.78     43216

############################## EPOCHS: 80 ##############################
Validation Loss: 0.2056
Token-level Accuracy: 0.9758
               precision    recall  f1-score   support

          BOD       0.80      0.81      0.80      2062
     BUILDING       0.85      0.85      0.85      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.77      0.79      0.78      1717
      COUNTRY       0.87      0.87      0.87      1285
         DATE       0.79      0.80      0.80      1415
DRIVERLICENSE       0.73      0.79      0.76      2110
        EMAIL       0.81      0.83      0.82      2234
     GEOCOORD       0.77      0.79      0.78       163
   GIVENNAME1       0.63      0.69      0.66      1662
   GIVENNAME2       0.49      0.61      0.54       434
       IDCARD       0.74      0.72      0.73      2404
           IP       0.79      0.82      0.80      1782
    LASTNAME1       0.58      0.66      0.62      2008
    LASTNAME2       0.47      0.51      0.49       505
    LASTNAME3       0.55      0.37      0.44       158
         PASS       0.67      0.71      0.69      1292
     PASSPORT       0.69      0.74      0.71      2083
     POSTCODE       0.77      0.80      0.79      1588
   SECADDRESS       0.80      0.80      0.80       719
          SEX       0.87      0.87      0.87      1652
 SOCIALNUMBER       0.79      0.81      0.80      2242
        STATE       0.84      0.83      0.83      1628
       STREET       0.78      0.81      0.80      1670
          TEL       0.76      0.78      0.77      1718
         TIME       0.80      0.83      0.81      2946
        TITLE       0.82      0.85      0.83      1694
     USERNAME       0.81      0.82      0.82      2459

    micro avg       0.76      0.79      0.77     43216
    macro avg       0.72      0.73      0.72     43216
 weighted avg       0.76      0.79      0.77     43216

############################## EPOCHS: 90 ##############################
Validation Loss: 0.2265
Token-level Accuracy: 0.9766
               precision    recall  f1-score   support

          BOD       0.80      0.81      0.81      2062
     BUILDING       0.85      0.85      0.85      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.75      0.79      0.77      1717
      COUNTRY       0.86      0.86      0.86      1285
         DATE       0.79      0.81      0.80      1415
DRIVERLICENSE       0.73      0.79      0.76      2110
        EMAIL       0.81      0.83      0.82      2234
     GEOCOORD       0.83      0.82      0.82       163
   GIVENNAME1       0.63      0.70      0.66      1662
   GIVENNAME2       0.52      0.59      0.55       434
       IDCARD       0.73      0.73      0.73      2404
           IP       0.80      0.82      0.81      1782
    LASTNAME1       0.60      0.62      0.61      2008
    LASTNAME2       0.44      0.55      0.49       505
    LASTNAME3       0.49      0.42      0.46       158
         PASS       0.67      0.72      0.69      1292
     PASSPORT       0.69      0.74      0.72      2083
     POSTCODE       0.78      0.80      0.79      1588
   SECADDRESS       0.78      0.79      0.79       719
          SEX       0.86      0.88      0.87      1652
 SOCIALNUMBER       0.79      0.79      0.79      2242
        STATE       0.85      0.83      0.84      1628
       STREET       0.79      0.81      0.80      1670
          TEL       0.76      0.79      0.78      1718
         TIME       0.81      0.83      0.82      2946
        TITLE       0.83      0.86      0.84      1694
     USERNAME       0.82      0.82      0.82      2459

    micro avg       0.76      0.79      0.77     43216
    macro avg       0.72      0.74      0.73     43216
 weighted avg       0.77      0.79      0.78     43216

############################## EPOCHS: 100 ##############################
Validation Loss: 0.2173
Token-level Accuracy: 0.9771
               precision    recall  f1-score   support

          BOD       0.81      0.81      0.81      2062
     BUILDING       0.86      0.86      0.86      1585
   CARDISSUER       0.00      0.00      0.00         1
         CITY       0.78      0.80      0.79      1717
      COUNTRY       0.86      0.88      0.87      1285
         DATE       0.81      0.82      0.81      1415
DRIVERLICENSE       0.73      0.76      0.75      2110
        EMAIL       0.82      0.83      0.82      2234
     GEOCOORD       0.75      0.81      0.78       163
   GIVENNAME1       0.67      0.62      0.64      1662
   GIVENNAME2       0.55      0.57      0.56       434
       IDCARD       0.74      0.75      0.74      2404
           IP       0.79      0.81      0.80      1782
    LASTNAME1       0.56      0.68      0.61      2008
    LASTNAME2       0.43      0.59      0.50       505
    LASTNAME3       0.44      0.45      0.44       158
         PASS       0.68      0.73      0.71      1292
     PASSPORT       0.71      0.76      0.74      2083
     POSTCODE       0.79      0.81      0.80      1588
   SECADDRESS       0.80      0.80      0.80       719
          SEX       0.85      0.87      0.86      1652
 SOCIALNUMBER       0.78      0.80      0.79      2242
        STATE       0.85      0.84      0.84      1628
       STREET       0.79      0.82      0.81      1670
          TEL       0.78      0.80      0.79      1718
         TIME       0.80      0.83      0.81      2946
        TITLE       0.82      0.87      0.84      1694
     USERNAME       0.81      0.82      0.82      2459

    micro avg       0.76      0.79      0.78     43216
    macro avg       0.72      0.74      0.73     43216
 weighted avg       0.77      0.79      0.78     43216
