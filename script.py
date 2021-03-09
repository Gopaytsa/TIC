import csv


def id():
  rec = 0 
  pStart = 1 
  pInterval = 1
  if (rec == 0): 
    rec = pStart 
  else: 
    rec = rec + pInterval 
  return 'GT-' + str(rec).zfill(3)

def action(data):
  data = input('')


def status(check_status):
  check_status = 1


def check_list_create(data):
    with open('database.csv', mode='a', newline='') as database2:
        check_list_id = id()
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([check_list_id, subject, message])

print(id())