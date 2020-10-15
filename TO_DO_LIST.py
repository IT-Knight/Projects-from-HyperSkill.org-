from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
 
 
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
 
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today().date())
 
    def __repr__(self):
        return "(id='%s', task='%s', deadline='%s')" % (self.id, self.task, self.deadline)
 
 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
 
 
def today_task(option):
    rows = session.query(Table).filter_by(deadline=datetime.today().date()).order_by(Table.deadline).all()
    session.commit()
 
    if option == '1':
        print(f'\nToday {datetime.now().strftime("%d %a")}:')
        if len(rows) == 0:
            print('Nothing to do!\n')
        else:
            for index, row in enumerate(rows, 1):
                print(f"{index}. {row.task}")
            print()
    if option == '2':
        print()
        for x in range(7): #  вывод на 7 дней
            rows = session.query(Table).filter_by(deadline=(datetime.today().date() + timedelta(days=x))).order_by(Table.deadline).all()
            day = (datetime.today() + timedelta(days=x)).strftime('%A %d %b')
            print(day + ':')
            if len(rows) == 0:
                print('Nothing to do!\n')
            else:
                for index, row in enumerate(rows):
                    print(f"{index}. {row.task}")
                print()
 
    if option == '3':
        rows = session.query(Table).order_by(Table.deadline).all()
        print(f"\nAll tasks:")
        if not rows:
            print("Nothing to do!")
        else:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i].task} {rows[i].deadline:%d %b}")
            print()
 
 
    if option == '4':
        print()
        rows = session.query(Table).order_by(Table.deadline).all()
 
        count = 1
        for i, row in enumerate(rows):
            if datetime.strptime(str(row.deadline), '%Y-%m-%d') < datetime.today():
                print(f"{count}. {rows[i].task} {rows[i].deadline:%d %b}")
                count +=1
        if count == 1:
            print('Nothing is missed!')
        print()
 
 
def delete_task():
    print('\nChose the number of the task you want to delete:')
    rows = session.query(Table).order_by(Table.deadline).all()
    if not rows:
        print('Nothing to delete')
    else:
        for i in range(len(rows)):
            print(f"{i + 1}. {rows[i].task} {rows[i].deadline:%d %b}")
        row_task_to_delete = rows[int(input())-1]
        session.delete(row_task_to_delete)
        session.commit()
        print('The task has been deleted!')
    print()
 
 
def add_task():
    Session = sessionmaker(bind=engine)
    session = Session()
    new_task = input('\nEnter task\n')
    deadline = input('Enter deadline\n')
    new_row = Table(task=new_task, deadline=datetime.strptime(deadline, '%Y-%m-%d'))
    session.add(new_row)
    session.commit()
    print('The task has been added!\n')
 
 
def menu():
    while True:
        print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")
        option = input()
        if option =='0':
            print('\nBye!')
            break
        if option == '1':  # прямо за option его возьми ибо хуле
            today_task(option)
        if option == '2':
            today_task(option)
        if option == '3':
            today_task(option)
        if option == '4':
            today_task(option)
        if option == '5':
            add_task()
        if option == '6':
            delete_task()
 
 
if __name__ == '__main__':  
    menu()
