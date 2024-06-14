from lib.database_connection import DatabaseConnection
from lib.user_repo import UserRepo
from lib.post_repo import PostRepo


class Application:
    def __init__(self) -> None:
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blogging_app.sql")

    def run(self):
        u_repo = UserRepo(self._connection)
        p_repo = PostRepo(self._connection)
        print('Hello, please choose from the following options.')
        while True:
            cmd = int(input('1 - User\n2 - Post '))
            if cmd == 1 :
                cmd2 = int(input('''
                1 - Print all
                2 - Find by ID
                3 - Create user
                4 - Delete by ID'''))
                if cmd2 == 1:
                    for object in u_repo.all():
                        print(object)
                if cmd2 == 2:
                    id = int(input('select id'))
                    print(u_repo.find(id))

                if cmd2 == 3:
                    tuple_user = input('Please input email,username: ')
                    tu_split = tuple_user.split(',')
                    u_repo.create(tu_split[0],tu_split[1])
                    print('Successfully added')
                
                if cmd2 == 4:
                    id = int(input('select id'))
                    u_repo.delete(id)
                    print('Successfully deleted')
    
            if cmd == 2:
                cmd2 = int(input('''
                1 - Print all
                2 - Find by ID
                3 - Create post
                4 - Delete by ID'''))
                if cmd2 == 1:
                    for object in p_repo.all():
                        print(object)
                    break
                if cmd2 == 2:
                    id = int(input('select id'))
                    print(p_repo.find(id))
                    break
                if cmd2 == 3:
                    tuple_user = input('Please input title,content,views,user_id: ')
                    tu_split = tuple_user.split(',')
                    p_repo.create(tu_split[0],tu_split[1],tu_split[2],tu_split[3])
                    print('Successfully added')
                    break
                if cmd == 4:
                    id = int(input('select id'))
                    p_repo.delete(id)
                    print('Successfully deleted')
                    break



if __name__ == '__main__':
    app = Application()
    app.run()