import logging
from flask import jsonify

from flask import Flask, request, Response

from words_count.report_task import TaskType
from words_count.words_count_service import WordsCountService


app = Flask(__name__)


@app.route('/report')
def report():
    report_type = request.args.get('type', '')
    content = request.args.get('content')

    try:
        report_type = TaskType[report_type.upper()]
    except KeyError:
        logging.getLogger(f'Exception occurred while trying to parse report type {report_type}')

    WordsCountService.get_instance().report(task_type=report_type, content=content)
    status_code = Response(status=200)
    return status_code


@app.route('/word_stats')
def word_stats():
    word = request.args.get('word')
    x = request.args

    if not word:
        logging.getLogger('no word arg passed')
        status_code = Response(status=400)
        return status_code

    count = WordsCountService.get_instance().get_word_count(word=word)
    word_count = {word: str(count)}
    return jsonify((word_count))
