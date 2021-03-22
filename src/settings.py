import os, sys


baseDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    CSRF_ENABLED=True
    SECRET_KEY = os.getenv('SECRET_KEY', 'Zench')
    CACHE_TYPE='simple'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOBS = [
        {
            'id': 'job1',                
            'func': 'src:cron.job1',          
            'args': None,              
            'trigger': 'cron',                     # 指定任务触发器 cron
            'day_of_week': 'mon-fri',              # 每周1至周5下午16点执行 
            'hour': 16,
            'minute': 1                        
        }
    ]
    SCHEDULER_API_ENABLED = True

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', os.path.join(baseDir, 'stock_dev.db'))
    
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI', os.path.join(baseDir,'stock_test.db'))

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', os.path.join(baseDir, 'stock.db'))

configs={
    'development':DevelopmentConfig,
    'test':TestConfig,
    'production':ProductionConfig
}