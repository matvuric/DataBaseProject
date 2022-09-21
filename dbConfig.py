import pymysql as sql
from config import host, user, password, db_name, months


def days_in_month(month, year):
  if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == \
    'October' or month == 'December':
    return 31
  elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    return 30
  elif month == 'February':
    if year % 4 != 0:
      return 28
    elif year % 100 == 0:
      if year % 400 == 0:
        return 29
      else:
        return 28
    else:
      return 29


if __name__ == '__main__':
  try:
      connection = sql.connect(
          host=host,
          port=3306,
          user=user,
          password=password,
          database=db_name,
          cursorclass=sql.cursors.DictCursor
      )
      print("Connected successfully")
  except Exception:
      print("Connection error")
      print(Exception)

  try:
    for year in range(2021, 2032):
      with connection.cursor() as cursor:
        create_table_query = "create table IF NOT EXISTS `year_%s`(month_name varchar(16), days int," \
                             " month_id int, primary key (month_id));"
        cursor.execute(create_table_query, year)
        print("table year_%d created successfully" % year)

      for month in range(len(months)):
        with connection.cursor() as cursor:
          insert_query = "INSERT IGNORE INTO `calendar`.`year_%s` ( `days`, `month_id`, `month_name`) " \
                         "VALUES ( '%s', '%s', %s);"
          cursor.execute(insert_query, (year, days_in_month(months[month], year), 
                                       int(str(year) + str(month + 1)), months[month]))
          connection.commit()
        with connection.cursor() as cursor:
          create_table_query = "create table IF NOT EXISTS `%s_%s`(day int," \
                               " holiday varchar(128), primary key (day));"
          cursor.execute(create_table_query, (year, month + 1))
          print("table %s_%s created successfully" % (year, months[month]))
        for day in range(days_in_month(months[month], year)):
          if (day == 0 or day == 1 or day == 2 or day == 3 or day == 4 or day == 5 or day == 7) and (
             month == 0):  # January
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                             "( '%s', 'New year');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 6) and (month == 0):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                             "( '%s', 'Christmas');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 9) and (month == 0):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                             "( '%s', 'Opened the Ice Castle in the garden Aquarium');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
                    # February
          elif (day == 21) and (month == 1):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                             "( '%s', 'The St. Petersburg Botanical Garden was established on " \
                             "Aptekarsky Island');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 22) and (month == 1):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Defender of the Fatherland Day');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
              # March
          elif (day == 7) and (month == 2):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                             "( '%s', 'International Woman`s day');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
              # April
          elif (day == 2) and (month == 3):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Decree issued on the construction of the first bridges');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 11) and (month == 3):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Consecration of the first wooden Peter and Paul Church');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
              # May
          elif (day == 0) and (month == 4):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'International Worker’s and May Day');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 8) and (month == 4):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Victory Day');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 23) and (month == 4):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Launching the cruiser Aurora');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 26) and (month == 4):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The Peter and Paul Fortress was founded; The Peter and " \
                              "Paul Hospital was opened');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
              # June
          elif (day == 3) and (month == 5):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The House of Peter I was laid');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 9) and (month == 5):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The stone Peter and Paul Cathedral was laid');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 11) and (month == 5):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Russia Day');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 14) and (month == 5):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Swedish squad burned three villages on Kamenny Island');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              # July
          elif (day == 3) and (month == 6):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'A wooden church was laid in the name of the apostles Peter " \
                              "and Paul');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 12) and (month == 6):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The wooden Kamennoostrovsky theater was opened ');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 22) and (month == 6):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Consecrated wooden Trinity Church on Trinity Square');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 24) and (month == 6):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Execution of the Decembrists on the shaft of the crownwork " \
                              "of the Peter and Paul Fortress');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 27) and (month == 6):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Burned down the Gluttony market on Troitskaya Square');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              # August
          elif (day == 7) and (month == 7):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Fire on the Petrograd side');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 10) and (month == 7):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The building of the Electrotechnical Institute was laid');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 13) and (month == 7):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The Leningrad Zoo was founded');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 23) and (month == 7):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Troitsky Bridge was laid');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 24) and (month == 7):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Explosion on Aptekarsky Island. The assassination attempt " \
                              "on P. A. Stolypin');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              # September
          elif (day == 10) and (month == 8):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The first folk festival in the Alexander Park');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 14) and (month == 8):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Celebration of the Peace of Nystad in St. Petersburg');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
          elif (day == 20) and (month == 8):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'The first catastrophic flood in St. Petersburg ');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              # November
          elif (day == 1) and (month == 10):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Peter I accepted the title of Peter the Great, Father of " \
                              "the Fatherland, Emperor of All Russia at the Trinity Cathedral');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          elif (day == 3) and (month == 10):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'National unity day');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
              # December
          elif (day == 11) and (month == 11):
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`, `holiday`) VALUES " \
                              "( '%s', 'Mint founded');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
          else:  # if there is no holiday
            with connection.cursor() as cursor:
              insert_query = "INSERT IGNORE INTO `calendar`.`%s_%s` ( `day`) VALUES ( '%s');"
              cursor.execute(insert_query, (year, month + 1, day + 1))
              connection.commit()
  finally:
    connection.close()
