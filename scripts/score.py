
import json


### The current dialog format
### [{dialog_id : " ", lst_candidate_id: [{candidate_id: " ", rank: " "}, ...]}]

def do_parse_cmdline():

    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("--input-result-file-test", dest="inputfiletest",
                      default="output-result-tfidf.json",
                      help="filename of the task", metavar="FILE")

    parser.add_option("--input-result-file-truth", dest="inputfiletruth",
                      default="output-truth.json",
                      help="filename of the task", metavar="FILE")

    parser.add_option("--input-nb-candidate", dest="inputnbcandidate",
                      default=10,
                      help="nbr. candidate", metavar="INTEGER")

    (options, args) = parser.parse_args()

    return options.inputfiletest, options.inputfiletruth, \
           int(options.inputnbcandidate)


def do_load_json_result(filename, nb_candidate):

    dict_result = {}
    with open(filename, 'rb') as fd:

        json_data = json.load(fd)

        if (type(json_data) != list):
            print "[Error] The result file should be a list ..."
            exit(1)

        for item in json_data:

            if (item.get('dialog_id') == None):
                print "[Error] No dialog_id key founded ..."
                continue

            if (item.get('lst_candidate_id') == None):
                print "[Error] No lst_candidate_id key founded ..."
                exit(1)

            lst_candidate = [None] * nb_candidate
            for candidate in item['lst_candidate_id']:

                if (candidate.get('rank') == None):
                    print "[Error] one candidate has no rank key ..."
                    exit(1)
                if (candidate.get('candidate_id') == None):
                    print "[Error] one candidate has no candidate_id key ..."
                    exit(1)

                if (int(candidate["rank"]) <= nb_candidate):
                    lst_candidate[int(candidate["rank"]) - 1] = candidate['candidate_id']

            dict_result[item['dialog_id']] = lst_candidate


    return dict_result


def do_compute_score(dict_result_truth, dict_result_test, precision_at):

    nb_true  = 0.0
    for key in dict_result_truth.keys():
        if (dict_result_test.get(key) != None):
            if (dict_result_truth[key][0] in dict_result_test[key][0:precision_at]):
                nb_true += 1.0
    return nb_true / len(dict_result_truth)


if __name__ == '__main__':

    # Parsing command line
    inputfiletest, inputfiletruth, nbcandidate = do_parse_cmdline()

    dict_result_test   = do_load_json_result(inputfiletest, nbcandidate)
    dict_result_truth  = do_load_json_result(inputfiletruth, 1)

    ### Accuracy - Precision @1
    print str("Precision @1: ") + str(do_compute_score(dict_result_truth, dict_result_test, 1))
    print str("Precision @2: ") + str(do_compute_score(dict_result_truth, dict_result_test, 2))
    print str("Precision @5: ") + str(do_compute_score(dict_result_truth, dict_result_test, 5))