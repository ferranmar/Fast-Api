import oracledb
from core import config



def get_data():
    oracledb.init_oracle_client(lib_dir="/opt/oracle/instantclient_21_10")
    connection = oracledb.connect(
        user=config.ORACLE_USER,
        password=config.ORACLE_PSW,
        host="172.20.32.36", 
        port=1567, 
        sid="SIOM")
    


def start():
    get_data()


if __name__ == '__main__':
    start()