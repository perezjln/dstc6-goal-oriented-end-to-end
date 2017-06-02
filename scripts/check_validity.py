
import json

### The current dialog format
### [{dialog_id : " ", lst_candidate_id: [{candidate_id: " ", rank: " "}, ...]}]

def do_parse_cmdline():

    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("--input-task-file", dest="inputtaskfile",
                      default="output-result-tfidf.json",
                      help="filename of the task", metavar="FILE")

    (options, args) = parser.parse_args()

    return options.inputtaskfile


if __name__ == '__main__':


    inputtaskfile = do_parse_cmdline()

    with open(inputtaskfile, 'rb') as fd:

        json_data = json.load(fd)

        if (type(json_data) != list):
            print "[Error] The result file should be a list ..."
            exit(1)

        for item in json_data:
            if (item.get("dialog_id") == None):
                print "[Error] No dialog_id key founded ..."
                exit(1)
            if (item.get('lst_candidate_id') == None):
                print "[Error] No lst_candidate_id key founded ..."
                exit(1)

            for candidate in item['lst_candidate_id']:
                if (candidate.get('rank') == None):
                    print "[Error] one candidate has no rank key ..."
                    exit(1)
                if (candidate.get('candidate_id') == None):
                    print "[Error] one candidate has no id key ..."
                    exit(1)


    print str("[Success]: Valid format")