
import numpy as np
import json

from sklearn.feature_extraction.text import CountVectorizer


def do_statistics(lst_dialogs):

    dict_stats = {}

    lst_utterances = []
    lst_nb_utterances = []
    for dialog in lst_dialogs:
        for utterance in dialog['utterances']:
            lst_utterances.append(utterance)
        lst_nb_utterances.append(len(dialog['utterances'])*1.0)

    dict_stats['nb_dialog'] = len(lst_dialogs)
    dict_stats['nb_utterance_total'] = len(lst_utterances)
    dict_stats['nb_utterance_unic'] = len(list(set(lst_utterances)))
    dict_stats['nb_utterance_per_dialog'] = np.mean(lst_nb_utterances)

    cnt = CountVectorizer()
    cnt.fit(lst_utterances)
    dict_stats['voc_total_len'] = len(cnt.get_feature_names())
    dict_stats['voc_total'] = cnt.get_feature_names()

    cnt = CountVectorizer(stop_words="english")
    cnt.fit(lst_utterances)
    dict_stats['voc_non_stop_len'] = len(cnt.get_feature_names())
    dict_stats['voc_non_stop'] = cnt.get_feature_names()

    return dict_stats


def do_parse_cmdline():

    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("--input-task-file", dest="inputtaskfile",
                      default="dataset-challenge/dialog-task3OPTIONS-kb1_atmosphere-distr0.9-trn10000.json",
                      help="filename of the task", metavar="FILE")

    parser.add_option("--output-task-file", dest="outputtaskfile",
                      #default="dataset-challenge/plain/dialog-task3OPTIONS-kb1_atmosphere-distr0.9-trn10000.plain",
                      default=None,
                      help="filename of the task", metavar="FILE")

    parser.add_option("--output-statistics", dest="outputstatistics",
                      default="statistics.plain",
                      help="filename of the task", metavar="FILE")

    (options, args) = parser.parse_args()

    return options.inputtaskfile, options.outputtaskfile, options.outputstatistics



### The current dialog format
### [{dialog_id : " ",
#     utterances: [" "],
#     candidates: [{candidate_id: " " , utterance: ""}, ... ],
#     answer: {candidate_id: " " , utterance: ""} ]

if __name__ == '__main__':

    # Parsing command line
    inputtaskfile, outputtaskfile, outputstatistics \
        = do_parse_cmdline()

    fd = open(inputtaskfile, 'rb')
    json_data = json.load(fd)
    fd.close()

    ### Print-out plain dialogs
    if (outputtaskfile != None):

        fd_out = open(outputtaskfile, 'wb')
        for story in json_data:

            fd_out.write(str('dialog_id: ') + str(story['dialog_id']) + "\n")

            fd_out.write(str("Utterances:\n"))
            for utterance in story['utterances']:
                fd_out.write(" * " + str(utterance) + "\n")

            fd_out.write("Candidates:\n")
            for cand in story['candidates']:
                fd_out.write(" * " + str(cand['candidate_id']) + " - " + str(cand['utterance']) + "\n")

            fd_out.write(str("Answer:\n"))
            if (story.get('answer') != None):
                fd_out.write(" * " + str(story['answer']['candidate_id'])
                             + " - " + str(story['answer']['utterance']) + "\n")
            else:
                fd_out.write(str(None) + "\n")
            fd_out.write("\n")
        fd_out.close()

    ### Print-out statistics
    if (outputstatistics != None):
        with open(outputstatistics, "wb") as fd_out:
            dict_stats = do_statistics(lst_dialogs=json_data)
            for key in dict_stats.keys():
                fd_out.write(str(key) + ":\n")
                fd_out.write(str(dict_stats[key]) + "\n\n")
