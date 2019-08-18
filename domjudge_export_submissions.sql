use domjudge;
SELECT
	submission.submitid,
	team.NAME AS 'candidate',
	contestproblem.shortname AS '#',
	problem.NAME AS 'problem_name',
	langid AS 'language',
	CONVERT(submission_file.sourcecode,CHAR) AS 'sourcecode'
FROM
	contestproblem,
	problem,
	judging,
	submission,
	team,
	submission_file 
WHERE
  submission.probid = problem.probid 
	AND submission.teamid = team.teamid 
	AND submission.submitid = submission_file.submitid 
	AND judging.submitid = submission_file.submitid 
	AND contestproblem.cid = submission.cid 
	AND contestproblem.probid = submission.probid 
	AND submission.cid = 1 
	AND judging.result = 'correct';