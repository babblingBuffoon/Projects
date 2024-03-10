from icecream import ic

def get_grade(s1, s2, s3):
    # score = sum([s1 , s2 , s3]) / 3
    # match score:
    #     case s if 0 <= score < 60: return 'F'
    #     case s if 60 <= score < 70 : return 'D'
    #     case s if 70 <= score < 80: return 'C'
    #     case s if 80 <= score < 90: return 	'B'
    #     case s if 90 <= score <= 100: return 'A'
    #     case _: return 'score invalid'

    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get(round((s1 + s2 + s3) / 30), 'F')


ic(get_grade(50, 40, 80))  