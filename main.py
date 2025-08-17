import pandas as pd
import json

def read_json(json_file):

    with open(json_file, 'r') as f:
        data = json.load(f)
    
    sub_data = []
    for lesson in data['lessons']:
        lesson_dict = {}
        lesson_dict['nameZh'] = lesson['course']['nameZh']
        lesson_dict['nameEn'] = lesson['course']['nameEn']
        lesson_dict['dateTimePlacePersonText'] = lesson['scheduleText']['dateTimePlacePersonText']
        lesson_dict['sub_lessons'] = []
        for sub_lesson in lesson_dict['dateTimePlacePersonText']['textZh'].split('; \n'):
            week, weekday, time, place, person = sub_lesson.split(' ')
            sub_lesson_dict = {
                'week': week,
                'weekday': weekday,
                'time': time,
                'place': place,
                'person': person
            }
            lesson_dict['sub_lessons'].append(sub_lesson_dict)
        sub_data.append(lesson_dict)
    return sub_data

def format_csv(sub_data):
    df = pd.DataFrame(columns=['课程名称',
                               '星期',
                               '开始节数',
                               '结束节数',
                               '老师',
                               '地点',
                               '周数'])
    weekday_map = {
        '星期一' : '1',
        '星期二' : '2',
        '星期三' : '3',
        '星期四' : '4',
        '星期五' : '5',
        '星期六' : '6',
        '星期天' : '7',
        '星期日' : '7'
    }

    for lesson in sub_data:
        for sub_lesson in lesson['sub_lessons']:
            new_week = sub_lesson['week']
            new_week = new_week.replace('周', '')
            new_week = new_week.replace('~', '-')
            new_week = new_week.replace(',', '、')
            new_week = new_week.replace('(', '')
            new_week = new_week.replace(')', '')
            sub_lesson['week'] = new_week
            df = df._append({
                '课程名称': lesson['nameZh'],
                '星期': weekday_map[sub_lesson['weekday']],
                '开始节数': sub_lesson['time'].split('~')[0],
                '结束节数': sub_lesson['time'].split('~')[1][:-1],
                '老师': sub_lesson['person'],
                '地点': sub_lesson['place'],
                '周数': sub_lesson['week']
            }, ignore_index=True)
    return df

if __name__ == "__main__":
    json_file = 'data.json'
    sub_data = read_json(json_file)
    df = format_csv(sub_data)
    df.to_csv('output.csv', index=False)
