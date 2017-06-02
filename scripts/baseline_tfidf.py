
import numpy as np
import random
import json

from sklearn.feature_extraction.text import TfidfVectorizer


def do_parse_cmdline():

    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("--input-task-file", dest="inputtaskfile",
                      default="dialog-task5full-dialogs-hard-SK_wifi_atmosphere_restrictions-trn1000.json",
                      help="filename of the task", metavar="FILE")

    parser.add_option("--output_result-file", dest="outputresultfile",
                      default="output-result-tfidf.json",
                      help="output file results", metavar="FILE")

    (options, args) = parser.parse_args()

    return options.inputtaskfile, options.outputresultfile


def do_load_storie_tfidf(json_data):

    lst_docs = []
    vect = TfidfVectorizer()

    for story in json_data:
        lst_docs.append(" ".join(story['utterances']))

    lst_docs = vect.fit_transform(lst_docs)

    return vect, lst_docs


### The current dialog format
### [{dialog_id : " ", lst_candidate_id: [{candidate_id: " ", rank: " "}, ...]}]

if __name__ == '__main__':

    # Parsing command line
    inputtaskfile, outputresultfile = do_parse_cmdline()

    fd = open(inputtaskfile, 'rb')
    json_data = json.load(fd)
    fd.close()

    vect, lst_docs = do_load_storie_tfidf(json_data)

    lst_responses = []

    for idx_story, story in enumerate(json_data):
        dict_answer_current = {}
        dict_answer_current['dialog_id'] = story['dialog_id']

        lst_candidate_id   = []
        lst_candidate_utterance = []
        for cand in story['candidates']:
            lst_candidate_id.append(cand['candidate_id'])
            lst_candidate_utterance.append(cand['utterance'])
        lst_candidate_utterance = vect.transform(lst_candidate_utterance)

        idx_rank = np.asarray(np.argsort(-np.dot(lst_docs[idx_story],
                                      np.transpose(lst_candidate_utterance)).todense().ravel()))[0]
        lst_candidate_rank = []
        for it in range (0, len(lst_candidate_id)):
            lst_candidate_rank.append({"candidate_id": lst_candidate_id[idx_rank[it]], "rank": it+1})

        dict_answer_current['lst_candidate_id'] = lst_candidate_rank
        lst_responses.append(dict_answer_current)

    fd = open(outputresultfile, 'wb')
    json.dump(lst_responses, fd)
    fd.close()