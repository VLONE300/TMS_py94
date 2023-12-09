from home_works.lesson14.file_worker import FileWorker


def app():
    fw = FileWorker('E:\\Python\\TMS_py94\\qwerty.json')
    content = fw.read()
    fw.append('obj1')
    fw.append('obj2')
    fw.close()
    return content


print(app())
