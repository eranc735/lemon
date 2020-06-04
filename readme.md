Assumptions:

    1. Client always get an ok message
    2. Each file can be big but it contains many lines in reasonable size
    2. Each URL response can be big but it contains many lines in reasonable size
    3. Text input should feet memory
    3. Reporting rate should be reasonable to let system ingest the inputs(didn't include limit to tasks queue)
    4. URL endpoint should return 200 status code to be processed

Call examples:

Word counter endpoint:

    File: localhost:5000/report?type=file&content=/tmp/sample_file.txt
    URL: localhost:5000/report?type=text&content=http://www.slim.shadi/file.txt
    Text: localhost:5000/report?type=text&content=will the real slim shady please stand up

Word Stats:

    localhost:5000/word_stats?word=shady
    
Running the app:
from project dir:
    pip install -r requirements.txt
    export FLASK_APP=main.py
    cd src
    flask run