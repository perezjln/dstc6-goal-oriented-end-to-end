# Dialog State Tracking Challenge 6 (DSTC6)

## End-to-End Goal Oriented Dialog Learning

This track of the DSTC-6 challenge series is aiming to build End-to-End dialog systems for goal-oriented applications. Goal-oriented dialog technology is an important research issue and End-to-End dialog learning has emerged as a primary research subject in the domain of conversation agent learning. It consists in learning a dialog policy from transactional dialogs of a given domain. In this task, the automatic system responses generated using a given task-oriented dialog data will be evaluated. 

A full description of the task and the dataset is available here
http://workshop.colips.org/dstc6/proposals/Goal_Oriented_End_To_End_Dialog-Facebook-XRX.pdf

## Test Dataset format and submission
The test-set is composed with 4 subdirectories: "tst1", "tst2", "tst3", "tst4". 

A valid submission consists in a tarball (.tgz file) with the 4 subdirectories added in it. In each subdirectory of the test-set, 5 .json files have to be processed. The json files of the test-set follow the same format than the training files. A valid response file should have the same name than the corresponding test file with the suffixe ".answers.json" and should follow the format of the response file described in the description of the task. 

For example, the valid name of the test file "tst1/dialog-task1API-kb1_atmosphere-distr0.5-tst1000.json" must be "tst1/dialog-task1API-kb1_atmosphere-distr0.5-tst1000.answers.json".


## Contact Information
You can get the latest updates and participate in discussions on DSTC mailing list

To join the mailing list, send an email to: (listserv@lists.research.microsoft.com)
putting "subscribe DSTC" in the body of the message (without the quotes).
To post a message, send your message to: (dstc@lists.research.microsoft.com).
