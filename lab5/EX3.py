# define a list of survey response values.

Survey_responses = [5,7,3,8]

# define a tuple of survey respondent ID's

respondent_ids = (1012, 1035, 1021, 1053)

#create a dictionary by ziping together the lsts of tuple, with 
# IDs as key and responses as values

survey_dict = dict(zip(respondent_ids, Survey_responses))
print('survey response values:', Survey_responses)
print('survey respondent IDs:', respondent_ids)
print('survey dictionary:', survey_dict)

print( f' respondent { respondent_ids[2]} gave a response of {Survey_responses[2]}')
