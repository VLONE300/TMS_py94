from home_works.lesson14.file_worker import FileWorker


def app():
    fw = FileWorker('path')
    qw = fw.handler
    content = qw.read()
    qw.append('obj1')
    qw.append('obj2')
    qw.close()
